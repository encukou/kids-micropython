#! /bin/bash -exu

# Flash all the software onto a NodeMCU devkit board

esptool --port /dev/ttyUSB0 erase_flash
esptool --port /dev/ttyUSB0 write_flash 0 esp8266-20170612-v1.9.1.bin --flash_mode dio
sleep 3
ampy -p /dev/ttyUSB0 put boot.py
sleep 1
ampy -p /dev/ttyUSB0 reset
