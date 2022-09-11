# Pico Solar System

A miniature device depicting the relative position of the planets in Solar System.

![pico](docs/pico.jpeg)

### Hardware
* Raspberry Pi Pico and time source
  * Pico + Precision RTC Module (DS3231)
  * OR Pico W + available Wi-Fi network
* Pico Display Pack


### Software
#### MicroPython
The software is written in MicroPython 1.19 and uses a custom build from Pimoroni which includes drivers for the display.
Download it from the official Pimoroni repository [here](https://github.com/pimoroni/pimoroni-pico/releases/tag/1.19.7). 
Please note that Pico and Pico W require different UF2 files. Here is a direct link for [Pico](https://github.com/pimoroni/pimoroni-pico/releases/download/1.19.7/pimoroni-pico-1.19.7-micropython.uf2) 
and for [Pico W](https://github.com/pimoroni/pimoroni-pico/releases/download/1.19.7/pimoroni-picow-1.19.7-micropython.uf2)


1. Download the MicroPython UF2.
2. Push and hold the BOOTSEL button and plug your Pico into the USB port of your computer. Release the BOOTSEL button after your Pico is connected.
3. It will mount as a Mass Storage Device called RPI-RP2.
4. Drag and drop the MicroPython UF2 file onto the RPI-RP2 volume. 

#### rshell
To upload and configure your Pico Solar System you will need to install rshell. Make sure you have _pip_ installed.
```
pip3 install rshell
```

#### Installing Pico Solar System
1. Download Pico Solar System
```
git clone https://github.com/dr-mod/pico-solar-system.git
```
2. Open the directory with the source code
```
cd pico-solar-system
```
3. (If using Wi-Fi), rename wifi_config_sample.py to wifi_config.py and edit to include your Wi-Fi information

4. Copy required python files to your pico
```
rshell
cp *.py /pyboard/
```
5. (If using RTC) Set time & configure the RTC module 
```
repl

import time
import ds3231
rtc = ds3231.ds3231()
rtc.set_time(time.time())
```
To account for a timezone you might want to apply an offset to the UTC timestamp in seconds:
```
rtc.set_time(time.time() + 60 * 60 * (+ OFFSET_IN_HOURS) )
```

### Case 
A 3d printable case for this project can be found [here](https://www.printables.com/model/237722-raspberry-pi-pico-rtc-display-case).

A remixed case for the Pico W and display (without the RTC) can be found [here](https://www.printables.com/model/261540).

### Support the project
If you would like to support what I do and keep me caffeinated, you can do it here:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/drmod)
