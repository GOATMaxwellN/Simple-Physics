""""""
from tkinter import *
from tkinter import ttk


class SimplePhysics:

    GEOMETRY = "500x500"
    REGULAR_FONT = ("Times", 15)
    HEADING_FONT = ("Times", 20, "bold")


    def __init__(self, root):
        self.root = root
        self.root.title("Simple Physics")
        self.root.geometry(self.GEOMETRY)

        # Create styles
        style = ttk.Style(self.root)
        style.configure("TLabel", font=self.REGULAR_FONT)
        style.configure("Heading.TLabel", font=self.HEADING_FONT)
        
        # Create the content frame
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.pack(fill=BOTH, expand=True)

        self.create_title()
        self.create_buttons()


    def create_title(self):
        """Creates the 'Simple Physics' label to the top of the menu screen"""
        # Create small frame that will hold the title label
        title_label_frame = ttk.Frame(self.mainframe)
        title_label_frame.pack(fill=X, side=TOP)
        # Big label saying 'Simple Physics'
        title_label = ttk.Label(title_label_frame, text="Simple Physics", 
            style="Heading.TLabel")
        title_label.pack(side=TOP)

    def create_buttons(self):
        """Creates the buttons that lead to the physics animations"""
        # Names of physics animations included
        physics_anims = (
            ("Projectile Motion", self.projectile_motion, (0, 0)),
        )

        # Frame that will hold all the buttons
        buttons_frame = ttk.Frame(self.mainframe)
        buttons_frame.pack(fill=BOTH, side=TOP, expand=True)

        pad = 5
        for anim, func, colrow in physics_anims:
            (ttk.Button(buttons_frame, text=anim, command=func)
                .grid(column=colrow[0], row=colrow[1], padx=pad, pady=pad))

    def projectile_motion(self):
        print("I will show you projectile motion")


if __name__ == "__main__":
    root = Tk()
    app = SimplePhysics(root)
    root.mainloop()