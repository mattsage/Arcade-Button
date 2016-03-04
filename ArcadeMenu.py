from gpiozero import Button
import os

button = Button(17)
button2 = Button(18)
button3 = Button(27)

while True:
        if button.is_pressed:
                os.system("echo emulationstation")
                #os.system("emulationstation")
                #exit()

        if button2.is_pressed:
                os.system("echo startx")
                #os.system("startx")
                #exit()
                
        if button3.is_pressed:
                os.system("echo poweroff")
                #os.system("poweroff")
                #exit()

#Need another button for Exit game?
