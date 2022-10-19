from math import remainder


ONE_HOUR_IN_MINUTES = 60


def get_remaining_minutes_to_start(meeting, now):

    remaing_minutes = (
        (float(meeting['start_time']) - (float(now.strftime("%H")))) * ONE_HOUR_IN_MINUTES) - float(now.strftime('%M'))

    return remaing_minutes if remaing_minutes > 0 else None
