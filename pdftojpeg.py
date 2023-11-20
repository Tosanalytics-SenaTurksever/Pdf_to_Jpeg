import os
import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_jpeg(pdf_folder, output_path, resolution):
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            pdf_document = fitz.open(pdf_path)
            
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                image = page.get_pixmap(matrix=fitz.Matrix(resolution/2, resolution/2))
                

                pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)

              
                output_filename = f"{output_path}/{pdf_file}.jpeg"
                pil_image.save(output_filename, "JPEG")

            pdf_document.close()


pdf_path = "C:/Desktop/MovedPdf/Pdfs"
output_path = "C:/Desktop/OutPutPath"
resolution = 300  

convert_pdf_to_jpeg(pdf_path, output_path, resolution)
