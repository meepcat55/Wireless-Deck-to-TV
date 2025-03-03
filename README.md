## Requirements
- A Steam Deck or really any computer with steam but this guide is made for the steam deck
- A raspberry Pi 5 2GB or better (A raspberry pi 4 may work but I have not tested it)
- A SD card or SSD for your raspberry pi at least 16GB
- Ethernet to your raspberry pi (highly recommended but not essential)
- A WiFi network that can get at least 100 mbps over the local network
- Some kind of wireless remote controller for the raspberry pi like a wireless mouse, wireless keyboard, some kind of controller, a flipper zero, or anything else with buttons that the Pi can understand
- A display for the raspberry pi like a TV or monitor
- An internet connection
- Electricity
- Some kind of ssh client (the steam deck can be used but a keyboard is recommended if a laptop is not an option) [(instructions on ssh basics)](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server)
- The ability to read these instructions
- A snack because this can take a while depending on your internet speed
## Setup
- [Install raspberry pi imager](https://www.raspberrypi.com/software/)
- Plug in your SD card
- Open imager
- Select choose device
- Select your PI
- Select Choose os
- Select Raspberry Pi OS (64-bit)
- Select Choose Storage
- Select your SD card
- Select next
- Select edit settings
- make sure of the following
-  the hostname is raspberrypi.local
- a username and password is set
- ssh is enabled
- then select save
- and then select yes
- Wait for it to finish
- Remove the SD card and put it in your Pi
- Plug your Pi into Ethernet, power, and HDMI 
 in the port closest to the usbc port on your pi
- Wait for it to finish setting up
- Go on your steam deck in desktop mode and open konsole (or on any system with openssh installed)
- type ssh {The username you entered in imager}@raspberrypi.local
- It will have a prompt something something fingerprint just answer yes
- enter the password you entered in imager
- paste this string and press enter `git clone https://github.com/meepcat55/Wireless-Deck-to-TV.git && cd Wireless-Deck-to-TV && python3 main.py `
Once this is finished just pair your steam deck
I reccomend changing some streaming settings for optimal performance
Click the gear in the top right and select streaming settings then customize and change the following
- video beautiful
- bitrate limit 50 MBits/s
- HVEC video enabled
- low latency networking enabled
  
