# gui/main_window.py

import tkinter as tk
from gui.wordlist_gui import launch_wordlist_gui
from gui.rainbow_gui import launch_rainbow_gui
from gui.ntlm_gui import launch_ntlm_gui
from gui.wifi_gui import launch_wifi_gui
from gui.website_gui import launch_website_gui

def launch_main_window():
    root = tk.Tk()
    root.title("Advanced Password Cracker")
    root.geometry("900x400")
    root.configure(bg="#0f0f0f")

    frame = tk.Frame(root, bg="#0f0f0f", highlightbackground="lime", highlightthickness=2)
    frame.pack(expand=True)

    title = tk.Label(frame, text="Advanced Password Cracker", font=("Courier New", 24, "bold"), fg="lime", bg="#0f0f0f")
    title.grid(row=0, column=0, columnspan=5, pady=30)

    buttons = [
        ("Wordlist Attack", launch_wordlist_gui),
        ("Rainbow Table Attack", launch_rainbow_gui),
        ("Website Brute Forcing", launch_website_gui),
        ("Wi-Fi Password Cracking", launch_wifi_gui),
        ("NTLM Hash Cracker", launch_ntlm_gui)
    ]

    for idx, (label, action) in enumerate(buttons):
        btn = tk.Button(frame, text=label, command=action,
                        bg="#0f0f0f", fg="lime", font=("Courier New", 12),
                        highlightbackground="lime", highlightthickness=1, padx=10, pady=5)
        btn.grid(row=1, column=idx, padx=10)

    root.mainloop()
