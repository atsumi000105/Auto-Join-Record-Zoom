import imp
from math import remainder
import subprocess

ONE_HOUR_IN_MINUTES = 60


def get_remaining_minutes_to_start(meeting, now):

    remaing_minutes = (
        (float(meeting['start_time']) - (float(now.strftime("%H")))) * ONE_HOUR_IN_MINUTES) - float(now.strftime('%M'))

    return remaing_minutes if remaing_minutes > 0 else None


def kill(app_name):
    # Kills the given app.
    subprocess.call(
        f"pidof {app_name} && kill -9 $(pidof {app_name})", shell=True)
