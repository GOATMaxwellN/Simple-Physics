"""Frame class that shows animation for projectile motion"""
from tkinter import *
from tkinter import ttk


class ProjectileMotionFrame(ttk.Frame):

    CANVAS_OPTIONS = {
        "width": 300,
        "height": 300
    }

    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        # Make sure frame fills up window
        self.pack(fill=BOTH, side=TOP, expand=True)

        # Just some temporary styling for visual aid
        ttk.Style(self).configure("TFrame", background="violet")

        self.create_canvas()
        self.create_configurables()

    def create_canvas(self):
        canvas = Canvas(self, **self.CANVAS_OPTIONS)
        canvas.pack(side=TOP, fill=BOTH)

    def create_configurables(self):
        config_frame = ttk.Frame(self)
        config_frame.pack(side=TOP, fill=BOTH)