import time
import schedule
from playsound import playsound
import datetime

def audio_5():
    playsound("C:/Users/sec/Desktop/time_5.mp3")

def audio_1():
    playsound("C:/Users/sec/Desktop/time_1.mp3")

schedule.every().day.at("09:55").do(audio_5)
schedule.every().day.at("09:59").do(audio_1)
schedule.every().day.at("10:55").do(audio_5)
schedule.every().day.at("10:59").do(audio_1)
schedule.every().day.at("11:55").do(audio_5)
schedule.every().day.at("11:59").do(audio_1)
schedule.every().day.at("12:55").do(audio_5)
schedule.every().day.at("12:59").do(audio_1)
schedule.every().day.at("13:55").do(audio_5)
schedule.every().day.at("13:59").do(audio_1)
schedule.every().day.at("14:55").do(audio_5)
schedule.every().day.at("14:59").do(audio_1)
schedule.every().day.at("15:55").do(audio_5)
schedule.every().day.at("15:59").do(audio_1)
schedule.every().day.at("16:55").do(audio_5)
schedule.every().day.at("01:33").do(audio_1) 

n_h = 0
while (n_h<17):
    now = datetime.datetime.now()
    n_h = now.hour
    schedule.run_pending()
    time.sleep(1)