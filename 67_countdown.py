#! python3
# countdown.py - A simple countdown script.
import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
    print()

# At the end of the countdown, play a sound file.
subprocess.Popen(['open', 'alarm.wav'])

# 在 Windows 上，要确保传入 Popen()的列表中包含'start'，并传入关键字参 数 shell=True。
# 在 OS X 上，传入'open'，而不是'start’，并去掉 shell=True。
