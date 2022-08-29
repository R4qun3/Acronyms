from datetime import datetime   
from playsound import playsound #This allows audio to be played

#You could maybe edit this to not include the seconds (who gives a shit about seconds?)
alarm_time = input("Enter the time of alarm to be set (12hr time): 08:30:00:PM/AM\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")

while True:
	#Gather the current time into seperate variables
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    #Check that the alarm time matches up with the actual time
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                	#Bingo!
                    print("Wake Up!")
                    playsound("C:/Add/Your/Audio/File.mp3")
                    #Kill it
                    break