import tkinter as tk
from tkinter import ttk

class BadgesPage (tk.Frame):
    def __init__(self, stage, main):
        super().__init__(stage, bg="pink")
        self.title("Virelia")
        
        self.resizable(False, False)
    
        self.petition_count = 0


    
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
        self.tab_home = tk.Frame(notebook)
        self.tab_create = tk.Frame(notebook)
        self.notebook.add(tab_home, text="Home")
        self.notebook.add(tab_create, text="Create Petition")
        self.notebook.pack(expand=True, fill="both")
        
    def create_badge(self):
        self.badge_text, badge_color = assign_badge(petition_count)
        self.badge_label = tk.Label(tab_home, text=badge_text, fg=badge_color, font=("Arial", 12))
        self.badge_label.pack(pady=20)
        
    def create_label(self):
        self.count_label = tk.Label(tab_home, text=f"Petitions Signed: {petition_count}")
        self.count_label.pack()
        
        tk.Label(tab_create, text="Subject").pack(pady=5)
        self.subject = tk.Entry(tab_create)
        self.subject.pack()
    
        tk.Label(tab_create, text="Description").pack(pady=5)
        self.desc = tk.Text(tab_create, height=4, width=25)
        self.desc.pack()
    
    def submit_petition(self):
    
        if self.subject.get() and self.desc.get("1.0", tk.END).strip():
            self.petition_count += 1
            self.text, self.color = assign_badge(self.petition_count)
            self.badge_label.config(text=text, fg=color)
            self.count_label.config(text=f"Petitions Signed: {petition_count}")
            self.subject.delete(0, tk.END)
            self.desc.delete("1.0", tk.END)
    def create_button(self):
        tk.Button(tab_create, text="Submit", command=submit_petition).pack(pady=10)
