import pyautogui
import random
import time
import datetime

import logging                              # --- Add New - Start
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__doc__)
fileHandler = logging.FileHandler("./abc.log")
logger.addHandler(fileHandler)              # --- Add New - End

pyautogui.FAILSAFE = False                  # --- Add New

x = 0
y = 0
while True:
    x = random.randrange(100, 500, 1)
    y = random.randrange(100, 500, 1)
    print(x, y)
    pyautogui.moveTo(y, x)
    pyautogui.click()
    logger.info('Y軸: ' + str(y) + ' ' + 'X軸: ' + str(x))    # --- Add New

    time.sleep(30)
