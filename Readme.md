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

Config file content:
```ini
[DEFAULT]

GH_TOKEN = YOUR_GITHUB_TOKEN

URL = CFD_ONLINE_JOBS_URL
```

### 1. GitHub statistics
Firstly, copy config file:
```sh
cp config.ini.example config.ini
```

Go to [github token settings](https://github.com/settings/tokens) and generate a new personal token. Put it to  `YOUR_GITHUB_TOKEN`.

### 2. CFD Job monitor
If you are a CFD engineer student who is seeking for a PhD scolarship, a Post-Doc position or an industry job, this DesktopPi provides a small screen showing the latest
job posted on [cfd-online](https://www.cfd-online.com/Jobs/listjobs.php).  
Choose one of the following jobs' url and put it to `CFD_ONLINE_JOBS_URL`:
- https://www.cfd-online.com/Jobs/listjobs.php?category=Job%20in%20Industry
- https://www.cfd-online.com/Jobs/listjobs.php?category=Job%20in%20Academia
- https://www.cfd-online.com/Jobs/listjobs.php?category=Contract%20Work
- https://www.cfd-online.com/Jobs/listjobs.php?category=PostDoc%20Position
- https://www.cfd-online.com/Jobs/listjobs.php?category=PhD%20Studentship
- https://www.cfd-online.com/Jobs/listjobs.php?category=Internship

## Set Raspberry Pi menu bar to `autohide`
`Right click menu bar` -> `Panel Settings` -> `Advanced` -> Check `Minimize panel when not in use`.

## Run
```sh
python desktopPi.py
```

## Demo
![May-06-20:13-36](https://user-images.githubusercontent.com/7792396/236623411-91aac2ff-78cb-44dd-8530-1f960a6cef1e.png)

## Acknowledgement
The CPU/RAM's UI design and PyQt code are adapted from [earthinversion/SystemMonitorApp](https://github.com/earthinversion/SystemMonitorApp.git) (MIT License).  

Thermo icon was taken from [xiaoyou-bilibili/pi_tool](https://github.com/xiaoyou-bilibili/pi_tool.git).  

Others used [Alibaba Iconfont](https://www.iconfont.cn/).

