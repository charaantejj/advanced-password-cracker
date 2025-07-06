import tkinter as tk
from tkinter import filedialog, scrolledtext
from modules.rainbow_table import rainbow_crack

def launch_rainbow_gui():
    def browse_hash_file():
        path = filedialog.askopenfilename(title="Select Hash File", filetypes=[("Text Files", "*.txt")])
        hash_file_var.set(path)

    def browse_rainbow_table_file():
        path = filedialog.askopenfilename(title="Select Rainbow Table File", filetypes=[("Text Files", "*.txt")])
        rainbow_file_var.set(path)

    def start_cracking():
        hash_path = hash_file_var.get()
        rainbow_path = rainbow_file_var.get()
        if not hash_path or not rainbow_path:
            output_text.insert(tk.END, "Please select both files.\n")
            return
        output_text.delete("1.0", tk.END)
        result = rainbow_crack(hash_path, rainbow_path)
        output_text.insert(tk.END, result)

    window = tk.Tk()
    window.title("Rainbow Table Attack")
    window.geometry("800x600")
    window.configure(bg="#0f0f0f")

    title = tk.Label(window, text="RAINBOW TABLE ATTACK", font=("Consolas", 24), fg="#00ffff", bg="#0f0f0f")
    title.pack(pady=10)

    hash_file_var = tk.StringVar()
    rainbow_file_var = tk.StringVar()

    # Hash file input
    tk.Label(window, text="Select Hash File:", fg="#00ffff", bg="#0f0f0f", font=("Consolas", 12)).pack()
    tk.Entry(window, textvariable=hash_file_var, width=80).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_hash_file, bg="#1f1f1f", fg="#00ffff").pack()

    # Rainbow table input
    tk.Label(window, text="Select Rainbow Table File:", fg="#00ffff", bg="#0f0f0f", font=("Consolas", 12)).pack(pady=10)
    tk.Entry(window, textvariable=rainbow_file_var, width=80).pack(pady=5)
    tk.Button(window, text="Browse", command=browse_rainbow_table_file, bg="#1f1f1f", fg="#00ffff").pack()

    # Start button
    tk.Button(window, text="Start Cracking", command=start_cracking, bg="#00ffff", fg="#000000", font=("Consolas", 12, "bold")).pack(pady=20)

    # Output text area
    output_text = scrolledtext.ScrolledText(window, width=100, height=20, bg="#1e1e1e", fg="#00ffff", font=("Consolas", 10))
    output_text.pack(pady=10)

    window.mainloop()
