from asyncore import poll3
from re import L
from time import sleep
from bot_functions import join_and_watch_meeting, zoom, get_upcoming_meeting, launch_zoom, exit_zoom, record, stop_recording
import multiprocessing as mp

TIME_FOR_LAUCHING_ZOOM = 7  # seconds

# Ensuring that zoom isn't launched.
exit_zoom()

# Process for starting recording.
p_recording = mp.Process(target=record)

# Start recording
p_recording.start()

# Process for launching zoom.
p_launch_zoom = mp.Process(target=zoom)

# Launching zoom in a child process.
p_launch_zoom.start()
sleep(TIME_FOR_LAUCHING_ZOOM)

# Find next meeting.
meeting = get_upcoming_meeting()

join_and_watch_meeting(meeting)

exit_zoom()

p_recording.terminate()
