import tkinter as tk
from tkinter import ttk

def assign_badge(count):
    if count >= 10: return "gold badge: signed 10 petitions", "gold"
    if count >= 5: return "silver badge: signed 5 petitions", "silver"
    if count >= 1: return "bronze badge: signed 1 petition", "brown"
    return "no badge: no petitions signed", "black"

def say_hello():
    badge_label.config(text="Hello! Please keep signing petitions!", fg="red")

window = tk.Tk()
window.title("Virelia")
window.geometry("320x568")
window.resizable(False, False)

petition_count = 0

notebook = ttk.Notebook(window)
tab_home = tk.Frame(notebook, bg="peachpuff")     # Light orange
tab_create = tk.Frame(notebook, bg="pink")        # Baby pink
notebook.add(tab_home, text="Home")
notebook.add(tab_create, text="Create Petition")
notebook.pack(expand=True, fill="both")

badge_text, badge_color = assign_badge(petition_count)
badge_label = tk.Label(tab_home, text=badge_text, fg=badge_color,
                       font=("Arial", 16, "bold"), bg="peachpuff")
badge_label.pack(pady=20)

count_label = tk.Label(tab_home, text=f"Petitions Signed: {petition_count}",
                       font=("Arial", 12), bg="peachpuff")
count_label.pack(pady=10)

tk.Button(tab_home, text="Say Hello", command=say_hello,
          bg="red", fg="white", font=("Arial", 12)).pack(pady=10)

tk.Label(tab_create, text="Subject", bg="pink").pack(pady=5)
subject = tk.Entry(tab_create, width=30)
subject.pack(pady=5)

tk.Label(tab_create, text="Description", bg="pink").pack(pady=5)
desc = tk.Text(tab_create, height=4, width=30)
desc.pack(pady=5)

def submit_petition():
    global petition_count
    if subject.get() and desc.get("1.0", tk.END).strip():
        petition_count += 1
        text, color = assign_badge(petition_count)
        badge_label.config(text=text, fg=color)
        count_label.config(text=f"Petitions Signed: {petition_count}")
        subject.delete(0, tk.END)
        desc.delete("1.0", tk.END)

tk.Button(tab_create, text="Submit", command=submit_petition,
          bg="green", fg="white").pack(pady=20)

window.mainloop()
