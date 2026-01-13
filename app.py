# app.py
# v1.1 - compatible with EXE build

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os
import sys

from modules.loader import load_list
from modules.analyzer import analyze_password

passwords = []
weak_list = []

# --- Helper for PyInstaller ---
def resource_path(relative_path):
    """Return absolute path to resource, works for dev and PyInstaller"""
    try:
        base_path = sys._MEIPASS  # temporary folder PyInstaller uses
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load default weak.txt
default_weak_path = resource_path(os.path.join("data", "weak.txt"))
if os.path.exists(default_weak_path):
    weak_list = [p.lower() for p in load_list(default_weak_path)]
    print(f"Loaded default weak.txt with {len(weak_list)} entries")
else:
    print("Default weak.txt not found in data/ folder")

# --- GUI Functions ---
def load_passwords():
    global passwords
    file = filedialog.askopenfilename(title="Select passwords.txt")
    if not file:
        return
    passwords = load_list(file)
    messagebox.showinfo("Loaded", f"Loaded {len(passwords)} passwords")

def load_weak():
    global weak_list
    file = filedialog.askopenfilename(title="Select weak.txt")
    if not file:
        return
    weak_list = [p.lower() for p in load_list(file)]
    messagebox.showinfo("Loaded", f"Loaded {len(weak_list)} weak dictionary entries")

def analyze():
    if not passwords or not weak_list:
        messagebox.showerror("Error", "Load passwords and weak.txt first!")
        return

    output.delete(1.0, tk.END)
    weak_count = 0

    for pwd in passwords:
        status, reasons, suggestions = analyze_password(pwd, weak_list)

        if status in ("WEAK", "VERY WEAK"):
            weak_count += 1

        output.insert(tk.END, f"Password: {pwd}\n")
        output.insert(tk.END, f"Status: {status}\n")

        if reasons:
            output.insert(tk.END, "Reasons:\n")
            for r in reasons:
                output.insert(tk.END, f" - {r}\n")

        if suggestions:
            output.insert(tk.END, "Suggestions:\n")
            for s in suggestions:
                output.insert(tk.END, f" + {s}\n")

        output.insert(tk.END, "-" * 50 + "\n")

    output.insert(tk.END, f"\nTotal weak passwords: {weak_count}/{len(passwords)}")

def save_report():
    report = output.get(1.0, tk.END).strip()
    if not report:
        messagebox.showerror("Error", "Nothing to save!")
        return
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w", encoding='utf-8') as f:
            f.write(report)
        messagebox.showinfo("Saved", "Report saved successfully!")

# --- GUI Setup ---
app = tk.Tk()
app.title("Weak Password Checker GUI")
app.geometry("700x600")

tk.Button(app, text="Load passwords.txt", command=load_passwords).pack(pady=5)
tk.Button(app, text="Reload weak.txt", command=load_weak).pack(pady=5)
tk.Button(app, text="Analyze", command=analyze).pack(pady=5)
tk.Button(app, text="Save Report", command=save_report).pack(pady=5)

output = ScrolledText(app, height=25)
output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()
