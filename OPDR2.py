import os
from PIL import Image

def is_image(file):
    try:
        Image.open(file).verify()
        return True
    except Exception:
        return False

def resize_image(image_path, output_path, max_size):
    with Image.open(image_path) as img:
        img.thumbnail((max_size, max_size))
        img.save(output_path)
        print(f"Aangepast: {os.path.basename(image_path)}")

def main():
    source_dir = input("Geef het pad op naar de bronmap met afbeeldingen: ")
    output_dir = input("Geef het pad op naar de doelmap voor aangepaste afbeeldingen: ")
    max_size = int(input("Wat is het maximale formaat in pixels? (max 2000): "))

    if max_size > 2000:
        print("Maximale grootte is 2000 pixels. Gebruik een lager getal.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(source_dir)
    image_files = [f for f in files if is_image(os.path.join(source_dir, f))]

    print(f"Totaal gevonden bestanden: {len(files)}")
    print(f"Aantal afbeeldingen: {len(image_files)}")
    print(f"Niet-afbeeldingen worden overgeslagen.")

    for file in files:
        source_path = os.path.join(source_dir, file)
        if not is_image(source_path):
            print(f"Overgeslagen (geen afbeelding): {file}")
            continue
        output_path = os.path.join(output_dir, file)
        resize_image(source_path, output_path, max_size)

    print("Klaar!")

if __name__ == "__main__":
    main()

