
import tkinter as tk
from tkintermapview import TkinterMapView

window = tk.Tk()
window.title("Virelia - Map")
window.geometry("320x568")
window.resizable(False, False)

header = tk.Frame(window, bg="#e84393", height=60)
header.pack(fill="x")
title = tk.Label(header, text="MAP", bg="#e84393", fg="white", font=("Arial", 16, "bold"))
title.pack(side="left", padx=10, pady=10)
tip = tk.Label(window, text="Daily tip: Check the petitions page for local issues",
               bg="#f8c8dc", fg="black", font=("Arial", 9))
tip.pack(fill="x")
label = tk.Label(window)
label.pack()
map_widget = TkinterMapView(window, width= 320, height= 430, corner_radius = 0)
map_widget.set_position(43.6532,-79.3832)
map_widget.place(relx=0.5, rely=0.5, anchor="center")
footer = tk.Frame(window, bg="#e84393", height=60)
footer.pack(side="bottom", fill="x")

buttons = ["Home", "Map", "Petition", "Badges", "Help"]
for name in buttons:
    btn = tk.Button(footer, text=name, bg="#fab1a0", fg="black",
                    font=("Arial", 10, "bold"), height=2, width=8)
    btn.pack(side="left", expand=True, padx=5, pady=10)
#thank you sanya for the header and button codes ^-^
window.mainloop()
