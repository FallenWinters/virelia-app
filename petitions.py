'''Virelia Petitions Page'''

import tkinter as tk


class PetitionsPage(tk.Frame):
    def __init__(self, parent, main):
        super().__init__(parent)
        self.title = "Virelia - Petitions"
        self.configure(bg="white")

    def header(self):
        self.header = tk.Frame(self, bg="#e84393", height=60)
        self.header.pack(fill="x")
        self.title = tk.Label(self.header, text="PETITIONS", bg="#e84393", fg="white", font=("Arial", 16, "bold"))
        self.title.pack(side="left", padx=10, pady=10)
        self.tip = tk.Label(self, text="Daily tip: Check the petitions page for local issues",
                       bg="#f8c8dc", fg="black", font=("Arial", 9))
        self.tip.pack(fill="x")

    def make_petition(self):
        self.petiwin = tk.Toplevel(self)
        self.petiwin.title("Create a Petition")
        self.petiwin.geometry("300x300")
        self.petiwin.resizable(False, False)
        self.petiwin.config()

        self.subj_label = tk.Label(self.petiwin, text="Subject:")
        self.subj_label.grid(column=0, row=0)
        self.subject = tk.Entry(self.petiwin)
        self.subject.grid(columnspan=2, column=1, row=0)

        self.desc_label = tk.Label(self.petiwin, text="Description")
        self.desc_label.grid(column=0, row=1)
        self.desc_box = tk.Text(self.petiwin, width=25, height=5)
        self.desc_box.grid(column=1, row=2)

        self.pet_button = tk.Button(self.petiwin, text="Publish Petition")
        self.pet_button.grid(column=1, row=4)



    def create_buttons(self):
        self.make_button = tk.Button(self, text="Create", command=lambda: self.make_petition())
        self.make_button.grid(column=3, row=5)

    def footer(self):
        self.footer = tk.Frame(self, bg="#e84393", height=60)
        self.footer.pack(side="bottom", fill="x")

        self.buttons = ["Home", "Map", "Petition", "Badges", "Help"]
        for name in self.buttons:
            btn = tk.Button(self.footer, text=name, bg="#fab1a0", fg="black",
                            font=("Arial", 10, "bold"), height=2, width=8)
            btn.pack(side="left", expand=True, padx=5, pady=10)
