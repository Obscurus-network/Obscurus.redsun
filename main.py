#settings

#name of the directory that is going to be created
dir_name = 'Redsun'

#drops an easter egg
drop_file = True

#drop file name
file_name = 'README'

#the easter egg file content
file_content = """only in Ohio bruh"""

#URL of the sound that is going to be used, WARNING! THE FILE IS GOING TO BE DOWNLOADED AND NOT STREAMED 
sound_url = 'https://cdn.discordapp.com/attachments/1062049894631755997/1083050003636953149/redsun_incident.wav'

#URL of the background that is going to be used WARNING! THE FILE IS GOING TO BE DOWNLOADED AND NOT STREAMED 
back_url = 'https://media.discordapp.net/attachments/1062049894631755997/1083054264252911678/redsun_incident_back.jpg'

#the sleep time, A.K.A the sleep time/period of inactivity, leave at 0 for no pause
sleep_time = int(0)

import requests
import os
import time 
import ctypes

from playsound import playsound

roaming_dir = os.getenv('AppData')

time.sleep(sleep_time)

os.chdir(roaming_dir)
os.mkdir(f"{dir_name}")
os.chdir(f"{dir_name}")

getback = requests.get(back_url)
open("background.jpg", "wb").write(getback.content)

getsound = requests.get(sound_url)
open("sound.mp3", "wb").write(getsound.content)

if drop_file == True:
    file_write = open(f"{file_name}.md", "x")
    file_write.write(f"{file_content}")
else:
    pass

selfdir = os.getcwd()
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{selfdir}/background.jpg" , 0)


playsound("sound.mp3")

