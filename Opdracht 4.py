from deep_translator import GoogleTranslator
from pathlib import Path
from gtts import gTTS
from playsound import playsound
import os

# Stap 1: Vertaal alle .txt-bestanden in de bronmap
def vertaal_directory(source_map, target_map, bron_taal="en", doel_taal="nl"):
    source = Path(source_map)
    target = Path(target_map)
    target.mkdir(parents=True, exist_ok=True)

    for tekstbestand in source.glob("*.txt"):
        with open(tekstbestand, "r", encoding="utf-8") as file:
            inhoud = file.read()

        # In stukken hakken (Google Translate limiet is rond 5000 tekens)
        chunks = [inhoud[i:i+4500] for i in range(0, len(inhoud), 4500)]
        vertaalde_chunks = []
        for chunk in chunks:
            try:
                vertaling = GoogleTranslator(source=bron_taal, target=doel_taal).translate(chunk)
                vertaalde_chunks.append(vertaling)
            except Exception as e:
                print(f"Fout bij vertalen: {e}")
                vertaalde_chunks.append("[FOUT BIJ VERTALING]")

        output_path = target / tekstbestand.name
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(vertaalde_chunks))

    print(f"Vertaling voltooid. Bestanden opgeslagen in: {target}")

# Stap 2: Toon bestanden in de doelmap en laat gebruiker kiezen
def toon_bestanden_en_kies(pad):
    bestanden = list(Path(pad).glob("*.txt"))
    if not bestanden:
        print("Geen vertaalde bestanden gevonden.")
        return None

    print("\nVertaalde bestanden:")
    for i, bestand in enumerate(bestanden):
        print(f"{i + 1}. {bestand.name}")

    keuze = int(input("Kies een bestand om voor te laten lezen (nummer): ")) - 1
    return bestanden[keuze] if 0 <= keuze < len(bestanden) else None

# Stap 3: Lees gekozen tekstbestand voor met gTTS
def voorlezen_met_gtts(bestandspad):
    with open(bestandspad, "r", encoding="utf-8") as file:
        tekst = file.read()

    print("\nVoorlezen gestart...")
    tts = gTTS(tekst, lang='nl')
    audio_pad = "temp_audio.mp3"
    tts.save(audio_pad)
    playsound(audio_pad)
    os.remove(audio_pad)
    print("Voorlezen voltooid.")

# Hoofdprogramma
if __name__ == "__main__":
    bronmap = "bron_teksten"         # Zorg dat deze map bestaat met .txt-bestanden
    doelmap = "vertaald_teksten"     # Hier komen de vertaalde bestanden

    vertaal_directory(bronmap, doelmap)
    gekozen = toon_bestanden_en_kies(doelmap)
    if gekozen:
        voorlezen_met_gtts(gekozen)
