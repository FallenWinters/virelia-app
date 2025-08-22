import tkinter as tk
from tkinter import ttk

class BadgesPage(tk.Frame):
    def __init__(self, stage, main):
        super().__init__(stage, bg="pink")
        self.title("Virelia")
        self.resizable(False, False)

        self.content = main

        self.petition_count = 0
        self.create_notebook()
        self.create_label()
        self.create_button()
        self.create_badge()
        self.create_footer()

    def assign_badge(self):
        if self.petition_count >= 10:
            return "gold badge: signed 10 petitions", "yellow"
        elif self.petition_count >= 5:
            return "silver badge: signed 5 petitions", "gray"
        elif self.petition_count >= 1:
            return "bronze badge: signed 1 petition", "brown"
        return "no badge: no petitions signed", "black"

    def create_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.tab_home = tk.Frame(self.notebook, bg="pink")
        self.tab_create = tk.Frame(self.notebook, bg="pink")
        self.notebook.add(self.tab_home, text="Home")
        self.notebook.add(self.tab_create, text="Create Petition")
        self.notebook.pack(expand=True, fill="both")
        
    def create_badge(self):
        badge_text, badge_color = self.assign_badge()
        self.badge_label = tk.Label(self.tab_home, text=badge_text, fg=badge_color, bg="pink", font=("Arial", 12))
        self.badge_label.pack(pady=20)
        
    def create_label(self):
        self.count_label = tk.Label(self.tab_home, text=f"Petitions Signed: {self.petition_count}", bg="pink")
        self.count_label.pack()
        
        tk.Label(self.tab_create, text="Subject", bg="pink").pack(pady=5)
        self.subject = tk.Entry(self.tab_create)
        self.subject.pack()
    
        tk.Label(self.tab_create, text="Description", bg="pink").pack(pady=5)
        self.desc = tk.Text(self.tab_create, height=4, width=25)
        self.desc.pack()

    def submit_petition(self):
        if self.subject.get() and self.desc.get("1.0", tk.END).strip():
            self.petition_count += 1
            text, color = self.assign_badge()
            self.badge_label.config(text=text, fg=color)
            self.count_label.config(text=f"Petitions Signed: {self.petition_count}")
            self.subject.delete(0, tk.END)
            self.desc.delete("1.0", tk.END)

    def create_button(self):
        tk.Button(self.tab_create, text="Submit", command=self.submit_petition).pack(pady=10)

    def create_footer(self):
        self.footer = tk.Frame(self, bg="#e84393", height=60)
        self.footer.pack(side="bottom", fill="x")

        buttons = ["Home", "Map", "Petition", "Badges", "Help"]
        for name in buttons:
            btn = tk.Button(self.footer, text=name, bg="#fab1a0", fg="black",
                            font=("Arial", 10, "bold"), height=2, width=8)
            btn.pack(side="left", expand=True, padx=5, pady=10)
