import customtkinter
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import split

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 800
    height = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("SplitRight")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        self.iconbitmap(os.path.join("..", "Images", "icon.ico"))

        self.bg_image = customtkinter.CTkImage(Image.open(os.path.join("..", "Images", "bg_gradient.jpg")),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="SplitRight", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=0, pady=(150, 15))


        self.login_frame.pack_propagate(False)

        self.config_label = customtkinter.CTkLabel(self.login_frame, text="Config File Path", font=customtkinter.CTkFont(size=12))
        self.config_label.grid(row=1, column=0, padx=40, pady=(20, 0), sticky="w")
        self.file_path = customtkinter.StringVar() 
        self.file_path.set("Enter Config File Path...")
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, textvariable=self.file_path, placeholder_text="Enter File Path...")
        self.username_entry.grid(row=2, column=0, padx=40, pady=(3, 10))
        
        self.upload_button = customtkinter.CTkButton(self.login_frame, text="Browse", command=self.browse_file, width=200)
        self.upload_button.grid(row=5, column=0, padx=40, pady=(15, 15))

        

        self.config_label = customtkinter.CTkLabel(self.login_frame, 
                                                   text="Save split pdfs in original pdf folder?", 
                                                   font=customtkinter.CTkFont(size=11), anchor="w")
        self.config_label.grid(row=6, column=0, padx=40, pady=(15, 0), sticky="w")

        self.checkbox = customtkinter.CTkCheckBox(self.login_frame, text="Preserve Folder Structure", command=self.on_checkbox_click)
        self.checkbox.grid(row=7, column=0, pady=(2, 10), padx=40, sticky="w")
        
        self.convert_button = customtkinter.CTkButton(self.login_frame, text="Split", command=self.convert_file, width=200)
        self.convert_button.grid(row=8, column=0, padx=40, pady=(15, 15))

        self.progress_bar = customtkinter.CTkProgressBar(self.login_frame, mode="indeterminate")
        self.progress_bar.grid(row=9, column=0, padx=40, pady=(15, 15))

    def on_checkbox_click(self):
        if self.checkbox.get() == 1:
            print("Checkbox is enabled")
            split.preserve_folder_structure = True
        else:
            print("Checkbox is disabled")
            split.preserve_folder_structure = False

    def get_formatted_path(self, full_path):
        path_parts = full_path.split(os.sep)
        if len(path_parts) > 2:
            abbreviated_path = f"{path_parts[0]}\\...\\{path_parts[-1]}"
        else:
            abbreviated_path = full_path
    
        return abbreviated_path

    def browse_file(self):
        global label
        file_path = filedialog.askopenfilename()
        if file_path:
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, file_path)
            input_path_text = "Input Path: "+self.get_formatted_path(split.getParsedConfig(self.file_path.get()).get("INPUT"))
            self.input_path_label = customtkinter.CTkLabel(self.login_frame, 
                                                        text=input_path_text,
                                                        font=customtkinter.CTkFont(size=12))
            self.input_path_label.grid(row=3, column=0, padx=40, pady=(10, 0), sticky="w")

            output_path_text = "Output Path: "+self.get_formatted_path(split.getParsedConfig(self.file_path.get()).get("OUTPUT"))
            self.output_path_label = customtkinter.CTkLabel(self.login_frame, 
                                                        text=output_path_text,
                                                        font=customtkinter.CTkFont(size=12))
            self.output_path_label.grid(row=4, column=0, padx=40, pady=(10, 0), sticky="w")
    
    def start_progress_bar(self):
        self.progress_bar.start() 
    def stop_progress_bar(self):
        self.progress_bar.stop()   

    def convert_file(self):
        if hasattr(self, 'input_path_label'):
            def threaded_convert():
                self.start_progress_bar()  
                split.start_splitting(self.file_path.get())  
                self.stop_progress_bar() 
                messagebox.showinfo("Splitting Complete", "Splitting is complete!")  
            threading.Thread(target=threaded_convert).start()
        else:
            messagebox.showinfo("Input Error", "Check your input/output fields in config file!")  
        

if __name__ == "__main__":
    app = App()
    app.mainloop()