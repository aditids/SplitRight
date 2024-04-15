# SplitRight

SplitRight is a standalone tool designed with ease of use in mind. It effortlessly splits combined PDF documents into individual files, catering specifically to the needs of legal firms. Powered by Optical Character Recognition (OCR) technology, it automates the process of document organization and management. With its user-friendly interface and efficient functionality, our tool offers a seamless solution for legal professionals seeking to streamline their workflow and enhance productivity.

# Features
1. PDF Splitting: Split PDF files into multiple documents based on text content.
2. OCR Technology: Utilizes Tesseract which is one of the fastest Optical Character Recognition technique to accurately identify content in PDF files.
3. User-Friendly Interface: Intuitive design for easy navigation and operation.
4. **Preserve Folder Structure** (Additional feature): Privilege to save the new split pdfs near the original pdf's folder to help organize pdfs into subdirectories instead saving all files mixed together in one output folder.

# System Architecture
<img src="https://github.com/pbadhe/SplitRight/blob/main/Images/SystemArchitecture.png" alt="Image Description" width="600" height="400">


# How to Use
1. Open the Configuration file: Click the "Browse" button to select the configuration file. This file contains the following information:
   1. The path of the PDF file you wish to upload.
   2. The output path where you want the separated PDFs to be stored.
   3. The basis on which you want the PDFs to be split (e.g., based on specific text).
   4. The location or coordinates of the keywords on the page of the PDF where they can be found for splitting. Below image is for reference.
      
   <img src="https://github.com/pbadhe/SplitRight/blob/main/Images/Sample_Config_file.png" alt="Image Description" width="600" height="300">
2. OCR Processing: The application will process the PDF using OCR to identify text content.
3. Split PDF: Click on the "Convert" button to initiate the splitting process.

# Installation:
To start using SplitRight, simply follow these steps:
1. Download SplitRight: Visit our website at [pranavbadhe.live/SplitRight/](https://www.pranavbadhe.live/SplitRight/) and download the app.exe file.
2. Install Tesseract-OCR: Install Tesseract-OCR (standalone library) from [https://tesseract-ocr.github.io/tessdoc/Installation.html](https://tesseract-ocr.github.io/tessdoc/Installation.html) with appropriate instructions.
3. Run SplitRight: Once the download is complete, navigate where you downloaded the SplitRight.exe file and run it.
4. Enjoy SplitRight: Congratulations! You're now ready to use SplitRight to effortlessly split your combined PDFs. Happy organizing!

# Development:
1. If you're a developer and want to contribute to SplitRight or customize it further, follow these steps to set up your development environment:
2. Clone the Repository: Clone the SplitRight repository from GitHub to your local machine.
   1. customtkinter
   2. pytesseract
   3. tesseract
   4. tesserocr
3. Install Tesseract-OCR: Install Tesseract-OCR (standalone library) from https://tesseract-ocr.github.io/tessdoc/Installation.html with appropriate instructions.
3. Run SplitRight: Once the dependencies are installed, you can run SplitRight from the cloned repository to test your changes or contribute to the project by raising an issue.

# System Requirements
1. Operating System: Windows 10/11, macOS, or Linux
2. Processor: Dual-core processor or higher
3. RAM: 2GB or more
4. Disk Space: 100MB of free space

# Screenshots
<img src="https://github.com/pbadhe/SplitRight/assets/44113251/3095b197-ca00-4433-ae6f-581e17e3b8aa" width="400">


<img src="https://github.com/pbadhe/SplitRight/assets/44113251/d25cd4a7-13d3-49eb-9aa0-9e93ad125f73" width="400">

# Download Application from website
Link: [https://www.pranavbadhe.live/SplitRight/](https://www.pranavbadhe.live/SplitRight/)
