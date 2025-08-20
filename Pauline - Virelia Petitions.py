'''Virelia Petitions Page'''

import tkinter as tk

window = tk.Tk()
window.title("Virelia - Petitions")
window.geometry("320x568")
window.resizable(False, False)
window.config()

def make_petition():
    petiwin = tk.Toplevel(window)
    petiwin.title("Create a Petition")
    petiwin.geometry("300x300")
    #petiwin.resizable(False, False)
    petiwin.config()

    subj_label = tk.Label(petiwin, text="Subject:")
    subj_label.grid(column=0, row=0)
    subject = tk.Entry(petiwin)
    subject.grid(column=1, row=0)

    desc_label = tk.Label(petiwin, text="Description")
    desc_label.grid(column=0, row=1)
    desc_box = tk.Text(petiwin)
    desc_box.grid(column=1, row=2)

make_button = tk.Button(window, text="Create", command=make_petition)
make_button.grid(column=3, row=5)

window.mainloop()