import schedule
import time
from playsound import playsound

# Find the sound
def beep():
    playsound('beep.wav')
    print("welcome!")

def hello():
    print(input("tap 'ok' to sound beep: "))

schedule.every(2).minutes.do(hello)

# Schedule the time (every two minutes)
schedule.every(2).minutes.do(beep)

# Loop the hole thing
while True:
    schedule.run_pending()
    time.sleep(1)
