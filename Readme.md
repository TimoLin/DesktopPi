DesktopPi
========
A PyQt5 based GUI program to show some interesting information on the Raspberry Pi with a 3.5inch GPIO screen.

## Prerequisites
Hardware:  
`Raspberry Pi 3B` and `a 3.5 inch GPIO screen`

Environment:
```
sudo apt install python3-pyqt5
pip install -r requirements.txt
```

## Configuration
Firstly, copy config file:
```sh
cp config.ini.example config.ini
```

Go to [github token settings](https://github.com/settings/tokens) and generate a new personal token. Put it to  `YOUR_GITHUB_TOKEN`.

Config file content:
```ini
[DEFAULT]

GH_TOKEN = YOUR_GITHUB_TOKEN

DC_FULL_PATH = DAILY_CHECK_LOG_FILE_PATH

URL = URL_TO_BE_CONVERTED
```

## Set Raspberry Pi menu bar to `autohide`
`Right click menu bar` -> `Panel Settings` -> `Advanced` -> Check `Minimize panel when not in use`.

## Run
```sh
python desktopPi.py
```

## Demo
![Selection_002](https://user-images.githubusercontent.com/7792396/204963215-f64dc6c8-2680-4a54-a94b-a0fcef4c4c2b.png)

## Acknowledgement
The CPU/RAM's UI design and PyQt code are adapted from [earthinversion/SystemMonitorApp](https://github.com/earthinversion/SystemMonitorApp.git) (MIT License).  

Thermo icon was taken from [xiaoyou-bilibili/pi_tool](https://github.com/xiaoyou-bilibili/pi_tool.git).  

Others used [Alibaba Iconfont](https://www.iconfont.cn/).

