from asyncore import poll3
from re import L
from time import sleep
from bot_functions import meet, record, get_upcoming_meeting
import multiprocessing as mp
from utils import kill

meeting = get_upcoming_meeting()

# If no upcoming meeting exsist. exit program immediately.
if meeting == None:
    exit()

# Start recording
p_recording = mp.Process(target=record, args=(meeting,))
p_recording.start()

# Meet on zoom
p_meet = mp.Process(target=meet, args=(meeting,))
p_meet.start()

p_meet.join()
p_recording.join()
