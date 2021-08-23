import os
import pyautogui
def screenshot() :
    save_path = os.path.join(os.path.expanduser("~"),"pictures")
    shot = pyautogui.screenshot()
    shot.save(f"{save_path}\\screenshot.png")
    return print(f"\nScreenshot taken, and saved to{save_path}")


screenshot()