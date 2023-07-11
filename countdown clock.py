import time

def countdown(seconds):
    while seconds > 0:
        print(f"Countdown: {seconds} seconds")
        time.sleep(1)
        seconds -= 1

    print("Countdown finished!")

# Set the desired countdown duration in seconds
duration = 10

# Start the countdown
countdown(duration)
