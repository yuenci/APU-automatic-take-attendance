import time
import script.screenShot as screenShot
import script.qrscan as qrscan
import script.config as config
import script.bellRing as bellRing
import sys


if config.mode != "bell" and config.mode != "auto":
    print("Error: mode must be 'bell' or 'auto'.")
    exit()


if config.mode == "auto":
    import script.seleniumWD as seleniumWD


with open("./account.txt") as f:
    account = f.readlines()
    account = [x.split(",") for x in account]

no = 0

while True:
    if no > config.duration:
        break

    screenShot.window_capture(config.pictureName)
    code = qrscan.scan(config.pictureName)
    if code:
        print("code: ", code)
        if config.mode == "auto":
            seleniumWD.main(account[no][0], account[no][1].strip(), code)
        elif(config.mode == "bell"):
            if bellRing.status == False:
                bellRing.showCode(code)
                bellRing.playBell()
            else:
                sys.exit()
        else:
            raise Exception("mode error")
        no += 1
    else:
        if config.log:
            print(
                f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}: No QR code found.")
    time.sleep(config.interval)

print("Done.")
