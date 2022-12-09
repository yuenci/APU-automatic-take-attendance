from PyQt5.QtWidgets import QApplication
import sys
import time
import win32gui
import win32ui
import win32con
import win32api
import os
import script.config as config


def getScreenShot():
    filename = config.pictureName
    # hwnd = 0
    # hwndDC = win32gui.GetWindowDC(hwnd)
    # mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # saveDC = mfcDC.CreateCompatibleDC()
    # saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    # saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # saveDC.SelectObject(saveBitMap)
    # saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    # saveBitMap.SaveBitmapFile(saveDC, filename)
    # get screenshot
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(0).toImage()
    img.save(filename)


hwnd_title = {}


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def getHandle():
    keyword = " | Microsoft Teams"
    name = config.windowName
    if name == "Your course name":
        raise Exception(
            "windowName error, please set the course name in config.py, more details: https://github.com/yuenci/APU-automatic-take-attendance")
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if keyword in t and name in t:
            # win32gui.SetForegroundWindow(h)
            return h


def getWindowShot():
    filename = config.pictureName
    handle = getHandle()
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(handle).toImage()
    img.save(filename)
