from playsound import playsound
import script.config as config
from win10toast import ToastNotifier


status = False


def playBell():
    try:
        for i in range(config.belltimes):
            playsound("src/music.mp3")
        status = True
    except:
        pass
        # do nothing


def showCode(code):
    toaster = ToastNotifier()
    toaster.show_toast(
        "Attendance", f"Attendance code: {code}", duration=3)
    # toaster.show_toast(
    #     "Attendance", f"Attendance code: {code}", icon_path="f.ico", duration=10)
