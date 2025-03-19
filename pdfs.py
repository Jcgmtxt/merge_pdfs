from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import os
import re

def add_header(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, text)
    c.showPage()
    c.save()
    buffer.seek(0)
    return PdfReader(buffer)

def merge_pdfs(pdf_files, output_filename):
    writer = PdfWriter()
    
    for index, pdf_file in enumerate(pdf_files, start=1):
        header_pdf = add_header(f"Audio {index}")
        for page in header_pdf.pages:
            writer.add_page(page)
        
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output_filename, "wb") as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":
    pdf_folder = "./pdfs"  # Carpeta donde están los archivos PDF
    output_file = "audios_combinados.pdf"
    
    def extract_number(filename):
        match = re.search(r"\d+", filename)
        return int(match.group()) if match else float("inf")
    
    pdf_files = sorted(
        [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")],
        key=extract_number
    )
    
    merge_pdfs(pdf_files, output_file)
    print(f"PDF combinado guardado como {output_file}")
