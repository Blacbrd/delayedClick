import keyboard
import pyautogui
import time

while True:

    # This will check if the "m" key is pressed, as it doesn't do anything on YouTube
    if keyboard.is_pressed("n"):
        time.sleep(1.5)
        pyautogui.click()

    if keyboard.is_pressed("q"):
        print("Exit")
        break

