"""Frame class that shows animation for projectile motion"""
import threading
from tkinter import *
from tkinter import ttk
from math import floor, sin, cos, radians
import logger
from time import sleep


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
        self.base_coords = None
        self.create_scene()

    def create_canvas(self):
        """Create and add canvas widget to frame"""
        # Width and height set to 1 in order to allow weight of rows to
        # determine size. Highlightthickness set to 0 to remove default
        # border in canvas
        self.canvas = Canvas(self, background=self.CANVAS_BG_COLOR, 
            highlightthickness=0, width=1, height=1)
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

        # Reset button
        ttk.Button(
            config_frame, text="Reset", command=self.reset_ball_position).grid(
            column=2, row=1)

    def create_scene(self):
        """Adds items to the canvas"""
        # Create floor
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        thickness = 5
        thickness_radius = thickness // 2
        line_center = thickness_radius + 1
        floor_coords = (0, h-line_center, w, h-line_center)
        floor_line = self.canvas.create_line(
            *floor_coords, fill="black", width=thickness)

        # Create ball on the floor
        offset = 10  # offset from left edge of canvas
        floor_h = floor_coords[1] - thickness_radius # floor height
        ball_d = 50  # diameter of ball
        self.base_coords = (
            offset, floor_h-ball_d, ball_d+offset, floor_h
        )
        self.ball = self.canvas.create_oval(*self.base_coords, fill="red")

    def reset_ball_position(self):
        self.canvas.coords(self.ball, *self.base_coords)

    def throw(self):
        """Starts projectile motion animation given configs"""
        def throw_animation():
            """Inner function that holds the while loop doing the animation.
            Done in a seperate thread so mainloop isn't interrupted"""
            # 50 is arbitrary, and actually needs to be adjusted depending
            # on how long animation lasts (how long it is in the air)
            time_steps = round(time_in_the_air * 20)
            time_step = time_in_the_air / time_steps
            time = 0
            x = y = 0  # local start positions
            logger.new_pm_log()
            for _ in range(time_steps+1):
                # get new pos
                new_x = h_vel * time
                new_y = v_vel*time - (1/2)*g*time**2
                # calculate difference from current pos for canvas.move()
                # then convert to pixels
                x_off = round((new_x - x) * upc_num)
                y_off = round((new_y - y) * upc_num)
                # LOG
                logger.pm_log(x, y, new_x, new_y, x_off, y_off, 
                            (new_x-x)*upc_num, (new_y-y)*upc_num, 
                            time, time_in_the_air, verbose=False)
                self.canvas.move(self.ball, x_off, -y_off)
                # set cur pos to new pos
                x, y = new_x, new_y
                time += time_step
                sleep(1/30)  # maintains a rough frame rate | sleep(1/frame_rate)
        
        # TODO: curently only works for when initial vertical displacement is 0
        # Convert angle to radians
        angle = radians(int(self.angle.get()))
        init_velocity = int(self.init_velocity.get())
        v_vel = init_velocity * sin(angle)
        h_vel = init_velocity * cos(angle)
        g = 9.8
        time_in_the_air = 2 * (v_vel/g)
        upc_num = 20  # unit to pixel conversion

        animation = threading.Thread(target=throw_animation)
        animation.start()
