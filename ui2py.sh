#/bin/bash

pyuic5 -o  winUI.py winUI.ui

pyrcc5 res/icons.qrc -o icons_rc.py
