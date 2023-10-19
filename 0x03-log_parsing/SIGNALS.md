```python
import signal
import time

# Define a signal handler function
def handle_signal(signum, frame):
    print(f"Received signal {signum}")

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, handle_signal)

# Register the signal handler for SIGTERM
signal.signal(signal.SIGTERM, handle_signal)

print("Signal handling example. Press CTRL + C to send SIGINT or use 'kill -15 <pid>' to send SIGTERM.")

while True:
    print("Running...")
    time.sleep(1)
```
# explanation

We import the signal module to work with signals.

We define a function handle_signal that will be called when a signal is received. It simply prints the signal number.

We register handle_signal to handle the SIGINT signal (CTRL + C) using signal.signal(signal.SIGINT, handle_signal). You can also register other signals in a similar way.

We create a simple loop to keep the program running and print "Running..." every second.

The program will run indefinitely until you send a signal.

To test it:

Run the script in a terminal.

To send a SIGINT signal (CTRL + C), press CTRL + C, and you'll see the message "Received signal 2".

To send a SIGTERM signal, open another terminal and find the process ID (PID) of the running Python script using the ps command. Then use the kill command to send SIGTERM:

```bash
ps aux | grep your_script_name.py
kill -15 PID
```
Replace your_script_name.py with the actual name of your Python script and replace PID with the process ID you obtained from the ps command. You'll see the message "Received signal 15" in the first terminal where your Python script is running.



# a list of most used signals and what they do


Signals in Unix-like operating systems are a way to communicate with processes. Here's a list of some commonly used signals and their purposes:

- SIGINT (Interrupt) - Signal 2:

Purpose: Sent when the user interrupts a running process, typically by pressing CTRL + C. It's used to request that a process terminate gracefully.
- SIGTERM (Terminate) - Signal 15:

Purpose: Sent to request the termination of a process. Unlike SIGKILL, it allows the process to perform cleanup operations before exiting.
- SIGHUP (Hang Up) - Signal 1:

Purpose: Originally used to notify a process that the terminal has been disconnected. Now often used to request a process to reload its configuration.
- SIGKILL (Kill) - Signal 9:

Purpose: Sent to forcefully terminate a process. It doesn't allow the process to clean up or perform any graceful shutdown operations.
- SIGSTOP (Stop) - Signal 19:

Purpose: Pauses a process. It can be resumed later using SIGCONT.
- SIGCONT (Continue) - Signal 18:

Purpose: Resumes a process that was previously stopped using SIGSTOP.
- SIGABRT (Abort) - Signal 6:

Purpose: Sent by the process itself to request its own termination, often used when an unrecoverable error is detected.
- SIGUSR1 and SIGUSR2 (User-Defined Signals 1 and 2):

Purpose: These signals can be used for user-defined purposes in applications. Their behavior is not predefined by the operating system.
- SIGCHLD (Child Status Change):

Purpose: Sent to the parent process when a child process terminates. It's often used for managing child processes.
- SIGPIPE (Pipe):

Purpose: Sent to a process when it attempts to write to a pipe without a reader. It can be used to handle broken pipes in inter-process communication.
- SIGALRM (Alarm):

Purpose: Sent when the timer set by the alarm() function expires. It can be used to set a timeout for certain operations.
- SIGWINCH (Window Change):

Purpose: Sent to a process when the terminal window size changes. This can be used for handling terminal resizing events.
- SIGUSR1 and SIGUSR2 (User-Defined Signals 1 and 2):

Purpose: These signals are available for user-defined purposes. Application developers can use them as needed.