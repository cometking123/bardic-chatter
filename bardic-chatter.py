import time
import keyboard
# To do
# Set up exit to type (exit)
# Set up listener for click (])
proceed_key = ']'  # proceed to o
exit_key = 'ctrl+space'  # escape to stop program
story_loop = True


def stop_story():
    global story_loop
    story_loop = False
    keyboard.press_and_release(proceed_key)
    print("Story will terminate after this line \n")


keyboard.add_hotkey(exit_key, stop_story)

while story_loop:
    talename = input("What story would you like to play?")

    print(f"To proceed, press {proceed_key}")
    print(f"To exit, press {exit_key}")

    if not story_loop:
        break

    with open(f"poems/{talename}.txt", "r") as file:
        for line in file:
            if not story_loop:
                break
            keyboard.wait(proceed_key)

            if not story_loop:
                break

            # Press t
            keyboard.press_and_release('t')

            keyboard.write(line)

            if story_loop is False:
                break

            time.sleep(0.6)
keyboard.unhook_all_hotkeys()
print("\nProgram terminated.")
