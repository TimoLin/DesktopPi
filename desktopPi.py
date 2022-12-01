# 2022/11/29 21:22:27  zt
# Raspberry Pi Desktop toy

import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal,Qt
from winUI import Ui_Form

import psutil
import time

from githubStatistic import *
from dailyCheck import *

class guiForm(QtWidgets.QWidget, Ui_Form):
    
    def __init__(self,parent=None):
        super(guiForm,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|self.windowFlags())

        # Update clock
        self.timer_clock = QtCore.QTimer()
        self.timer_clock.timeout.connect(self.updateClock)
        self.timer_clock.start(1000)

        # Update CPU/Ram infomation every 1000 ms
        self.timer_systemStat = QtCore.QTimer()
        self.timer_systemStat.timeout.connect(self.getSystemStat)
        self.timer_systemStat.start(2000)

        # Update github status
        self.gh = ghStats()
        self.updateGH()
        self.timer_ghStat = QtCore.QTimer()
        self.timer_ghStat.timeout.connect(self.updateGH)
        self.timer_ghStat.start(10*3600*1000)

        # Update daily check status
        self.dc = dailyCheck()
        self.updateDailyCheck()
        self.timer_dc = QtCore.QTimer()
        self.timer_dc.timeout.connect(self.updateDailyCheck)
        self.timer_dc.start(2*3600*1000)

    def mousePressEvent(self, evt):
        '''Re-write mouse press event
        '''
        # Get mouse location
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()

        # Get current window form location
        self.origin_x = self.x()
        self.origin_y = self.y()


    def mouseMoveEvent(self, evt):
        '''Re-write mouse movement event
        '''
        # Calculate mouse movement dX, dY
        move_x = evt.globalX() - self.mouse_x
        move_y = evt.globalY() - self.mouse_y
    
        # Calculate window form new loation
        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y
    
        # Move window form to new location
        self.move(dest_x, dest_y)   

    def updateClock(self):
        '''Show current time
        '''
        curTime = QtCore.QTime.currentTime()
        timeLabel  =curTime.toString('hh:mm:ss')
        self.curTime.display(timeLabel)

    def getSystemStat(self):
        '''Get system CPU/RAM usage using psutil
        Adapted from https://github.com/earthinversion/SystemMonitorApp.git (MIT License)
        '''
        keys = list(psutil.sensors_temperatures().keys())
        cpuTemperature = psutil.sensors_temperatures()[keys[0]][0].current
        cpuPercent = psutil.cpu_percent()
        ramPercent = psutil.virtual_memory().percent
    
        self.setValue(cpuPercent,self.labelProgCPU,self.progCPU,"rgba(85, 170, 255, 255)")
        self.setValue(ramPercent,self.labelProgRam,self.progRam,"rgba(255, 0, 127, 255)")
        self.cpuTemp.setText(str(cpuTemperature))
        time.sleep(1)
    
    def setValue(self, value, labelPercentage, progressBarName, color):
        '''Set CPU/Ram usage value
        Adapted from https://github.com/earthinversion/SystemMonitorApp.git (MIT License)
        '''
    
        sliderValue = value
    
        # Html text percentage
        htmlText = """<p align="center"><span style=" font-size:12pt;">{VALUE}</span><span style=" font-size:10pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace(
            "{VALUE}", f"{sliderValue:.1f}"))
    
        # Call def progressbarvalue
        self.progressBarValue(sliderValue, progressBarName, color)
    
    def progressBarValue(self, value, widget, color):
        '''Set CPU/Ram usage circular progress value
        Adapted from https://github.com/earthinversion/SystemMonitorApp.git (MIT License)
        '''
    
        # Progressbar stylesheet base
        styleSheet = """
        QFrame{
        	border-radius: 37px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
    
        # Get progress bar value, convert to float and invert values
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0
    
        # Get new values
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
    
        # Fix max value
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
    
        # Set values to new stylesheet
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2).replace("{COLOR}", color)
    
        # Apply stylesheet with new values
        widget.setStyleSheet(newStylesheet)

    def updateGH(self):
        '''Update Github statistic labels
        '''

        [totStars,totlCommits, totPrs, totIssues, totRepos] = self.gh.ghGetStat()
        #print(totRepos,totlCommits,totPrs,totIssues,totRepos)

        self.ghStars.setText(str(totStars))
        self.ghCommits.setText(str(totlCommits))
        self.ghPrs.setText(str(totPrs))
        self.ghIssues.setText(str(totIssues))
        self.ghRepos.setText(str(totRepos))

        return

    def updateDailyCheck(self):
        '''Update Covid Daily Check status
        '''
        if ( self.dc.checkDC() ):
            self.dailyCheckStatus.setText("Success!")
            self.dailyCheckStatus.setStyleSheet("background-color: rgb(78, 154, 6); color: white;")
        else:
            self.dailyCheckStatus.setText("Failed!")
            self.dailyCheckStatus.setStyleSheet("background-color: rgb(239, 41, 41); color: white;")

    def callGenQRCode(self):
        '''Call QR Code generator
        '''

        # Todo

        return


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    window = guiForm()
    window.show()
    sys.exit(app.exec_())
