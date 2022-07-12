"""Module that provides logging functions that the animations can use to provide 
animation data that could be useful for debugging"""
import logging

# for projectile motion
prev_x_dis = prev_y_dis = 0

def pm_log(x, y, new_x, new_y, x_off, y_off, u_x_off, u_y_off, cur_t, t_time, 
    verbose=True):
    global prev_x_dis, prev_y_dis
    """Logging for projectile motion animation"""
    if verbose:
        logging.debug(f"T_time: {t_time}\t|\tTime: {cur_t}s\n"
                    f"Current coordinates: ({x}, {y})\t|\t"
                    f"New coordinates: ({new_x}, {new_y})\n"
                    f"Unrounded offset: ({u_x_off}, {u_y_off})\t|\t"
                    f"Offset: ({x_off}, {y_off})\n"
                    f"Total x displacement: {x_off + prev_x_dis}\t|\t"
                    f"Total y displacement: {y_off + prev_y_dis}\n")
    else:
        # If not verbose, I only care about time and total displacement
        logging.debug(f"T_time: {t_time}\t|\tTime: {cur_t}s\n"
                      f"Total x displacement: {x_off + prev_x_dis}\t|\t"
                      f"Total y displacement: {y_off + prev_y_dis}\n")

    prev_x_dis, prev_y_dis = (x_off + prev_x_dis), (y_off + prev_y_dis)

def new_pm_log():
    global prev_x_dis, prev_y_dis
    prev_x_dis = prev_y_dis = 0
    logging.basicConfig(filename="./logs/projectile_motion_logs.txt", 
        level=logging.DEBUG)
    logging.debug("-" * 20)