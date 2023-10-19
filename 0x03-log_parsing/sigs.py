import signal
import time

# define a signal handler fucntion
def handle_signal(signum, frame):
    print(f"Received signal: {signum}")


# register the signal handler for SIGINT(CTRL + c)
signal.signal(signal.SIGINT, handle_signal)


# Register the signal handler for SIGTERM
signal.signal(signal.SIGTERM, handle_signal)


print("Signal handling example. Press CTRL + c to send SIGINT or use 'kill -15 <pid>' to send SIGTERM.")

while True:
    print("Waiting...")
    time.sleep(2)

