import time
import pyautogui

import os

dir_fd = os.open('./poems', os.O_RDONLY)

print("bardic-chatter: The only way to recite good tales")
print("")
print("To use this, select the poem name, and use the ']' key to progress through each line.")
print("Make sure you're tabbed into Minecraft, LOTC server!")

# To do
# Set up exit to type (exit)
# Set up function to pull data from poems/"talename".txt
# Set up listener for click (])
# 
time.clock_gettime
pyautogui.click()
talename = input("What story would you like to play?")

