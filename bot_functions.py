from calendar import c
from os import nice
import re
import subprocess
from tkinter import N
from traceback import print_tb
import pyautogui as pg
from time import sleep
import json
import multiprocessing as mp
from datetime import datetime
from utils import get_remaining_minutes_to_start, kill

ONE_HOUR_IN_SECONDS = 3600
ZOOM_LAUNCH_TIME = 5  # seconds
TIME_FOR_LAUCHING_ZOOM = 7  # seconds
ADDITIONAL_ZOOM_TIME = 60  # seconds
ADDITIONAL_RECORDING_TIME = ADDITIONAL_ZOOM_TIME + 30  # seconds


def meet(meeting):

    # Launching zoom.
    p_zoom = mp.Process(target=zoom)
    p_zoom.start()
    sleep(TIME_FOR_LAUCHING_ZOOM)

    # Joining Meeting
    p_join_watch = mp.Process(target=join_and_watch_meeting, args=(meeting,))
    p_join_watch.start()
    p_join_watch.join()

    print("Watching the meeting...")
    # Sleep until the meeting ends.
    sleep(meeting['duration'] * ONE_HOUR_IN_SECONDS + ADDITIONAL_ZOOM_TIME)

    print("Meeting ends...")
    # Closing zoom
    kill(zoom)
    exit()


def record(meeting):

    # To ensure ffmpeg isn't running
    kill('ffmpeg')

    recording_duration = (
        meeting["duration"] * ONE_HOUR_IN_SECONDS) + ADDITIONAL_RECORDING_TIME

    recording_file_name = f'meeting{meeting["id"]}.mp4'

    subprocess.call(f'rm {recording_file_name}', shell=True)

    get_screen_resolution_command = "resulution=$(xdpyinfo | awk '/dimensions/{print $2}')"
    record_command = f'ffmpeg -video_size $resulution -framerate 25 -f x11grab -i :0.0+0,0 \
        -f alsa -i default -t {recording_duration} {recording_file_name}'
    subprocess.call(get_screen_resolution_command +
                    ";" + record_command, shell=True)


def zoom():
    # Opens up the zoom app.
    # Change the path specific to your computer

    # If on windows use below line for opening zoom
    # subprocess.call('C:\\myprogram.exe')

    # If on mac / Linux use below line for opening zoom
    #subprocess.run(['echo hi', '&', ''])

    # To ensure zoom isn't running
    kill('zoom')

    print("Lauching Zoom...")
    subprocess.call("/usr/bin/zoom", shell=True)
    exit()


def get_upcoming_meeting():
    # Finds the next meeting. Assuminig that the meetings are today.

    print("Looking for next meeting...")

    f = open('meetings.json')
    meetings = json.load(f)['meetings']

    if len(meetings) == 0:
        print('Your meetings.json file is either empty or wrong formated.')
        return None

    now = datetime.now()

    upcoming_meeting = None
    remaining_min_of_upcoming_meeting = None

    for meeting in meetings:
        remaining_min_of_current_meeting = get_remaining_minutes_to_start(
            meeting, now)

        if remaining_min_of_current_meeting == None:
            continue

        if remaining_min_of_upcoming_meeting == None:
            remaining_min_of_upcoming_meeting = remaining_min_of_current_meeting
            upcoming_meeting = meeting
            continue

        if (remaining_min_of_upcoming_meeting > remaining_min_of_current_meeting):
            upcoming_meeting = meeting
            remaining_min_of_upcoming_meeting = remaining_min_of_current_meeting

    if upcoming_meeting == None:
        print('No upcoming meeting found. Please check the start_time of your meetings.')
    else:
        print("Found next meeting: " + str(meeting['id']))

    return upcoming_meeting


def join_and_watch_meeting(meeting):
    # Joins in a zoom Meeting.
    # Assumed that zoom is open and visible on the screen.
    if meeting == None:
        return

    print("Joining into the meeting...")

    # Clicks the join button
    plus_join_btn = pg.locateOnScreen(
        "plus_join_btn.png", confidence=.8)
    if plus_join_btn == None:
        print("Plus_join_button could not be found.")
        exit()

    pg.moveTo(plus_join_btn)
    pg.click()
    sleep(2)

    # Type the meeting ID
    meeting_id_text_field = pg.locateCenterOnScreen(
        'meeting_id_text_field.png', grayscale=True, confidence=.8)
    if meeting_id_text_field == None:
        print("Meeting ID text field could not be found.")
        exit()

    pg.moveTo(meeting_id_text_field)
    pg.click()
    pg.write(str(meeting['id']))
    sleep(2)

    # Hits the join button
    join_btn = pg.locateCenterOnScreen(
        'join_btn.png', grayscale=True, confidence=.8)

    if join_btn == None:
        print("Join button could not be found.")
        exit()
    pg.moveTo(join_btn)
    pg.click()

    # sleep(5)
    # # Types the password and hits enter
    # meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    # pyautogui.moveTo(meeting_pswd_btn)
    # pyautogui.click()
    # pyautogui.write(meeting.pswd)
    # pyautogui.press('enter')

    sleep(5)

    # Switch to full screen.
    pg.hotkey("alt", "f10")

    exit()
