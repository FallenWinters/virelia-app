import tkinter as tk
from PIL import Image, ImageTk

# Single Root Window
root = tk.Tk()
root.title("Virelia")
root.geometry("360x430")
root.configure(bg="white")

# Header
header = tk.Frame(root, bg="#e84393", height=60)
header.pack(fill="x")
title = tk.Label(header, text="HELP", bg="#e84393", fg="white", font=("Arial", 16, "bold"))
title.pack(side="left", padx=10, pady=10)

# Icon Image - Reference
icons_img = Image.open("icons.png").resize((105, 65))
icons_photo = ImageTk.PhotoImage(icons_img)

icon1 = tk.Label(header, image=icons_photo, bg="#e84393")
icon1.image = icons_photo  # Keep a reference to prevent garbage collection
icon1.pack(side="right", padx=5, pady=5)

# Daily tips header
tip = tk.Label(root, text="Daily tip: Check the petitions page for local issues",
               bg="#f8c8dc", fg="black", font=("Arial", 10))
tip.pack(fill="x")

# Scrollbar container
container = tk.Frame(root)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, bg="white")
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_configure)

scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def resize_frame(event):
    canvas.itemconfig(scrollable_window, width=event.width)

canvas.bind("<Configure>", resize_frame)

# Example blocks for scrolling
for _ in range(10):
    block = tk.Frame(scrollable_frame, bg="#e17055", height=150)
    block.pack(fill="x", padx=10, pady=10)
    block.pack_propagate(False)

# Footer with buttons
footer = tk.Frame(root, bg="#e84393", height=60)
footer.pack(side="bottom", fill="x")

buttons = ["Home", "Map", "Petition", "Badges", "Help"]
for name in buttons:
    btn = tk.Button(footer, text=name, bg="#fab1a0", fg="black",
                    font=("Arial", 10, "bold"), height=2, width=8)
    btn.pack(side="left", expand=True, padx=5, pady=10)

root.mainloop()
