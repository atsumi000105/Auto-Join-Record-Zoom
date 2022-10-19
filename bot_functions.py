from calendar import c
import subprocess
from tkinter import N
from traceback import print_tb
import pyautogui
from time import sleep
import json
from datetime import datetime
from utils import get_remaining_minutes_to_start

ONE_HOUR_IN_SECONDS = 3600
ZOOM_LAUNCH_TIME = 5  # seconds


def launch_zoom():
    # Opens up the zoom app.
    # Change the path specific to your computer

    # If on windows use below line for opening zoom
    # subprocess.call('C:\\myprogram.exe')

    # If on mac / Linux use below line for opening zoom
    #subprocess.run(['echo hi', '&', ''])

    print("Lauching Zoom...")
    subprocess.call("/usr/bin/zoom", shell=True)
    exit()


def exit_zoom():
    # Closes the zoom app.

    subprocess.call("sudo kill -9 $(pidof zoom)", shell=True)


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
        exit()

    print("Joining into the meeting...")
    # Clicks the join button
    # join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    # pyautogui.moveTo(join_btn)
    # pyautogui.click()

    # # Type the meeting ID
    # meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button.png')
    # pyautogui.moveTo(meeting_id_btn)
    # pyautogui.click()
    # pyautogui.write(meeting.id)

    # # Disables both the camera and the mic
    # media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    # for btn in media_btn:
    #     pyautogui.moveTo(btn)
    #     pyautogui.click()
    #     sleep(2)

    # # Hits the join button
    # join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    # pyautogui.moveTo(join_btn)
    # pyautogui.click()

    # sleep(5)
    # # Types the password and hits enter
    # meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    # pyautogui.moveTo(meeting_pswd_btn)
    # pyautogui.click()
    # pyautogui.write(meeting.pswd)
    # pyautogui.press('enter')

    # Sleep until the meeting ends.
    sleep(meeting['duration'] * ONE_HOUR_IN_SECONDS)

    print("Meeting ends...")

    exit()
