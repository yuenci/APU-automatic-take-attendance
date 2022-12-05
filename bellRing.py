from playsound import playsound
import config


status = False


def playBell():
    try:
        for i in range(config.belltimes):
            playsound("./music.mp3")
        status = True
    except:
        pass
        # do nothing
