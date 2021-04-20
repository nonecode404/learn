import os
import time

adb1 = 'adb shell input keyevent 106'
for i in range(100):
    os.popen(adb1)
    time.sleep(2)
    os.popen(adb1)
    time.sleep(2)