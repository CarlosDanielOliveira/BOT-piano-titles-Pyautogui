import pyautogui as pa
from time import sleep 
import win32api
import win32con
import keyboard

#https://gameforge.com/en-US/littlegames/magic-piano-tiles/?_gl=1*1p3n8yn*_ga*MTMwODAwNDMuMTczMTk3NDM2Mw..*_ga_37GXT4VGQK*MTczNTI1NTEyMi4zNy4xLjE3MzUyNTUyODQuMC4wLjA.

pa.click(810,557, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('1') == False:

    if pa.pixelMatchesColor(660,446,(0,0,0)):
        click(660,446)

    if pa.pixelMatchesColor(760,446,(0,0,0)):
        click(760,446)

    if pa.pixelMatchesColor(860,446,(0,0,0)):
        click(860,446)

    if pa.pixelMatchesColor(960,446,(0,0,0)):
        click(960,446)




