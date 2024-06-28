import datetime
import time
import os

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    return alarm_time

def validate_time(alarm_time):
    try:
        valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
        return valid_time
    except ValueError:
        return None

def sound_alarm():
    for _ in range(5):  # Beep 5 times
        print('\a')
        time.sleep(1)

def alarm_clock():
    alarm_time = set_alarm()
    valid_time = validate_time(alarm_time)

    if not valid_time:
        print("Invalid time format! Please enter time in HH:MM format.")
        return

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            sound_alarm()
            break
        time.sleep(30)  # Check every 30 seconds

if _name_ == "_main_":
    alarm_clock()