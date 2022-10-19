from asyncore import poll3
from re import L
from time import sleep
from bot_functions import join_and_watch_meeting, launch_zoom, get_upcoming_meeting, launch_zoom, exit_zoom
import multiprocessing as mp

TIME_FOR_LAUCHING_ZOOM = 5  # Seconds

# Find next meeting.
meeting = get_upcoming_meeting()

# Process for launching zoom
p1_launch_zoom = mp.Process(target=launch_zoom)

# Process for joining into the meeting.
p2_join_and_watch_meeting = mp.Process(
    target=join_and_watch_meeting, args=(meeting,))

# Process for exiting zoom.
p3_exit_zoom = mp.Process(target=exit_zoom)

# Execution

p1_launch_zoom.start()
sleep(TIME_FOR_LAUCHING_ZOOM)

p2_join_and_watch_meeting.start()
p2_join_and_watch_meeting.join()

p3_exit_zoom.start()
p3_exit_zoom.join()
