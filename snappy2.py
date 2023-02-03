#! python3
import pyautogui, sys
import time

# pyautogui.MINIMUM_DURATION = 0 # Defult duration
pyautogui.MINIMUM_DURATION = 0.01

print('Press Ctrl-C to quit.')

try:
	for i in range(3):
		pyautogui.moveTo(1318, 823)
		pyautogui.click(button='left')
		pyautogui.moveTo(1318, 823)
		pyautogui.click(button='left')
		pyautogui.moveTo(1252, 623)
		pyautogui.click(button='left')
		pyautogui.moveTo(1295, 836)
		pyautogui.click(button='left')
except KeyboardInterrupt:
	print('\n')
	sys.exit()