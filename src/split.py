import fitz
import helper
import os

preserve_folder_structure = False

def split_pdf(doc, parsed_config):
    title_visited = set()
    current_title = ""
    current_doc = fitz.open()
    output_dir = parsed_config.get("OUTPUT")

    for i, page in enumerate(doc):
        if not current_title:
            for config in parsed_config.get("OCR"): 
                title = config[0]
                location = config[1]
                if helper.get_ocr_title(page, title, location, helper.CONST_zoom_factor):
                    current_title = title
                    current_doc.insert_pdf(doc, from_page=i, to_page=i)
                    break

        else:
            for config in parsed_config.get("OCR"): 
                title = config[0]
                location = config[1]
                if helper.get_ocr_title(page, title, location, helper.CONST_zoom_factor):
                    if current_title != title:
                        save_pdf(doc, current_doc, current_title, title_visited, output_dir)
                        current_doc = fitz.open()
                        current_title = title
                        break
            
            current_doc.insert_pdf(doc, from_page=i, to_page=i)

    save_pdf(doc, current_doc, current_title, title_visited, output_dir)
    doc.close()


def save_pdf(doc, current_doc, current_title, title_visited, output_dir):
    print("Preserve is ", preserve_folder_structure)
    if not preserve_folder_structure:
        original_fname = os.path.splitext(os.path.basename(doc.name))[0]
    else:
        original_fname = doc.name[:-4]

    fname = f"{original_fname}_{current_title}.pdf"

    if current_title not in title_visited: 
        title_visited.add(current_title)
        current_doc.save(os.path.join(output_dir, fname))
    else:
        visited_doc = fitz.open(os.path.join(output_dir, fname))
        visited_doc.insert_pdf(current_doc)
        visited_doc.saveIncr()
        visited_doc.close()


def getParsedConfig(config_file_path):
    config_content = helper.read_config_file(config_file_path)
    parsed_config = {}
    try:
        parsed_config = helper.parse_config(config_content)
        print(parsed_config)
        if not parsed_config.get("OCR"):
            print("No text configurations found")
    except ValueError as e:
        print(e)

    return parsed_config


def start_splitting(config_file_path):
    parsed_config = getParsedConfig(config_file_path)
    
    try:
        input_dir = parsed_config.get("INPUT")
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    doc = fitz.open(file_path)
                    print(file_path)
                    print(doc.name)
                    split_pdf(doc, parsed_config)
    except Exception as e:
        print(e)
