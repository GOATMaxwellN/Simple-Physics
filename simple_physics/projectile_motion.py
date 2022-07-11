"""Frame class that shows animation for projectile motion"""
from tkinter import *
from tkinter import ttk
from math import floor, sin, cos, radians


class ProjectileMotionFrame(ttk.Frame):

    CANVAS_BG_COLOR = "#CCD1D1"

    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        # Make sure frame fills up window
        self.pack(fill=BOTH, side=TOP, expand=True)
        
        # Configure the grid
        # First row will have a higher weight, making canvas bigger
        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Just some temporary styling for visual aid
        ttk.Style(self).configure("Config.TFrame", background="violet")

        self.create_canvas()
        self.create_configurables()
        # Need correct width and height values
        parent.update()

        # Canvas items and variables to be created
        self.ball = None
        self.floor_h = None
        self.create_scene()

    def create_canvas(self):
        """Create and add canvas widget to frame"""
        # width and height set to 1 in order to allow weight of rows to
        # determine size and keep proportions
        self.canvas = Canvas(self, background=self.CANVAS_BG_COLOR, 
            width=1, height=1)
        self.canvas.grid(column=0, row=0, sticky=(N, E, S, W))

    def create_configurables(self):
        """Create and add frame that holds the configuration options"""
        config_frame = ttk.Frame(self, style="Config.TFrame")
        config_frame.grid(column=0, row=1, sticky=(N, E, S, W))

        # Grid configurations
        for i in range(3):
            config_frame.columnconfigure(i, weight=1)
        config_frame.rowconfigure(0, weight=1)
        config_frame.rowconfigure(1, weight=1)

        # Settings to config projectile motion
        # Initial velocity
        self.init_velocity = StringVar(value="10")
        ttk.Label(config_frame, text="Initial velocity").grid(
            column=0, row=0, sticky=S)
        ttk.Entry(config_frame, textvariable=self.init_velocity).grid(
            column=0, row=1, sticky=N)
        # Angle
        self.angle = StringVar(value="45")
        ttk.Label(config_frame, text="Angle").grid(
            column=1, row=0, sticky=S)
        ttk.Entry(config_frame, textvariable=self.angle).grid(
            column=1, row=1, sticky=N)

        # Throw button
        ttk.Button(config_frame, text="Throw", command=self.throw).grid(
            column=2, row=0, rowspan=2)

    def create_scene(self):
        """Adds items to the canvas"""
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        # Create floor
        floor_coords = (0, floor(h*0.7), w, floor(h*0.7))
        floor_line = self.canvas.create_line(
            *floor_coords, fill="black", width=3)

        # Create ball on the floor
        offset = 10  # offset from left edge of canvas
        floor_h = floor_coords[1]  # floor height
        ball_d = 50  # diameter of ball
        self.ball = self.canvas.create_oval(
            offset, floor_h-ball_d, ball_d+offset, floor_h, fill="red"
        )

    def throw(self):
        """Starts projectile motion animation given configs"""
        # TODO: curently only works for when initial vertical displacement is 0
        # Convert angle to radians
        angle = radians(int(self.angle.get()))
        init_velocity = int(self.init_velocity.get())
        v_vel = init_velocity * sin(angle)
        h_vel = init_velocity * cos(angle)
        g = 9.8

        time_in_the_air = 2 * (v_vel/g)
        time = 0
        upc_num = 10  # unit to pixel conversion 
        print("init_velocity", init_velocity, "v_vel", v_vel, "h_vel", h_vel, "time in the air", time_in_the_air, sep=" ")
        x = y = 0  # local start positions
        while time <= time_in_the_air:
            print("cur_time ", time)
            # get new pos
            new_x = h_vel * time
            new_y = v_vel*time - (1/2)*g*time**2
            # calculate difference from current pos for canvas.move()
            # then convert to pixels
            x_off = floor((new_x - x) * upc_num)
            y_off = floor((new_y - y) * upc_num)
            self.canvas.move(self.ball, x_off, -y_off)
            # set cur pos to new pos
            x, y = new_x, new_y

            time += time_in_the_air / 2
