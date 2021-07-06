# This Python file uses the following encoding: utf-8

import os
from appDb import AppDb
import sys
from time import sleep
import threading
import asyncio
from PyQt5 import QtWidgets
# from thermo import Ui_MainWindow
from mainwindows import Ui_MainWindow
import random
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

import numpy as np
from mplwidget import MplWidget

from database import ThermoDb
import project_rc
import project_folder_rc
from random import uniform
from uart import Uart





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        #super(MainWindow, self).__init__(*args, **kwargs)
        super(__class__, self).__init__(*args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        # init Db 
        self.data_base = AppDb(min_temperature=0,max_temperature=170)
        # add a first data
        self.data_base.addingDataToDb()
        # add data
        self.data_base.addToDb(2)

        # variables

        self.axe_x = []
        self.axe_y1 = []
        self.axe_y2 = []
        self.axe_y3 = []
        self.axe_y4 = []
        self.axe_y5 = []
        self.t0 = 0
        
        
        #PAGE 4 => info
        self.info_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.info_btn.clicked.connect(self.boxInfo)

        # PAGE 1
        self.btn_basic.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.radio_btn_t1.toggled.connect(self.lcdSetValue_1)
        self.radio_btn_t2.toggled.connect(self.lcdSetValue_2)
        self.radio_btn_t3.toggled.connect(self.lcdSetValue_3)
        self.radio_btn_t4.toggled.connect(self.lcdSetValue_4)
        self.radio_btn_t5.toggled.connect(self.lcdSetValue_5)
        # PAGE 2
        self.btn_reel.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_reel.clicked.connect(self.graphs_real_time)
        # PAGE 3
        self.btn_analyse.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        self.btn_mise_zero.clicked.connect(self.clear_graph)
        self.btn_mise_jour.clicked.connect(self.update_graph)
        # uart
        print("affiche")
        self.show()
        print("je passe")
        self.data_base.readWriteDB(1000)
        

    def graphs_real_time(self) : 
        self.graph_from_db(self.MplWidget,1)
        self.graph_from_db(self.MplWidget_2,2)
        self.graph_from_db(self.MplWidget_3,3)
        self.graph_from_db(self.MplWidget_4,4)
        self.graph_from_db(self.MplWidget_5,5)
        #self.update_graph(self.MplWidget_6)

    def update_graph(self):
        #clear axes
        self.MplWidget_6.canvas.axes.cla()
        self.t0 = self.spinBox.value()
        legend = []

        self.axe_x = self.data_base.thermocouplesDB.find_by_column(0,self.t0)
        if (self.checkBox_T1.isChecked()) : 
            self.axe_y1 = self.data_base.thermocouplesDB.find_by_column(1,self.t0)
            legend.append('T1')
            #self.MplWidget_6.canvas.axes.legend(legend)
            self.MplWidget_6.canvas.axes.plot(self.axe_x, self.axe_y1)
            
        if (self.checkBox_T2.isChecked()) :  
            self.axe_y2 = self.data_base.thermocouplesDB.find_by_column(2,self.t0)
            legend.append('T2')
            #self.MplWidget_6.canvas.axes.legend(legend)
            self.MplWidget_6.canvas.axes.set_label("t2")
            self.MplWidget_6.canvas.axes.plot(self.axe_x, self.axe_y2)

        if (self.checkBox_T3.isChecked()) : 
            self.axe_y3 = self.data_base.thermocouplesDB.find_by_column(3,self.t0)
            legend.append('T3')
            #self.MplWidget_6.canvas.axes.legend(legend)
            self.MplWidget_6.canvas.axes.plot(self.axe_x, self.axe_y3)
            
        if (self.checkBox_T4.isChecked()) :  
            self.axe_y4 = self.data_base.thermocouplesDB.find_by_column(4,self.t0)
            legend.append('T4')
            #self.MplWidget_6.canvas.axes.legend(legend)
            self.MplWidget_6.canvas.axes.plot(self.axe_x, self.axe_y4)

        if (self.checkBox_T5.isChecked()) :  
            self.axe_y5 = self.data_base.thermocouplesDB.find_by_column(5,self.t0)
            legend.append('T5')
            #self.MplWidget_6.canvas.axes.legend(legend)
            self.MplWidget_6.canvas.axes.plot(self.axe_x, self.axe_y5)
			
			
        self.MplWidget_6.canvas.axes.set_ylabel('temperatures')
        self.MplWidget_6.canvas.axes.set_xlabel('n')
        self.MplWidget_6.canvas.axes.legend(legend)
        self.MplWidget_6.canvas.draw()
		

    def graph_from_db(self, mplwidget_number,num) : 
        
        axe_y = []
        axe_x = []
        for element in self.data_base.thermocouplesDB.display() : 
            axe_x.append(element[0])
            axe_y.append(element[num])

        mplwidget_number.canvas.axes.set_title('Thermocouple '+  str(num))
        mplwidget_number.canvas.axes.plot(axe_x, axe_y)
        mplwidget_number.canvas.draw()
    
    

    def clear_graph(self):
        self.MplWidget_6.canvas.axes.clear()
        # self.MplWidget_6.canvas.axes.plot(t, t)
        self.MplWidget_6.canvas.draw()
        print("clear le graph")

    # setting lcd values from DB pas de chgmnt de valeur automaique
    def lcdSetValue_1(self):

        self.lcd_temp.display(float((round(self.data_base.thermocouplesDB.display()[-1][1],2))))

    def lcdSetValue_2(self):

        self.lcd_temp.display(float((round(self.data_base.thermocouplesDB.display()[( - 1 )][2],2))))
    
    def lcdSetValue_3(self):

        self.lcd_temp.display(float((round(self.data_base.thermocouplesDB.display()[(- 1 )][3],2))))

    def lcdSetValue_4(self):

        self.lcd_temp.display(float((round(self.data_base.thermocouplesDB.display()[( - 1 )][4],2))))

    def lcdSetValue_5(self):

        self.lcd_temp.display(float((round(self.data_base.thermocouplesDB.display()[( - 1 )][5],2))))

    
    def boxInfo(self):
        
        #test = asyncio.run(self.serial.read_temperatures())
        #print(test)
        self.label_info.setText("""GUIDE UTULISATION IHM IPS 2021 S7P BY REDA KASSAD  \n Pour toute question contactez-moi sur : r7kassad@enib.fr \n \n \n  \t \t Mode Basique :
		\t Ce mode permet d'afficher la témpérature du termocouple selectionné. 
		\n \n   \t \t Mode Temps reel :
		\t Comme son nom l'indique, nous avons un graphique pour chaque thermocouple. \n \t \t \t Et on suit l'evolution de la temperature en temps réel, des 5 thermocouples.
        \n \n   \t \t Mode Analyse graphique : 
        \t \t \t C'est un mode qui permet de visualiser un ou plusieurs thermocouple, \n \t \t \t et nous pouvons fixer T0 (à partir de quand on veut visualiser les tempèratures) . """)


        
        
    
        
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()

app.exec_()








