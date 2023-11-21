import time
from datetime import datetime

def set_alarm(alarm_time):
    # Convert the alarm time from 12-hour format to 24-hour format for comparison
    alarm_time_24 = datetime.strptime(alarm_time, '%I:%M %p').strftime('%H:%M')

    print(f"Alarm set for {alarm_time}")
    while True:
        # Get current time in 24-hour format
        current_time_24 = datetime.now().strftime('%H:%M')

        # Display current time in 12-hour format
        current_time_12 = datetime.now().strftime('%I:%M %p')
        print(f"Current time: {current_time_12}", end="\r", flush=True)

        if current_time_24 == alarm_time_24:
            print("\nWake up!")
            # Here you can add any functionality you want to trigger the alarm
            break

        time.sleep(60)  # Update the time every minute

# Example usage
alarm_time = input("Enter alarm time in HH:MM AM/PM format: ")
set_alarm(alarm_time)