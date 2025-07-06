# gui/ntlm_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from modules.ntlm_cracker import crack_ntlm_hash

def launch_ntlm_gui():
    def browse_wordlist():
        path = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text Files", "*.txt")])
        wordlist_var.set(path)

    def start_cracking():
        hash_input = hash_var.get().strip()
        wordlist_file = wordlist_var.get().strip()

        if not hash_input or not wordlist_file:
            messagebox.showerror("Input Error", "Please enter a hash and select a wordlist file.")
            return

        result = crack_ntlm_hash(hash_input, wordlist_file)
        messagebox.showinfo("Result", result)

    window = tk.Toplevel()
    window.title("NTLM Hash Cracker")
    window.geometry("600x300")
    window.configure(bg="#0f0f0f")

    tk.Label(window, text="Enter NTLM Hash:", fg="lime", bg="#0f0f0f", font=("Courier New", 12)).pack(pady=5)
    hash_var = tk.StringVar()
    tk.Entry(window, textvariable=hash_var, width=80).pack(pady=5)

    tk.Label(window, text="Select Wordlist File:", fg="lime", bg="#0f0f0f", font=("Courier New", 12)).pack(pady=5)
    wordlist_var = tk.StringVar()
    tk.Entry(window, textvariable=wordlist_var, width=80).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_wordlist, bg="black", fg="lime").pack(pady=5)

    tk.Button(window, text="Start Cracking", command=start_cracking,
              bg="lime", fg="black", font=("Courier New", 12, "bold")).pack(pady=20)

    window.mainloop()
