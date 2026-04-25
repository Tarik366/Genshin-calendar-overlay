# Source - https://stackoverflow.com/a/4055612
# Posted by Bryan Oakley, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-26, License - CC BY-SA 4.0

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.attributes('-alpha', 0.8)
        self.attributes('-topmost', True)
        self.configure(bg="black")

        self.grip = tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)

    def add_widget(self, func):
        """Widget oluşturan fonksiyonu dekore eder,
        widget'ı frame'e ekler ve ismiyle attribute olarak saklar."""
        widget = func(self.content_frame)
        widget.pack(padx=4, pady=2)
        setattr(self, func.__name__, widget)  # self.floater.my_button gibi erişim
        return func

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")
