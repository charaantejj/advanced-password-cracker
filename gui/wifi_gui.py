# gui/wifi_gui.py

import tkinter as tk
from tkinter import scrolledtext
from modules.wifi_cracker import crack_wifi

def launch_wifi_gui():
    def start_wifi_cracking():
        output_text.delete("1.0", tk.END)
        result = crack_wifi()
        output_text.insert(tk.END, result)

    window = tk.Tk()
    window.title("Wi-Fi Cracker")
    window.geometry("800x600")
    window.configure(bg="#0f0f0f")

    title = tk.Label(window, text="Wi-Fi Password Cracking", font=("Consolas", 20, "bold"), fg="#00ff00", bg="#0f0f0f")
    title.pack(pady=20)

    start_button = tk.Button(window, text="Start Cracking", command=start_wifi_cracking,
                             bg="#00ff00", fg="#000000", font=("Consolas", 12, "bold"))
    start_button.pack(pady=10)

    output_text = scrolledtext.ScrolledText(window, width=100, height=25, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 10))
    output_text.pack(pady=10)

    window.mainloop()
