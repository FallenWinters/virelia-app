import tkinter as tk
from tkintermapview import TkinterMapView

window = tk.Tk()
window.title("Virelia - Map")
window.geometry("320x568")
window.resizable(False, False)
label = tk.Label(window)
label.pack()
map_widget = TkinterMapView(window, width= 320, height= 400, corner_radius = 0)
map_widget.set_position(43.6532,-79.3832)
map_widget.place(relx=0.5, rely=0.5, anchor="center")
window.mainloop()
