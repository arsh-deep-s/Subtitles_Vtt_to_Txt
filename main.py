import re
import os
from tkinter import Tk, filedialog, messagebox

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

        messagebox.showinfo("Successo", f"Conversione completata! Il file è stato salvato come '{output_txt}'")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

# Funzione per aprire il file .vtt e avviare la conversione
def select_file():
    # Ottenere la cartella in cui si trova il file dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Aprire una finestra per selezionare il file .vtt con la cartella corrente come directory iniziale
    file_path = filedialog.askopenfilename(
        title="Seleziona il file VTT", 
        filetypes=[("VTT files", "*.vtt")],
        initialdir=script_dir  # Imposta la cartella di avvio
    )
    
    if file_path:
        # Creare la cartella 'txt' se non esiste
        output_dir = os.path.join(script_dir, 'txt')
        os.makedirs(output_dir, exist_ok=True)
        
        # Generare il nome per il file di output .txt nella cartella 'txt'
        output_txt = os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0] + ".txt")
        
        # Convertire il file .vtt in .txt
        convert_vtt_to_txt(file_path, output_txt)

# Funzione principale per avviare l'interfaccia
def main():
    # Creare la finestra principale
    root = Tk()
    root.withdraw()  # Nascondere la finestra principale
    messagebox.showinfo("VTT to TXT Converter", "Seleziona un file VTT per la conversione.")
    select_file()

# Esegui la funzione principale
if __name__ == "__main__":
    main()
