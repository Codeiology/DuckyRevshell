# Revshell
A tool built for macOS to create listeners and Duckyscript payloads! Payloads tested with Flipper Zero. Works perfectly.

# Usage
Once you run revshell.py, a user friendly interface will appear and the whole thing will be a breeze. After you have the payload generated, and you made sure that the target is on the same Wi-Fi, and ready to be exploited. Activate the listener, load the payload into the device (in my case qFlipper), execute it on the target, and boom! Reverse shell, complete access to all files and such. A command prompt will not be visible, but if the payloads are delivered correctly, the outputs of the commands you inject should appear.

`git clone https://github.com/Codeiology/Revshell.git`

`cd Revshell`

`python3 revshell.py`
