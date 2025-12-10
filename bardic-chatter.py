import time
import keyboard
# To do
# Set up exit to type (exit)
# Set up listener for click (])
proceed_key = ']'  # proceed to o
exit_key = 'ctrl+space'  # escape to stop program
story_loop = True

while story_loop:
    talename = input("What story would you like to play?")

    print(f"To proceed, press {proceed_key}")
    print(f"To exit, press {exit_key}")

    with open(f"poems/{talename}.txt", "r") as file:
        for line in file:
            keyboard.wait(proceed_key)

            if keyboard.is_pressed(exit_key):
                story_loop = False
                break
            # Press t
            keyboard.press_and_release('t')

            keyboard.write(line)

            time.sleep(0.6)
