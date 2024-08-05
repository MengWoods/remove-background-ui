#!/usr/bin/env python3
from UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QPushButton, \
                            QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QTransform, QPixmap, QCursor, QPainter

import sys
import os
from removebg import RemoveBg
from PIL import Image, ImageDraw, ImageFont

# Paste your key at here !
key = ""

'''====================================
1. load pic, 2. parameters,  3. generate.
====================================='''
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        '''ui adjust'''
        self.radioButton.setChecked(True)
        self.view = self.graphicsView
        self.key = key
        self.fpath = os.getcwd()
        '''open pic'''
        self.openButton.clicked.connect(self.loadpic)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.generate)
        '''checkBox'''
        self.transparent_ = 0
        self.red_ = 0
        self.lightblue_ = 0
        self.darkblue_ = 0
        self.white_ = 0
        self.gradientred_ = 0
        self.gradientblue_ = 0
        self.gradientgray_ = 0

        self.checkBox.stateChanged.connect(self.transparent)
        self.checkBox_2.stateChanged.connect(self.red)
        self.checkBox_4.stateChanged.connect(self.lightblue)
        self.checkBox_5.stateChanged.connect(self.darkblue)
        self.checkBox_3.stateChanged.connect(self.white)
        self.checkBox_9.stateChanged.connect(self.gradientred)
        self.checkBox_8.stateChanged.connect(self.gradientblue)
        self.checkBox_10.stateChanged.connect(self.gradientgray)
        '''radio buttons'''
        self.png_ = 0
        self.jpg_ = 0
        self.jpeg_ = 0
        self.bmp_ = 0
        self.radioButton.toggled.connect(self.png)
        self.radioButton_2.toggled.connect(self.jpg)
        self.radioButton_3.toggled.connect(self.jpeg)
        self.radioButton_4.toggled.connect(self.bmp)
            
    '''radiobuttons'''
    def jpg(self):        
        if self.sender().isChecked():
            self.jpg_ = 1
            self.statusBar().showMessage('jpg_=1')
        else:
            self.jpg_ = 0
            self.statusBar().showMessage('jpg_=0')
    def jpeg(self):        
        if self.sender().isChecked():
            self.jpeg_ = 1
            self.statusBar().showMessage('jpeg_=1')
        else:
            self.jpeg_ = 0
            self.statusBar().showMessage('jpeg_=0')
    def png(self):        
        if self.sender().isChecked():
            self.png_ = 1
            self.statusBar().showMessage('png_=1')
        else:
            self.png_ = 0
            self.statusBar().showMessage('png_=0')
    def bmp(self):        
        if self.sender().isChecked():
            self.bmp_ = 1
            self.statusBar().showMessage('bmp_=1')
        else:
            self.bmp_ = 0
            self.statusBar().showMessage('bmp_=0')
            

    def loadpic(self):
        print('[INFO] load file')
        self.statusBar().showMessage('load file')
        #self.label_11 = 'loadpic'
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择图片', self.fpath + '/', 'Image files(*.jpg *.gif *.png *.jpeg)')
        
        self.pic = QtGui.QImage(self.fname)
        self.pic_ = QtGui.QPixmap.fromImage(self.pic)
        self.size = self.pic_.size()
        self.width = self.size.width()
        self.height = self.size.height()
        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0, 0, self.width, self.height)  
        items_ = QtWidgets.QGraphicsPixmapItem(self.pic_)          
        scene.addItem(items_)
        
        self.view.setScene(scene)
        self.view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.view.show()

    def transparent(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.transparent_ = 1
            self.statusBar().showMessage('transparent_ = 1')
        else:
            self.transparent_ = 0
            self.statusBar().showMessage('transparent_ = 0')
    def red(self, state): 
        if state == QtCore.Qt.Checked:
            self.red_ = 1
            self.statusBar().showMessage('red_ = 1')
        else:
            self.red_ = 0
            self.statusBar().showMessage('red_ = 0')
    def lightblue(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.lightblue_ = 1
            self.statusBar().showMessage('lightblue_ = 1')
        else:
            self.lightblue_ = 0
            self.statusBar().showMessage('lightblue_ = 0')
    def darkblue(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.darkblue_ = 1
            self.statusBar().showMessage('darkblue_ = 1')
        else:
            self.darkblue_ = 0
            self.statusBar().showMessage('darkblue_ = 0')
    def white(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.white_ = 1
            self.statusBar().showMessage('white_ = 1')
        else:
            self.white_ = 0
            self.statusBar().showMessage('white_ = 0')
    def gradientred(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.gradientred_ = 1
            self.statusBar().showMessage('gradientred_ = 1')
        else:
            self.gradientred_ = 0
            self.statusBar().showMessage('gradientred_ = 0')
    def gradientblue(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.gradientblue_ = 1
            self.statusBar().showMessage('gradientblue_ = 1')
        else:
            self.gradientblue_ = 0
            self.statusBar().showMessage('gradientblue_ = 0')
    def gradientgray(self, state): # 透明背景cb
        if state == QtCore.Qt.Checked:
            self.gradientgray_ = 1
            self.statusBar().showMessage('gradientgray_ = 1')
        else:
            self.gradientgray_ = 0
            self.statusBar().showMessage('gradientgray_ = 0')


    '''generate results'''
    def generate(self):
        rmbg = RemoveBg(self.key, 'error.log')
        rmbg.remove_background_from_img_file(self.fname) # 生成no_bg.png
        img = Image.open(self.fname + '_no_bg.png')
        x, y = img.size
        
        extension = '.png'
        if self.jpg_ == 1:
            extension = '.jpg'
        elif self.jpeg_ == 1:
            extension = '.jpeg'
        elif self.bmp_ == 1:
            extension = '.bmp'
        # To custmize color, change values below !
        # Define background colors
        backgrounds = {
            'red': (155, 0, 0),
            'white': (255, 255, 255),
            'lightblue': (173, 216, 230),
            'darkblue': (0, 0, 139)
        }

        # Define corresponding flags
        flags = {
            'red': self.red_,
            'white': self.white_,
            'lightblue': self.lightblue_,
            'darkblue': self.darkblue_
        }

        # Define gradient flags
        gradient_flags = {
            'gradientred': self.gradientred_,
            'gradientblue': self.gradientblue_,
            'gradientgray': self.gradientgray_
        }

        for key, color in backgrounds.items():
            if flags[key] == 1:
                bg_image = Image.new('RGB', img.size, color)
                bg_image.paste(img, (0, 0, x, y), img)
                bg_image.save(f"{self.fname}_{key}{extension}") 

        for key in gradient_flags.keys():
            if gradient_flags[key] == 1:
                if key == 'gradientred':
                    start_color = (255, 0, 0)
                    end_color = (255, 192, 203)  # Example gradient from red to pink
                elif key == 'gradientblue':
                    start_color = (0, 0, 255)
                    end_color = (135, 206, 235)  # Example gradient from blue to sky blue
                elif key == 'gradientgray':
                    start_color = (128, 128, 128)
                    end_color = (192, 192, 192)  # Example gradient from gray to light gray

                gradient_bg = self.create_gradient(img.width, img.height, start_color, end_color)
                gradient_bg.paste(img, (0, 0, x, y), img)
                gradient_bg.save(f"{self.fname}_{key}{extension}")

    # Create gradient color
    def create_gradient(self, width, height, start_color, end_color):
        base = Image.new('RGB', (width, height), start_color)
        top = Image.new('RGB', (width, height), end_color)
        mask = Image.linear_gradient('L').resize((width, height))
        base.paste(top, (0, 0), mask)
        return base

    def close(self):
        sys.exit()       

def main():
    # A PyQt application requires an application object
    app = QApplication(sys.argv)
    # Create an instance of the main window
    myWin = MyWindow()
    myWin.setWindowTitle('Background Removal')
    # Display the main window
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()