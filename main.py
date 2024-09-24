import re
import os
from tkinter import Tk, messagebox

# Funzione per convertire il file VTT in TXT
def convert_vtt_to_txt(vtt_file, output_txt):
    try:
        # Aprire il file .vtt
        with open(vtt_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Creare un nuovo file .txt per salvare la trascrizione pulita
        with open(output_txt, 'w', encoding='utf-8') as output:
            for line in lines:
                # Rimuovere numeri di sequenza e timestamp
                if not re.match(r'^\d+$', line) and not re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}$', line) and line.strip():
                    output.write(line.strip() + ' ')  # Aggiungi spazio per migliorare la leggibilità

    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

# Funzione per convertire tutti i file VTT nella cartella 'vtt'
def convert_all_vtt_in_folder():
    # Ottenere la cartella in cui si trova il file dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Impostare la cartella 'vtt' come directory di input
    input_dir = os.path.join(script_dir, 'vtt')
    
    # Creare la cartella 'txt' se non esiste
    output_dir = os.path.join(script_dir, 'txt')
    os.makedirs(output_dir, exist_ok=True)
    
    # Controllare se la cartella 'vtt' esiste
    if not os.path.exists(input_dir):
        messagebox.showerror("Errore", f"La cartella '{input_dir}' non esiste.")
        return
    
    # Trovare tutti i file .vtt nella cartella 'vtt'
    vtt_files = [f for f in os.listdir(input_dir) if f.endswith('.vtt')]
    
    if not vtt_files:
        messagebox.showinfo("Nessun file", "Non ci sono file .vtt nella cartella 'vtt'.")
        return
    
    # Convertire ogni file .vtt in un file .txt
    for vtt_file in vtt_files:
        vtt_file_path = os.path.join(input_dir, vtt_file)
        output_txt_path = os.path.join(output_dir, os.path.splitext(vtt_file)[0] + '.txt')
        convert_vtt_to_txt(vtt_file_path, output_txt_path)
    
    messagebox.showinfo("Successo", f"Conversione completata! I file sono stati salvati nella cartella '{output_dir}'.")

# Funzione principale per avviare il processo di conversione
def main():
    # Creare la finestra principale (necessaria per visualizzare i messaggi)
    root = Tk()
    root.withdraw()  # Nascondere la finestra principale
    
    # Avviare la conversione
    convert_all_vtt_in_folder()

# Esegui la funzione principale
if __name__ == "__main__":
    main()
