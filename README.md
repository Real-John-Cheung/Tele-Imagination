# Tele-Imagnation
by [JohnC](https://johncheung.art) and Flynn

## Dev Instructions for python scripts
You will need to have `python3`, `pip` and `pipenv` for development

under `./pyScripts` create a new terminal and run `pipenv install` to create a virtual env and install dependencies from Pipfile

when installing packages for the project, use `pipenv install <package_name>`

use `pipenv run <command>` to run sth inside the virtual env

after installing packages, run `pipenv run pip freeze -> requirements.txt` to generate requirements.txt

## Instructions for testing
1. programming ESP32CAM: 

    -1. get the newest ESP hardware library for arduino IDE, visit [this page](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#windows-manual-installation)

    -2. get the esp32cam wrapper by yoursunny visit [this page](https://github.com/yoursunny/esp32cam)

    -3. connect the FTDI interface to the ESP32cam, for instruction, visit [this page](https://randomnerdtutorials.com/program-upload-code-esp32-cam/) Remember to connect GIO0 pin and GND pin while programming the ESP32cam board, use a [jumper](https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Fparts%2F2%2F4%2F0%2F7%2F09044-02-L.jpg&imgrefurl=https%3A%2F%2Fwww.sparkfun.com%2Fproducts%2F9044&tbnid=VswzLEwkGLUwcM&vet=12ahUKEwie2KWsu_D2AhVJXJQKHTKSCsQQMygAegUIARC-AQ..i&docid=970qvGPxp6UYVM&w=600&h=600&q=pin%20jumper&client=firefox-b-d&ved=2ahUKEwie2KWsu_D2AhVJXJQKHTKSCsQQMygAegUIARC-AQ) for that

    -4. in arduinoCode.ino, find `WIFI_SSID` and `WIFI_PASS`, change them to match your WiFi. If there is no router, use your computer to create a hotspot.

    -5. after uploading the code, keep the serial monitor on so you can find the local ip address of the ESP32cam board

2. Python scripts: in `imgFunctions.py`, change the `ip` variable accordingly, then start a virtural environment, install dependencies and run `main.py` (maybe I should make a shell scripts for that later)