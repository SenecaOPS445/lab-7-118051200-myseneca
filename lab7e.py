#!/usr/bin/env python3
# Student ID: 118051200

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    function attributes: __init__, __str__, __repr__,
                         time_to_sec, format_time,
                         change_time, sum_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return Time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return the sum."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        sum_time = sec_to_time(self_sec + t2_sec)
        return sum_time

    def change_time(self, seconds):
        """Change the time by adding/subtracting seconds"""
        time_seconds = self.time_to_sec()
        new_time = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert a Time object to a single integer representing the number of seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the Time object attributes"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def __str__(self):
        """Return a string representation for the object self"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object self with '.' instead of ':'"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object in hour, minute, second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
