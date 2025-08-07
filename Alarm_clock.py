
import datetime
import time
import winsound

def set_alarm(alarm_time, sound_duration=1000, frequency=2500):
    print(f"Alarm set for {alarm_time}")
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            winsound.Beep(frequency, sound_duration)
            break

alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
