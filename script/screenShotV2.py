import win32gui
import sys


from PyQt5.QtWidgets import QApplication


hwnd_title = {}

keyword = " | Microsoft Teams"
name = "SDM"


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def getHandle():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if keyword in t and name in t:
            #print(h, t)
            # win32gui.SetForegroundWindow(h)
            return h


def getScreenShot():
    handle = getHandle()
    print(handle)

    # app = QApplication(sys.argv)
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(handle).toImage()
    # img.save("screenshot.jpg")
getScreenShot()
