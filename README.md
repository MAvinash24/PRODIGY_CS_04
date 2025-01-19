# PRODIGY_CS_04

## Keylogger for Educational Purposes

This is a simple keylogger implemented in Python using the `pynput` library. It records keypress events and stores them in a log file for educational purposes only. The program writes logs with timestamps for each key pressed.

### Features

- **Logs Keystrokes**: The keylogger records every keypress event, including special keys like space, enter, tab, and others. Each keystroke is logged with a timestamp indicating when the key was pressed.

- **Esc Key to Stop**: The program runs in the background and listens for keypress events. Pressing the `Esc` key will stop the keylogger and exit the program, ensuring the user has control over when the logging stops.

- **Log File Location**: The keylogger creates a folder named `.keylogger_logs` inside the user's **Documents** directory (if it doesn't already exist). The logs are stored in a file called `keylog.txt` inside this folder. This way, the logged keystrokes are saved safely and in an organized manner.

  - **Log Path**: 
    ```
    <Your Home Directory>/Documents/.keylogger_logs/keylog.txt
    ```
  - The directory and the log file are created automatically when the script is run, making the process seamless for the user.


### Requirements

To run this project, you'll need to install the `pynput` library. You can install it using pip:

```bash
pip install pynput
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MAvinash24/PRODIGY_CS_04.git
```

2.Navigate to project directory:
```bash
cd PRODIGY_CS_04
```

3. Run the code:
```bash
python keylogger.py
```






