# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thermo_user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 822)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1103, 711))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 100))
        self.frame.setMaximumSize(QtCore.QSize(200, 100))
        self.frame.setStyleSheet("image: url(:/logo.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.btn_basic = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_basic.sizePolicy().hasHeightForWidth())
        self.btn_basic.setSizePolicy(sizePolicy)
        self.btn_basic.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_basic.setObjectName("btn_basic")
        self.verticalLayout.addWidget(self.btn_basic)
        self.btn_reel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_reel.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_reel.setObjectName("btn_reel")
        self.verticalLayout.addWidget(self.btn_reel)
        self.btn_analyse = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_analyse.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_analyse.setObjectName("btn_analyse")
        self.verticalLayout.addWidget(self.btn_analyse)
        self.info_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.info_btn.setMaximumSize(QtCore.QSize(40, 35))
        self.info_btn.setAutoFillBackground(False)
        self.info_btn.setStyleSheet("background-repeat: no-repeat;\n"
"background-image: url(:/infoo.png);\n"
"QPushButton { padding: 10px; };")
        self.info_btn.setText("")
        self.info_btn.setObjectName("info_btn")
        self.verticalLayout.addWidget(self.info_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(887, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.frameViews = QtWidgets.QFrame(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameViews.sizePolicy().hasHeightForWidth())
        self.frameViews.setSizePolicy(sizePolicy)
        self.frameViews.setMinimumSize(QtCore.QSize(891, 700))
        self.frameViews.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameViews.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameViews.setObjectName("frameViews")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameViews)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frameViews)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lcd_temp = QtWidgets.QLCDNumber(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_temp.sizePolicy().hasHeightForWidth())
        self.lcd_temp.setSizePolicy(sizePolicy)
        self.lcd_temp.setMinimumSize(QtCore.QSize(0, 10))
        self.lcd_temp.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lcd_temp.setObjectName("lcd_temp")
        self.verticalLayout_6.addWidget(self.lcd_temp)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(10, 0))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.widget = QtWidgets.QWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 700))
        self.widget.setStyleSheet("background-image: url(:/radiateur.jpg);\n"
"background-repeat: no-repeat;")
        self.widget.setObjectName("widget")
        self.radio_btn_t1 = QtWidgets.QRadioButton(self.widget)
        self.radio_btn_t1.setEnabled(True)
        self.radio_btn_t1.setGeometry(QtCore.QRect(60, 20, 100, 30))
        self.radio_btn_t1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radio_btn_t1.setObjectName("radio_btn_t1")
        self.radio_btn_t4 = QtWidgets.QRadioButton(self.widget)
        self.radio_btn_t4.setGeometry(QtCore.QRect(420, 330, 100, 30))
        self.radio_btn_t4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radio_btn_t4.setObjectName("radio_btn_t4")
        self.radio_btn_t2 = QtWidgets.QRadioButton(self.widget)
        self.radio_btn_t2.setGeometry(QtCore.QRect(160, 120, 100, 30))
        self.radio_btn_t2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radio_btn_t2.setObjectName("radio_btn_t2")
        self.radio_btn_t3 = QtWidgets.QRadioButton(self.widget)
        self.radio_btn_t3.setGeometry(QtCore.QRect(160, 210, 100, 30))
        self.radio_btn_t3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radio_btn_t3.setObjectName("radio_btn_t3")
        self.radio_btn_t5 = QtWidgets.QRadioButton(self.widget)
        self.radio_btn_t5.setGeometry(QtCore.QRect(360, 150, 100, 30))
        self.radio_btn_t5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radio_btn_t5.setObjectName("radio_btn_t5")
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(9, 9, 681, 22))
        self.label.setObjectName("label")
        self.MplWidget = MplWidget(self.page_2)
        self.MplWidget.setGeometry(QtCore.QRect(30, 50, 291, 231))
        self.MplWidget.setObjectName("MplWidget")
        self.MplWidget_2 = MplWidget(self.page_2)
        self.MplWidget_2.setGeometry(QtCore.QRect(340, 50, 221, 221))
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.MplWidget_3 = MplWidget(self.page_2)
        self.MplWidget_3.setGeometry(QtCore.QRect(30, 290, 301, 261))
        self.MplWidget_3.setObjectName("MplWidget_3")
        self.MplWidget_4 = MplWidget(self.page_2)
        self.MplWidget_4.setGeometry(QtCore.QRect(460, 290, 361, 261))
        self.MplWidget_4.setObjectName("MplWidget_4")
        self.MplWidget_5 = MplWidget(self.page_2)
        self.MplWidget_5.setGeometry(QtCore.QRect(620, 50, 231, 231))
        self.MplWidget_5.setObjectName("MplWidget_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.checkBox_T1 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_T1.setGeometry(QtCore.QRect(140, 40, 43, 30))
        self.checkBox_T1.setObjectName("checkBox_T1")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(9, 9, 843, 22))
        self.label_3.setObjectName("label_3")
        self.checkBox_T2 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_T2.setGeometry(QtCore.QRect(240, 40, 43, 30))
        self.checkBox_T2.setObjectName("checkBox_T2")
        self.checkBox_T3 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_T3.setGeometry(QtCore.QRect(370, 40, 43, 30))
        self.checkBox_T3.setObjectName("checkBox_T3")
        self.checkBox_T4 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_T4.setGeometry(QtCore.QRect(460, 40, 43, 30))
        self.checkBox_T4.setObjectName("checkBox_T4")
        self.checkBox_T5 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_T5.setGeometry(QtCore.QRect(540, 40, 43, 30))
        self.checkBox_T5.setObjectName("checkBox_T5")
        self.btn_mise_zero = QtWidgets.QPushButton(self.page_3)
        self.btn_mise_zero.setGeometry(QtCore.QRect(770, 73, 94, 41))
        self.btn_mise_zero.setObjectName("btn_mise_zero")
        self.btn_mise_jour = QtWidgets.QPushButton(self.page_3)
        self.btn_mise_jour.setGeometry(QtCore.QRect(650, 73, 111, 41))
        self.btn_mise_jour.setObjectName("btn_mise_jour")
        self.MplWidget_6 = MplWidget(self.page_3)
        self.MplWidget_6.setGeometry(QtCore.QRect(40, 160, 811, 501))
        self.MplWidget_6.setObjectName("MplWidget_6")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 22))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.page_3)
        self.spinBox.setGeometry(QtCore.QRect(100, 70, 115, 34))
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_info = QtWidgets.QLabel(self.page_4)
        self.label_info.setGeometry(QtCore.QRect(40, 40, 2810, 220))
        self.label_info.setObjectName("label_info")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frameViews)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_basic.setText(_translate("MainWindow", "Mode basique"))
        self.btn_reel.setText(_translate("MainWindow", "Mode en temps r??el"))
        self.btn_analyse.setText(_translate("MainWindow", "Mode Analyse graphique"))
        self.label_4.setText(_translate("MainWindow", "T??mp??rature en degr??s Celsus du thermocouple selectionn??"))
        self.radio_btn_t1.setText(_translate("MainWindow", "T1"))
        self.radio_btn_t4.setText(_translate("MainWindow", "T4"))
        self.radio_btn_t2.setText(_translate("MainWindow", "T2"))
        self.radio_btn_t3.setText(_translate("MainWindow", "T3"))
        self.radio_btn_t5.setText(_translate("MainWindow", "T5"))
        self.label.setText(_translate("MainWindow", "Affichage en temps r??el la t??mp??rature de chaque thermocouple"))
        self.checkBox_T1.setText(_translate("MainWindow", "T1"))
        self.label_3.setText(_translate("MainWindow", "Affichage du graphique de temp??rature des thermocouples selectionn??s, valeurs recup??r??es depuis la base de donn??es"))
        self.checkBox_T2.setText(_translate("MainWindow", "T2"))
        self.checkBox_T3.setText(_translate("MainWindow", "T3"))
        self.checkBox_T4.setText(_translate("MainWindow", "T4"))
        self.checkBox_T5.setText(_translate("MainWindow", "T5"))
        self.btn_mise_zero.setText(_translate("MainWindow", "Mise ?? 0"))
        self.btn_mise_jour.setText(_translate("MainWindow", "Mise ?? jour"))
        self.label_2.setText(_translate("MainWindow", "D??finir T0 : "))
        self.label_info.setText(_translate("MainWindow", "page info"))
from mplwidget import MplWidget
