import tkinter as tk
class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Virelia")
        self.root.geometry("360x430")
        self.root.resizable(False, False)
        self.dark_mode = False
        self.light_theme = {
            "bg": "#E93B6D", "text": "white", "nav": "#F0A037",
            "tip_bg": "#FCD2E5", "tip_fg": "#6D2F3A", "card": "#ED6E52"
        }
        self.dark_theme = {
            "bg": "#2B2B2B", "text": "#FFFFFF", "nav": "#444444",
            "tip_bg": "#3C3C3C", "tip_fg": "#DDDDDD", "card": "#555555"
        }
        self.theme = self.light_theme
        self.root.configure(bg=self.theme["bg"])
        self.build_ui()
    def build_ui(self):
        self.header = tk.Frame(self.root, bg=self.theme["bg"], height=60)
        self.header.pack(fill="x")
        title = tk.Label(self.header, text="HOME", fg=self.theme["text"], bg=self.theme["bg"],
                         font=("Arial", 20, "bold"))
        title.pack(side="left", padx=10, pady=10)
        self.toggle_button = tk.Button(self.header, text=":crescent_moon:", bg=self.theme["nav"], fg=self.theme["text"],
                                       command=self.toggle_theme, bd=0, font=("Arial", 12))
        self.toggle_button.pack(side="right", padx=10, pady=10)
        icon = tk.Canvas(self.header, width=40, height=40, bg=self.theme["nav"], highlightthickness=0)
        icon.pack(side="right", padx=10, pady=10)
        icon.create_oval(10, 10, 30, 30, fill=self.theme["bg"])
        self.tip_bar = tk.Label(self.root,
                                text="Daily tip: Check the petitions page for local issues",
                                bg=self.theme["tip_bg"], fg=self.theme["tip_fg"], font=("Arial", 10))
        self.tip_bar.pack(fill="x")
        self.content_frame = tk.Frame(self.root, bg=self.theme["bg"])
        self.content_frame.pack(fill="both", expand=True)
        self.build_news_feed()
    def build_news_feed(self):
        canvas_frame = tk.Frame(self.content_frame, bg=self.theme["bg"])
        canvas_frame.pack(fill="both", expand=True)
        canvas = tk.Canvas(canvas_frame, bg=self.theme["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=self.theme["bg"])
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        news_data = [
            {"title": "Climate strike this Friday", "desc": "Join the Virelia students in city square."},
            {"title": "Petition hits 10K!", "desc": "Citizens show strong support for eco-change."},
            {"title": "New bike lanes coming soon", "desc": "Construction starts next week downtown."},
            {"title": "Tree planting success", "desc": "Over 500 trees planted in Greenpark."},
            {"title": "Youth council open", "desc": "Public welcome to attend the monthly talks."},
            {"title": "Workshops available", "desc": "Learn about local sustainability programs."},
            {"title": "Cleanup weekend", "desc": "Volunteers needed for Saturday's cleanup."},
            {"title": "Compost bins launched", "desc": "Waste sorting program begins Monday."},
            {"title": "Plastic ban official", "desc": "Virelia removes single-use plastic."},
            {"title": "Recycling upgrades", "desc": "New tech installed downtown."},
            {"title": "Community garden", "desc": "Teens grow food for shelters."},
            {"title": "Art contest open", "desc": "Posters about pollution awareness."},
        ]
        for news in news_data:
            card = tk.Frame(self.scrollable_frame, bg=self.theme["card"], padx=10, pady=5)
            card.pack(fill="x", pady=5, padx=10)
            inner = tk.Frame(card, bg=self.theme["card"])
            inner.pack(fill="x")
            img = tk.Canvas(inner, width=50, height=50, bg="#FFFFFF", highlightthickness=0)
            img.pack(side="left", padx=5)
            img.create_oval(5, 5, 45, 45, fill=self.theme["bg"])
            text_frame = tk.Frame(inner, bg=self.theme["card"])
            text_frame.pack(side="left", fill="both", expand=True, padx=5)
            tk.Label(text_frame, text=news["title"], font=("Arial", 10, "bold"),
                     bg=self.theme["card"], fg=self.theme["text"]).pack(anchor="w")
            tk.Label(text_frame, text=news["desc"], font=("Arial", 8),
                     wraplength=220, justify="left", bg=self.theme["card"], fg=self.theme["text"]).pack(anchor="w")
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.theme = self.dark_theme if self.dark_mode else self.light_theme
        self.root.configure(bg=self.theme["bg"])
        self.header.destroy()
        self.tip_bar.destroy()
        self.content_frame.destroy()
        self.build_ui()
if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()




