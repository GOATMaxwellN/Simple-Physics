"""Main module that shows window with main menu"""
from tkinter import *
from tkinter import ttk
from projectile_motion import ProjectileMotionFrame


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
        
        # Create the content frame for main menu
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.pack(fill=BOTH, expand=True)

        self.create_title()
        self.create_buttons()

        # Create all the frames going to be used
        self.cur_frame = self.mainframe
        self.frames = {
            "main_menu": self.mainframe,
            "projectile_motion": ProjectileMotionFrame
        }



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
            ("Projectile Motion", self.show_projectile_motion_frame, (0, 0)),
        )

        # Frame that will hold all the buttons
        buttons_frame = ttk.Frame(self.mainframe)
        buttons_frame.pack(fill=BOTH, side=TOP, expand=True)

        pad = 5
        for anim, func, colrow in physics_anims:
            (ttk.Button(buttons_frame, text=anim, command=func)
                .grid(column=colrow[0], row=colrow[1], padx=pad, pady=pad))

    def switch_frame(self, frame_name):
        """Switch to a different frame, which is usually going to be a 
        showing some physics animation"""
        self.cur_frame.destroy()
        self.cur_frame = self.frames[frame_name](self.root)
        self.cur_frame.pack(fill=BOTH, side=TOP, expand=True)

    def show_main_menu(self):
        """Shows the main menu frame"""
        # TODO: This doesn't work for main menu for now since the frame
        # holding the main menu is not a class to be initialiazed
        self.switch_frame("main_menu")

    def show_projectile_motion_frame(self):
        """Shows the projectile motion frame"""
        self.switch_frame("projectile_motion")


if __name__ == "__main__":
    root = Tk()
    app = SimplePhysics(root)
    root.mainloop()