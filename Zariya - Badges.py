import tkinter as tk
from tkinter import ttk


def assign_badge(count):
    if count >= 10:
        return "gold badge: signed 10 petitions"
    elif count >= 5:
        return "silver badge: signed 5 petitions"
    elif count >= 1:
        return "bronze badge: signed 1 petition"
    return "no badge: no petitions signed"


window = tk.Tk()
window.title("Virelia")
window.geometry("320x568")
window.resizable(False, False)

petition_count = 0

notebook = ttk.Notebook(window)

# Home tab (light orange)
tab_home = tk.Frame(notebook, bg="peachpuff")  
# Create Petition tab (baby pink)
tab_create = tk.Frame(notebook, bg="pink")      

notebook.add(tab_home, text="Home")
notebook.add(tab_create, text="Create Petition")
notebook.pack(expand=True, fill="both")

badge_label = tk.Label(tab_home, text=assign_badge(petition_count),
                       font=("Arial", 12), bg="peachpuff")
badge_label.pack(pady=20)

count_label = tk.Label(tab_home, text=f"Petitions Signed: {petition_count}",
                       bg="peachpuff")
count_label.pack()

tk.Label(tab_create, text="Subject", bg="pink").pack(pady=5)
subject = tk.Entry(tab_create)
subject.pack()

tk.Label(tab_create, text="Description", bg="pink").pack(pady=5)
desc = tk.Text(tab_create, height=4, width=25)
desc.pack()

def submit_petition():
    global petition_count
    if subject.get() and desc.get("1.0", tk.END).strip():
        petition_count += 1
        badge_label.config(text=assign_badge(petition_count))
        count_label.config(text=f"Petitions Signed: {petition_count}")
        subject.delete(0, tk.END)
        desc.delete("1.0", tk.END)

tk.Button(tab_create, text="Submit", command=submit_petition).pack(pady=10)

window.mainloop()

