# PRODIGY_CS_04

## Keylogger for Educational Purposes

This is a simple keylogger implemented in Python using the `pynput` library. It records keypress events and stores them in a log file for educational purposes only. The program writes logs with timestamps for each key pressed.

---

### Features

- **Logs Keystrokes**: Tracks every key press and records it with a timestamp.

- **Esc Key to Stop**: Press `Esc` to stop the keylogger and exit the program.

- **Log File Location**: Creates a `.keylogger_logs` folder in your **Documents** directory, and stores keystrokes in `keylog.txt`.

  - **Log Path**: 
    ```
    <Your Home Directory>/Documents/.keylogger_logs/keylog.txt
    ```

  - The directory and the log file are created automatically when the script is run, making the process seamless for the user.
  -  Note: After the first run, the keylogger will append new keystrokes to the existing keylog.txt file, continuing from where it left off, instead of overwriting the file.

---

### Requirements

To run this project, you'll need to install the `pynput` library. You can install it using pip:

```bash
pip install pynput
```

---

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
