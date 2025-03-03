import os
os.system("cd ~")
os.system("sudo apt-get update")
os.system("sudo apt-get upgrade -y")
os.system("sudo apt install steamlink -y")
choiceloop = 1
while choiceloop == 1:
    print("do you want to pair a bluetooth device")
    print("(1) Yes")    
    print("(2) No")
    choice = input(">>>")
    if choice == "1":
        print("plug in a mouse and pair your bluetooth device using the UI")
        input("once finished press enter")
    elif choice == "2":
        choiceloop = 0
    else:
        print("invalid choice")
os.system("cd ~")
os.system("git clone https://github.com/Botspot/autostar")
os.system("~/autostar/main.sh setup")
os.system("mkdir ~/.config/autostart")
os.system("cp ~/Wireless-Deck-to-TV/autorun.desktop ~/.config/autostart")
print("installing steam link exit with ctrl + C once finished")
os.system("steamlink")
choiceloop = 0
while choiceloop == 0:
    print("Do you have a 4k tv")
    print("(1) yes")
    print("(2) No")
    choice = input(">>>")
    if choice == "1":
        print("having the display resolution that high causes issues turn down the display resolution now using a mouse and the ui")
        choiceloop = 1
    elif choice == "2":
        choiceloop = 1
    else:
        print("invalid choice")