# gui/website_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from modules.website_bruteforce import brute_force_login

def launch_website_gui():
    def browse_wordlist():
        path = filedialog.askopenfilename(title="Select Password Wordlist", filetypes=[("Text files", "*.txt")])
        wordlist_var.set(path)

    def start_attack():
        url = url_var.get().strip()
        username = username_var.get().strip()
        wordlist = wordlist_var.get().strip()
        user_field = user_field_var.get().strip()
        pass_field = pass_field_var.get().strip()

        if not url or not username or not wordlist:
            messagebox.showerror("Input Error", "Please fill all required fields.")
            return

        output_text.delete("1.0", tk.END)
        result = brute_force_login(url, username, wordlist, user_field, pass_field)
        output_text.insert(tk.END, result)

    window = tk.Toplevel()
    window.title("Website Brute Forcing")
    window.geometry("750x600")
    window.configure(bg="#0f0f0f")

    tk.Label(window, text="Website Brute Forcing", font=("Consolas", 20, "bold"), fg="lime", bg="#0f0f0f").pack(pady=10)

    url_var = tk.StringVar()
    username_var = tk.StringVar()
    wordlist_var = tk.StringVar()
    user_field_var = tk.StringVar(value="username")
    pass_field_var = tk.StringVar(value="password")

    entries = [
        ("Login URL:", url_var),
        ("Username:", username_var),
        ("Username Field Name:", user_field_var),
        ("Password Field Name:", pass_field_var)
    ]

    for label_text, var in entries:
        tk.Label(window, text=label_text, fg="lime", bg="#0f0f0f", font=("Consolas", 12)).pack()
        tk.Entry(window, textvariable=var, width=70).pack(pady=5)

    # Wordlist file
    tk.Label(window, text="Select Password Wordlist:", fg="lime", bg="#0f0f0f", font=("Consolas", 12)).pack(pady=5)
    tk.Entry(window, textvariable=wordlist_var, width=70).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_wordlist, bg="#1f1f1f", fg="lime").pack()

    # Launch attack
    tk.Button(window, text="Start Attack", command=start_attack,
              bg="lime", fg="black", font=("Consolas", 12, "bold")).pack(pady=15)

    # Output display
    output_text = tk.Text(window, height=15, width=90, bg="#1e1e1e", fg="lime", font=("Consolas", 10))
    output_text.pack(pady=10)

    window.mainloop()
