
import tkinter as tk
from tkintermapview import TkinterMapView

class VireliaMapApp(tk.Frame):
    def __init__(self, stage, main):
        super().__init__(stage, bg=white)
        self.window = window
        self.window.title("Virelia - Map")
        self.window.geometry("320x568")
        self.window.resizable(False, False)

        self.create_header()
        self.create_dailytips()
        self.create_map()
        self.create_buttonfooter()

    def create_header(self):
        header = tk.Frame(self.window, bg="#e84393", height=60)
        header.pack(fill="x")
        title = tk.Label(header, text="MAP", bg="#e84393", fg="white", font=("Arial", 16, "bold"))
        title.pack(side="left", padx=10, pady=10)

    def create_dailytips(self):
        tip = tk.Label(self.window, text="Daily tip: Check the petitions page for local issues",
                       bg="#f8c8dc", fg="black", font=("Arial", 9))
        tip.pack(fill="x")

    def create_map(self):
        self.map_widget = TkinterMapView(self.window, width=320, height=430, corner_radius=0)
        self.map_widget.set_position(43.6532, -79.3832) #torontos coordinates
        self.map_widget.place(relx=0.5, rely=0.5, anchor="center")

    def create_buttonfooter(self):
        footer = tk.Frame(self.window, bg="#e84393", height=60)
        footer.pack(side="bottom", fill="x")

        buttons = ["Home", "Map", "Petition", "Badges", "Help"]
        for name in buttons:
            btn = tk.Button(footer, text=name, bg="#fab1a0", fg="black",
                            font=("Arial", 10, "bold"), height=2, width=8)
            btn.pack(side="left", expand=True, padx=5, pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = VireliaMapApp(window)
    window.mainloop()


