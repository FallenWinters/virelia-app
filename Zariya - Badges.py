import tkinter as tk
from tkinter import ttk

def assign_badge(count):
    if count >= 10:
        return "gold badge: signed 10 petitions", "yellow"
    elif count >= 5:
        return "silver badge: signed 5 petitions", "gray"
    elif count >= 1:
        return "bronze badge: signed 1 petition", "brown"
    return "no badge: no petitions signed", "black"

window = tk.Tk()
window.title("Virelia")
window.geometry("320x568")
window.resizable(False, False)

petition_count = 0

notebook = ttk.Notebook(window)
tab_home = tk.Frame(notebook)
tab_create = tk.Frame(notebook)
notebook.add(tab_home, text="Home")
notebook.add(tab_create, text="Create Petition")
notebook.pack(expand=True, fill="both")

badge_text, badge_color = assign_badge(petition_count)
badge_label = tk.Label(tab_home, text=badge_text, fg=badge_color, font=("Arial", 12))
badge_label.pack(pady=20)

count_label = tk.Label(tab_home, text=f"Petitions Signed: {petition_count}")
count_label.pack()

def open_other_page():
    new_window = tk.Toplevel(window)
    new_window.title("Other Page")
    new_window.geometry("320x568")
    tk.Label(new_window, text="Welcome to the other page!").pack(pady=20)
    tk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

tk.Button(tab_home, text="Go to other page", command=open_other_page).pack(pady=10)

tk.Label(tab_create, text="Subject").pack(pady=5)
subject = tk.Entry(tab_create)
subject.pack()

tk.Label(tab_create, text="Description").pack(pady=5)
desc = tk.Text(tab_create, height=4, width=25)
desc.pack()

def submit_petition():
    global petition_count
    if subject.get() and desc.get("1.0", tk.END).strip():
        petition_count += 1
    
        text, color = assign_badge(petition_count)
        badge_label.config(text=text, fg=color)
        count_label.config(text=f"Petitions Signed: {petition_count}")
        subject.delete(0, tk.END)
        desc.delete("1.0", tk.END)

tk.Button(tab_create, text="Submit", command=submit_petition).pack(pady=10)

window.mainloop()

