""" Reference
Formatting datetime values to standard formats """
import datetime

def ConvertTime(timedelta: int):

    # Get the total seconds from the timedelta
    total_time = int(timedelta.total_seconds())

    # Convert the total seconds to hours and minutes
    time_hours = total_time // 3600
    time_minutes = (total_time % 3600) // 60

    # Create a time object using the hours and minutes
    _datetime = datetime.time(time_hours, time_minutes)
    return _datetime.strftime('%I:%M %p')


def TimeBuilder(hours: int, minutes: int, seconds: int = 00) -> str:
    """ Build 24-hr time format for timepicker"""

    return ":".join([f"{hours:02d}", f"{minutes:02d}", f"{seconds:02d}"])
