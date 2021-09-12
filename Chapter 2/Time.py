import time
totalSeconds = int(time.time())
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute =  totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24 + 2
print(f"Current time is {currentHour}:{currentMinute}:{currentSecond} CET")
