import os
#This is the name of the disk that will be imaged if you are running this on a non steam deck system you need to change this to your sd card
disk = "mmcblk0"
print("__        ___    ____  _   _ ___ _   _  ____ ")
print("\ \      / / \  |  _ \| \ | |_ _| \ | |/ ___|")
print(" \ \ /\ / / _ \ | |_) |  \| || ||  \| | |  _ ")
print("  \ V  V / ___ \|  _ <| |\  || || |\  | |_| |")
print("   \_/\_/_/   \_\_| \_\_| \_|___|_| \_|\____|")
choiceloop = 0
while choiceloop == 0:
    print("THIS WILL OVERWRITE THE SD CARD CURRENTLY INSERTED MEANING ALL DATA WILL BE DELETED")
    print("I AM NOT RESPONSIBLE FOR ANY DATA LOSS THAT CAN OCCUR")
    print("This will NOT install to your steam deck itself and will only overwite the SD card")
    print("Do you wish to procede with the imaging yes/no")
    var = input("")
    if var == "yes" or "Yes":
        choiceloop = 1
    elif var == "no" or "No":
        quit()
    else:
        print("Invalid choice")
choiceloop = 1
while choiceloop == 0:
    print("Have you set a sudo password yes/no")
    var = input("")
    if var == "yes" or "Yes":
        choiceloop = 1
    elif var == "no" or "No":
        print("This is a required step so you must choose a password and enter it now")
        print("Make sure you remember this, write it down somewhere and put it on your fridge")
        print("It will not appear that you are typing anything however you are and it is just not displaying it")
        os.system("passwd")
        choiceloop = 1
    else:
        print("Invalid choice")
os.system("flatpak install flathub org.mozilla.firefox -y")
os.system("flatpak run org.mozilla.firefox")
print("Download the file opened in google drive in firefox to the downloads folder")
os.system("flatpak run org.mozilla.firefox https://drive.google.com/file/d/1B_eYMYBwzQQioxQ9drH0GuSux501-9Qs/view")
input("Press A once download completed")
os.system("7za x ~/Downloads/PiLink.7z")
print("Writing SD card image this may take a while ")
os.system("sudo dd if=PiLink.img of=/dev/" + disk)
print("Imaging complete, you can now remove the sd card and insert it into your Raspberry Pi")
