from PyPDF2 import PdfMerger
import os

pdf_folder = r"C:\path\to\folder"
output_file = r"C:\path\to\output.pdf"

merger = PdfMerger()
for filename in sorted(os.listdir(pdf_folder)):
    if filename.lower().endswith(".pdf"):
        merger.append(os.path.join(pdf_folder, filename))

merger.write(output_file)
merger.close()
print("✅ Combined PDF created!")
