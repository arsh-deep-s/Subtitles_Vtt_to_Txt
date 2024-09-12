import re

def convert_vtt_to_txt(vtt_file, output_txt):
    # Aprire il file .vtt
    with open(vtt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Creare un nuovo file .txt per salvare la trascrizione pulita
    with open(output_txt, 'w', encoding='utf-8') as output:
        for line in lines:
            # Rimuovere numeri di sequenza e timestamp (esempio: "00:00:00.620 --> 00:00:02.609")
            if not re.match(r'^\d+$', line) and not re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}$', line) and line.strip():
                output.write(line.strip() + ' ')  # Aggiungi spazio per migliorare la leggibilità

# Esegui la funzione
vtt_file = "Lez008_it1.vtt"  # Inserisci qui il percorso del file .vtt
output_txt = "trascrizione.txt"  # Il file di output
convert_vtt_to_txt(vtt_file, output_txt)

print("Conversione completata! Controlla il file 'trascrizione.txt'.")
