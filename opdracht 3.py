import os
from pathlib import Path
from PIL import Image
from fpdf import FPDF

def convert_jpgs_to_pdf(source_folder: Path, output_pdf_path: Path):
    pdf = FPDF(unit="pt")

    image_files = sorted(source_folder.glob("*.jpg"))
    if not image_files:
        raise FileNotFoundError("Geen JPG-bestanden gevonden in de opgegeven map.")

    for image_path in image_files:
        img = Image.open(image_path)
        width, height = img.size
        pdf.add_page(format=(width, height))
        pdf.image(str(image_path), 0, 0, width, height)

    pdf.output(str(output_pdf_path))
    print(f"PDF opgeslagen als: {output_pdf_path}")

if __name__ == "__main__":
    bronmap = Path("C:/opdr/school-opdrachten/Afbeeldingen")
    uitvoerpad = Path("C:/opdr/school-opdrachten/Afbeeldingen/output.pdf")
    convert_jpgs_to_pdf(bronmap, uitvoerpad)
