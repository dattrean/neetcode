import pyautogui
import time

start_time = time.time()

pyautogui.click(134, 860)
time.sleep(2)
pyautogui.click(810, 260)
pyautogui.moveTo(-20, -20, duration=0)
time.sleep(3.0)



pyautogui.keyDown("command")
pyautogui.press("enter")
pyautogui.keyUp("command")

end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
