import fitz
from PIL import Image
import pytesseract
import os

CONST_zoom_factor = 2

def parse_config(config_string):
    config_dict = {"INPUT": "", "OUTPUT": "", "OCR": []}
    section = None
    
    for line in config_string.splitlines():
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
        elif "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"')
            
            if section == "Files":
                if key.upper() in config_dict:
                    config_dict[key.upper()] = value
            elif section == "OCR":
                if key.startswith("Text"):
                    loc_key = "Loc" + key[-1]  # assumes Text1 and Loc1, Text2 and Loc2 pattern
                    loc_value = config_string.split(f"{loc_key}=")[1].split("\n")[0].strip()
                    coordinates = list(map(int, loc_value.split(",")))
                    
                    if len(coordinates) != 4:
                        raise ValueError(f"Error: {loc_key} should have exactly four integers. Found: {len(coordinates)}")
                    
                    loc_value = tuple(coordinates)
                    config_dict["OCR"].append((value, loc_value))
    
    config_dict["OUTPUT"] = os.path.normpath(config_dict["OUTPUT"])
    config_dict["INPUT"] = os.path.normpath(config_dict["INPUT"])
    return config_dict


def read_config_file(file_path):
    with open(file_path, 'r') as file:
        config_content = file.read()
    return config_content


def get_ocr_title(page, title, location, zoom_factor):
    # TO-DO what if text? page.get_text()
    page.set_cropbox(fitz.Rect(location[0], location[1], location[2], location[3]))
    pix = page.get_pixmap(matrix = zoom_factor)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img)

    # reader = easyocr.Reader(['en'], 'cpu')
    # results = reader.readtext(np.array(img))
    # text = ' '.join([result[1] for result in results])

    page.set_cropbox(page.mediabox)

    return True if (title.lower() in text.lower()) else False   # Lowercase Appearance 