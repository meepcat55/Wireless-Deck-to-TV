## Requirements
- A Steam Deck or other linux computer
- A raspberry Pi 5 2GB or better (A raspberry pi 4 may work but I have not tested it)
- A spare micro SD card that you are ok with deleting all data on
- Ethernet to your raspberry pi
- A WiFi network that can get at least 100 mbps over the local network
- Some kind of wireless remote controller for the raspberry pi like a wireless mouse, wireless keyboard, some kind of controller, a flipper zero, or anything else with buttons that the Pi can understand I recommend a logitech wireless mouse using a usb receiver 
- A display for the raspberry pi like a TV or monitor
- An internet connection
- Electricity
- The ability to read these instructions
- A snack because this can take a while depending on your internet speed
## Installation 
- make sure you have the SD card you plan on installing to in the micro SD card slot of the steam deck
- On your steam deck press the steam button > Power > Switch to desktop
- Open Konsole
- Paste the command `git clone https://github.com/meepcat55/Wireless-Deck-to-TV.git && cd Wireless-Deck-to-TV && python3 main.py`
- Press A and follow the displayed instructions
- Once the script is completed plug the SD card into your Raspberry pi and power it on
- After a while you should see a steam link screen
- To pair your steam deck make sure its in gaming mode, select the gear in the top left of steamlink and select computers then select your steam deck and pair it
- Now all you need to do is click play and your steam deck will be live streamed to your TV
## Using bluetooth devices to control steamlink
- In konsole on your steam deck with your raspberry Pi powered on and connected to Ethernet run the command ssh steamlink@steamlink.local
- It will have a prompt something something fingerprint just answer yes
- Then type the password steamlink and press enter
- Once you are logged in run the command bluetooth
- [The UI for bluetooth is powered by pythops bluetui ](https://github.com/pythops/bluetui)
- Use the controls listed below to pair your bluetooth device
## 🪄 Usage

### Global

`Tab`: Switch between different sections.

`j` or `Down` : Scroll down.

`k` or `Up`: Scroll up.

`s`: Start/Stop scanning.

`?`: Show help.

`esc`: Dismiss the help pop-up.

`ctrl+c` or `q`: Quit the app.

### Adapters

`p`: Enable/Disable the pairing.

`o`: Power on/off the adapter.

`d`: Enable/Disable the discovery.

### Paired devices

`u`: Unpair the device.

`Space`: Connect/Disconnect the device.

`t`: Trust/Untrust the device.

`e`: Rename the device.

### New devices

`p`: Pair the device.

- Once your device is paired you can exit konsole and return to gaming mode
## Recommended setting changes for Raspberry Pi models
To change settings select the gear in the top right of steam link > Streaming > Customize
- **Raspberry Pi 5**
- Settings are already optimal for visual quality and performance
- **Raspberry Pi 4**
- Change video to balanced
- Change bandwidth limit to 40 Mbps
- **Raspberry Pi 3**
- Currently untested
## Debug info
- The default user is steamlink
- The default password is steamlink
- The default hostname is steamlink
- The image is based off of Raspberry Pi os 64-bit from 2024-11-19
- The rootfs is not resized by default and is 8gb, it can be expanded using raspi-config
- The default raspberry pi os desktop can be accessed by pressing ctrl + C before steamlink initially starts on boot and then running startx
- when a session is started and is a non ssh session /home/steamlink/steamlink.py is run
