# 2022/11/30 20:02:25  zt

import time
import configparser
import qrcode
import os

class dailyCheck():
    def __init__(self):

        cfg = configparser.ConfigParser()
        cfgPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep+ "config.ini"
        cfg.read(cfgPath)

        self.fname = cfg['DEFAULT']['DC_FULL_PATH']
        self.url = cfg['DEFAULT']['URL']
        self.imgPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "QRCode.png"
        
    def checkDC(self):
        '''Check Covid daily check script status
        '''

        line = ''

        with open(self.fname,"r") as f:
            # Get last line
            line = f.readlines()[-1]
        
        today = time.strftime("%Y%m%d", time.localtime())+"\n"

        if (line == today):
            return True
        else:
            return False

    def genCovidQRCode(self):
        '''Generate QR code according to the url
        '''
        urlText = self.url+time.strftime("%Y%m%d", time.localtime())
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(textcontent)

        qr.make(fit=True)

        img = qr.make_image()

        img.save(self.imgPath)

        return   
