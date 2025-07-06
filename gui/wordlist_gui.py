import tkinter as tk
from tkinter import filedialog, scrolledtext
from modules.wordlist_attack import crack_hashes_with_wordlist

def create_wordlist_gui():
    def browse_hash_file():
        path = filedialog.askopenfilename(title="Select Hash File", filetypes=[("Text Files", "*.txt")])
        hash_file_var.set(path)

    def browse_wordlist_file():
        path = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text Files", "*.txt")])
        wordlist_file_var.set(path)

    def start_cracking():
        hash_path = hash_file_var.get()
        wordlist_path = wordlist_file_var.get()
        if not hash_path or not wordlist_path:
            output_text.insert(tk.END, "Please select both files.\n")
            return
        output_text.delete("1.0", tk.END)
        result = crack_hashes_with_wordlist(hash_path, wordlist_path)
        output_text.insert(tk.END, result)

    window = tk.Tk()
    window.title("Wordlist Attack")
    window.geometry("800x600")
    window.configure(bg="#0f0f0f")

    title = tk.Label(window, text="WORDLIST ATTACK", font=("Consolas", 24), fg="#00ff00", bg="#0f0f0f")
    title.pack(pady=10)

    hash_file_var = tk.StringVar()
    wordlist_file_var = tk.StringVar()

    # Hash file selection
    tk.Label(window, text="Select Hash File:", fg="#00ff00", bg="#0f0f0f", font=("Consolas", 12)).pack()
    tk.Entry(window, textvariable=hash_file_var, width=80).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_hash_file, bg="#1f1f1f", fg="#00ff00").pack()

    # Wordlist file selection
    tk.Label(window, text="Select Wordlist File:", fg="#00ff00", bg="#0f0f0f", font=("Consolas", 12)).pack(pady=10)
    tk.Entry(window, textvariable=wordlist_file_var, width=80).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_wordlist_file, bg="#1f1f1f", fg="#00ff00").pack()

    # Start cracking
    tk.Button(window, text="Start Cracking", command=start_cracking, bg="#00ff00", fg="#000000", font=("Consolas", 12, "bold")).pack(pady=20)

    # Output field
    output_text = scrolledtext.ScrolledText(window, width=100, height=20, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 10))
    output_text.pack(pady=10)

    window.mainloop()

# Exported function used by main.py
def launch_wordlist_gui():
    create_wordlist_gui()
