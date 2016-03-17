from gpiozero import Button
from termcolor import colored
import os

button = Button(3)
button2 = Button(5)
button3 = Button(27)

print colored(' _______  _______  _______  _______    _______  _______  _______  _______  ______   _______  ', 'red')
print colored('(  ____ \(  ___  )(  ____ \(  ____ \  (  ___  )(  ____ )(  ____ \(  ___  )(  __  \ (  ____ \ ', 'red')
print colored('| (    \/| (   ) || (    \/| (    \/  | (   ) || (    )|| (    \/| (   ) || (  \  )| (    \/ ', 'red')
print colored('| (_____ | (___) || |      | (__      | (___) || (____)|| |      | (___) || |   ) || (__     ', 'red')
print colored('(_____  )|  ___  || | ____ |  __)     |  ___  ||     __)| |      |  ___  || |   | ||  __)    ', 'red')
print colored('      ) || (   ) || | \_  )| (        | (   ) || (\ (   | |      | (   ) || |   ) || (       ', 'red')
print colored('/\____) || )   ( || (___) || (____/\  | )   ( || ) \ \__| (____/\| )   ( || (__/  )| (____/\ ', 'red')
print colored('\_______)|/     \|(_______)(_______/  |/     \||/   \__/(_______/|/     \|(______/ (_______/ ', 'red')
print (" ")
print ("Please Choose a Button")
print ("1) Arcade")
print ("2) Desktop")
print ("3) Power Off")

while True:
        if button.is_pressed:
                #os.system("echo emulationstation")
                os.system("emulationstation")
                exit()

        if button2.is_pressed:
                #os.system("echo startx")
                os.system("startx")
                exit()
                
        if button3.is_pressed:
                #os.system("echo poweroff")
                os.system("sudo poweroff")
                exit()

#Need another button for Exit game?
