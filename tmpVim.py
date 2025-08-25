#!/usr/bin/env python3
import subprocess
from pynput.keyboard import Key, Controller
import pyperclip
import os

keyboard = Controller()
tempDir = os.path.expanduser('~/tmp')
if not os.path.exists(tempDir):
    os.makedirs(tempDir)

tempAddr = os.path.join(tempDir, 'buffer')

keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release('c')
keyboard.release(Key.ctrl)

clipboard_content = pyperclip.paste()

with open(tempAddr, 'w') as file:
    file.write(clipboard_content)

subprocess.run(["gvim", tempAddr], capture_output=True)
subprocess.run(['xclip', '-selection', 'clipboard', tempAddr])

keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release(Key.ctrl)
keyboard.release('v')

os.remove(tempAddr)
