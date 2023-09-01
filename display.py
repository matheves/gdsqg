import pyautogui
import random
import time

while True:
    # Generate a random period of time between 20 seconds and 2 minutes
    random_period = random.uniform(20, 120)
    pyautogui.click()
    time.sleep(random_period)

    # Generate a random distance to move the mouse cursor
    move_distance = random.randint(10, 50)

    # Generate a random direction to move the mouse cursor in
    direction = random.choice(['up', 'down', 'left', 'right'])

    # Move the mouse cursor in the random direction and distance
    if direction == 'up':
        pyautogui.move(0, -move_distance, duration=1)
    elif direction == 'down':
        pyautogui.move(0, move_distance, duration=1)
    elif direction == 'left':
        pyautogui.move(-move_distance, 0, duration=1)
    elif direction == 'right':
        pyautogui.move(move_distance, 0, duration=1)
