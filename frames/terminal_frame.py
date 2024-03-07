# os: This is a built-in Python module that provides a portable way of using operating system dependent functionality.
# It allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.
import os
# pty: This is a Python library for creating and using Unix pseudo-terminals.
# Pseudo-terminals are pairs of virtual devices that provide an interface emulating a terminal.
import pty
# subprocess: This is a Python module used to spawn new processes, connect to their input/output/error pipes,
# and obtain their return codes. It allows you to spawn new processes and manage their input/output streams.
import subprocess
# threading: This is a built-in Python module used to create, control and manage threads.
# A thread is a separate flow of execution. This means that your program will have two things happening at once.
import threading
# pyte: This is a Python library that provides a simple VTXXX-compatible terminal emulator.
# VTXXX is a series of video terminals made by Digital Equipment Corporation. Pyte emulates these terminals and
# allows you to create and manage virtual screens of any size.
from pyte import Screen, Stream

import customtkinter


class EmbeddedShell(customtkinter.CTkFrame):
    def __init__(self, master, ispythonshell: bool = False, **kwargs):
        # Call the parent class's constructor
        # 'master' is the parent widget.
        super().__init__(master, **kwargs)

        # Set the foreground color to transparent
        self.configure(fg_color="transparent")

        # This attribute will determine if the terminal should start as a Python shell.
        self.ispythonshell = ispythonshell

        # Create a Text widget for the terminal output
        self.text = customtkinter.CTkTextbox(self, state='disabled')
        self.text.pack(fill='both', expand=True)

        # Create an Entry widget for the user input
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Type your command here and press Enter. Some commands may take a few seconds to execute or show output.")
        self.entry.pack(fill='x', pady=(10, 0))
        # Bind the send_input method to the Return event
        # When the user presses Enter, the send_input method will be called.
        self.entry.bind('<Return>', self.send_input)

        # Create a Screen and a Stream for the terminal
        # The Screen is a 2D array that holds the characters displayed on the terminal.
        # The Stream is a state machine that processes the terminal output and updates the Screen.
        self.screen = Screen(500, 300)
        self.stream = Stream()
        # Attach the Screen to the Stream.
        # This means that when the Stream processes the terminal output, it will update the Screen.
        self.stream.attach(self.screen)

        # Start the terminal
        # If ispythonshell is True, the terminal will start with a Python shell.
        self.start_terminal(ispythonshell)

    def start_terminal(self, event):
        # Open a new pseudo terminal
        # pty.openpty() returns a pair of file descriptors (master, slave) for the pty and the tty respectively.
        self.master_fd, slave_fd = pty.openpty()

        # Start a new process for the terminal
        # subprocess.Popen is used to run a command in a new process. Here, it's used to run the '/bin/bash' command, which starts a new bash shell.
        # preexec_fn=os.setsid is used to make the process run in a new session.
        # stdin, stdout, and stderr are set to slave_fd, which means the input and output of the process are connected to the tty.
        # universal_newlines=True is used to make the process use universal newline mode, which treats all newline characters the same.
        self.process = subprocess.Popen(['/bin/bash'], preexec_fn=os.setsid,
                                        stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, universal_newlines=True)

        # Start a new thread to read the terminal output
        # threading.Thread is used to create a new thread. target=self.read_output means the thread will run the read_output method.
        # daemon=True means the thread is a daemon thread, which means it will exit when the main program exits.
        threading.Thread(target=self.read_output, daemon=True).start()

        # If ispythonshell is True, send the 'clear && python3' command to the terminal
        # This clears the terminal and starts a new Python shell.
        # os.write is used to write the command to the pty. The command is encoded to bytes because os.write expects bytes, not a string.
        if self.ispythonshell is not False:
            command = 'clear && python3'
            os.write(self.master_fd, command.encode() + b'\n')
        else:
            command = 'clear'
            os.write(self.master_fd, command.encode() + b'\n')

    def read_output(self):
        # This method is run in a separate thread and continuously reads the terminal output.
        while True:
            try:
                # Read up to 1024 bytes from the pty.
                # os.read is used to read from a file descriptor. self.master_fd is the file descriptor of the pty.
                # The output is decoded from bytes to a string.
                output = os.read(self.master_fd, 1024).decode()
            except OSError:
                # If an OSError is raised, ignore it and continue with the next iteration of the loop.
                # This is used to handle errors caused by reading from a non-blocking file descriptor.
                continue

            if output:
                # If there is any output, process it.

                # Feed the output to the Stream.
                # The Stream will process the output and update the Screen.
                self.stream.feed(output)

                # Get the lines from the Screen.
                # The Screen is a 2D array that holds the characters displayed on the terminal.
                # The display attribute of the Screen is a list of lines, where each line is a list of cells.
                # The rstrip method is used to remove trailing whitespace from each line.
                lines = [line.rstrip() for line in self.screen.display]

                # Join the lines into a single string, separated by newline characters.
                # Then, remove trailing newline characters from the output and add a space at the end.
                new_output = '\n'.join(lines).strip('\n') + ' '

                # If the new output is different from the current output in the Text widget, update the Text widget.
                # The get method of the Text widget is used to get the current output.
                # The '1.0' argument means to start at line 1, character 0.
                # The 'end-1c' argument means to end at the last character.
                if new_output.strip() != self.text.get('1.0', 'end-1c').strip():
                    self.text.configure(state='normal')

                    # Delete the current output in the Text widget
                    self.text.delete('1.0', 'end')

                    # Insert the new output into the Text widget
                    self.text.insert('end', new_output)

                    # Scroll to the end of the Text widget so the most recent output is visible.
                    self.text.see('end')

                    self.text.configure(state='disabled')

            # If the process has ended, break the loop.
            # The poll method of the Popen object is used to check if the process has ended.
            # If the process has ended, poll will return the exit code. Otherwise, it will return None.
            if output == '' and self.process.poll() is not None:
                break

    def send_input(self, event):
        # This method is called when the user presses Enter in the Entry widget.

        # Get the user's input
        input = self.entry.get()

        # Clear the Entry widget
        self.entry.delete(0, 'end')

        # If the user's input is not empty, send it to the terminal.
        if input:
            # os.write is used to write the command to the pty. The command is encoded to bytes because os.write expects bytes, not a string.
            # The b'\n' at the end is a newline character, which is equivalent to pressing Enter in the terminal.
            os.write(self.master_fd, input.encode() + b'\n')
        else:
            # If the user's input is empty, send a newline character to the terminal.
            # This is equivalent to pressing Enter in the terminal without typing anything.
            os.write(self.master_fd, b'\n')

        # Prevent the default behavior of the Return event.
        # This is used to prevent the Entry widget from inserting a newline character into the text when Enter is pressed.
        # The 'break' string is a special return value that stops other bindings for this event from being executed.
        return 'break'
