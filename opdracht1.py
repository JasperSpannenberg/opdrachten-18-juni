import os


def hernoem_en_nummer_bestanden(map_naam):
    # Controleer of de map bestaat
    if not os.path.isdir(map_naam):
        print(f"De m1ap '{map_naam}' bestaat niet.")
        return

    # Haal alle bestandsnamen op uit de map
    bestanden = os.listdir(map_naam)

    # Filter de bestanden die alleen een geldig bestandstype zijn
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join(map_naam, bestand))]

    # Schrijf de oorspronkelijke bestandsnamen naar een tekstbestand
    with open("bestandsnamen.txt", "w", encoding="utf-8") as f:
        for naam in bestanden:
            f.write(naam + "\n")

    # Laat de bestandsnamen zien in de terminal
    print(f"\nBestanden in de map '{map_naam}':")
    for bestand in bestanden:
        print(bestand)  # Dit toont elk bestand in de map

    # Hernoem de bestanden
    for index, bestand in enumerate(bestanden, start=1):
        nieuwe_naam = f"movie_poster_{index:02d}{os.path.splitext(bestand)[1]}"

        # Volledige pad voor oude en nieuwe naam
        oude_pad = os.path.join(map_naam, bestand)
        nieuwe_pad = os.path.join(map_naam, nieuwe_naam)

        # Hernoem het bestand
        os.rename(oude_pad, nieuwe_pad)
        print(f"Hernoemd: {bestand} -> {nieuwe_naam}")

    print("\nAlle bestanden zijn hernoemd en genummerd.")


def hernoem_terug(map_naam):
    # Controleer of de map bestaat
    if not os.path.isdir(map_naam):
        print(f"De map '{map_naam}' bestaat niet.")
        return

    # Lees de oorspronkelijke bestandsnamen uit het bestand
    if not os.path.exists("bestandsnamen.txt"):
        print("Het bestand 'bestandsnamen.txt' bestaat niet. Kan niet terughernoemen.")
        return

    with open("bestandsnamen.txt", "r", encoding="utf-8") as f:
        originele_namen = f.readlines()

    # Haal de huidige bestandsnamen op in de map
    huidige_bestanden = os.listdir(map_naam)

    # Hernoem de bestanden terug naar hun oorspronkelijke naam
    for index, huidige_bestand in enumerate(huidige_bestanden):
        # Zorg ervoor dat we het bestand een originele naam geven
        originele_naam = originele_namen[index].strip()  # Verwijder eventuele extra nieuwe regels

        huidige_pad = os.path.join(map_naam, huidige_bestand)
        originele_pad = os.path.join(map_naam, originele_naam)

        # Hernoem het bestand terug naar de oorspronkelijke naam
        os.rename(huidige_pad, originele_pad)
        print(f"Hernoemd terug: {huidige_bestand} -> {originele_naam}")

    print("\nAlle bestanden zijn terughernoemd naar hun originele naam.")


def main():
    # Toon het menu aan de gebruiker
    print("Keuzeopties:")
    print("1. Hernoem en nummer bestanden")
    print("2. Hernoem bestanden naar originele naam")

    keuze = input("Maak je keuze (1 of 2): ")

    if keuze == "1":
        map_naam = input("Geef de naam van de map met afbeeldingen: ")
        hernoem_en_nummer_bestanden(map_naam)
    elif keuze == "2":
        map_naam = input("Geef de naam van de map met afbeeldingen: ")
        hernoem_terug(map_naam)
    else:
        print("Ongeldige keuze. Kies 1 of 2.")


if __name__ == "__main__":
    main()

