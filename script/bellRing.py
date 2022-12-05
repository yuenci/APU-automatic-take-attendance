from playsound import playsound
import script.config as config


status = False


def playBell():
    try:
        for i in range(config.belltimes):
            playsound("src/music.mp3")
        status = True
    except:
        pass
        # do nothing
