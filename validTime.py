"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
"""

def validTime(time):
    if int(time[:2])<24 and int(time[-2:])<60:
        return True
    else:
        return False
