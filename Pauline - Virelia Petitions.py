'''Virelia Petitions Page'''

import tkinter as tk

window = tk.Tk()
window.title("Virelia - Petitions")
window.geometry("320x568")
window.resizable(height=False, width=False)
window.config()

class Petition:
    def __init__(self, subject):
        self.subject = subject
    
    def make_petition(self, desc):
        self.desc = desc



window.mainloop()