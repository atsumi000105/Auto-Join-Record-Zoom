from asyncore import poll3
from re import L
from time import sleep
from bot_functions import join_and_watch_meeting, launch_zoom, get_upcoming_meeting, launch_zoom, exit_zoom
import multiprocessing as mp

TIME_FOR_LAUCHING_ZOOM = 7  # seconds

# Ensuring that zoom isn't launched.
exit_zoom()


# Process for launching zoom
p1_launch_zoom = mp.Process(target=launch_zoom)

# Launching zoom in a child process.
p1_launch_zoom.start()
sleep(TIME_FOR_LAUCHING_ZOOM)

# Find next meeting.
meeting = get_upcoming_meeting()

join_and_watch_meeting(meeting)

exit_zoom()
