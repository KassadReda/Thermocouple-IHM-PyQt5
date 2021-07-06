from time import sleep
from database import Connection,ThermoDb
from thermocoupleTemperature import ThermoTemperature
import random
import threading

class AppDb : 

    def __init__(self, min_temperature, max_temperature,thermocouplesDB=ThermoDb()):

        self.min_tempature = min_temperature
        self.max_temperature = max_temperature
        self.thermocouplesDB = thermocouplesDB
        self.thermocouplesDB.createTable()
        #threading
        self.lockRead = threading.Lock()
        self.lockWrite = threading.Lock()
        self.stopThreadRead = False
        self.stopThreadWrite = False
        self.timeSleep = 0

        
        

    
    def addingDataToDb(self) : 
        self.thermocouplesDB.clear()
        temperatures = ThermoTemperature(listTemperatures=[1.2,2.5,3.5,4.5,5.2])
        self.thermocouplesDB.create(temperatures)
        

    
    def getDataFromThermocouples(self):
        ''' Cette methode return une list de 5 temperatures [t1, t2, t3, t4, t5]'''
        # return await ser.read_temp(1) quand on aura la trame
        return random.sample(range(self.min_tempature, self.max_temperature), 5)
    
    # à modifier     
    def getDataFromDb(self,nbElements,startTimestamp):
        # 1 : (self.dataBaseForm.getDateTime()/1000000000)
        return [[1, self.getDataFromThermocouples()]]
    
    
    def addToDb(self,nbElements):
        compteur = 0
        print("Writing value : ")
        #Generate 5 random numbers between 10 and 30
        while(compteur <= nbElements):
            sleep(0.1)
            randomlist = self.getDataFromThermocouples()
            self.thermocouplesDB.create(ThermoTemperature(listTemperatures=randomlist))
            compteur += 1

    #thread

              
    def readFromDb(self):
        while not self.stopThreadRead:
            print("Reading value : ")
            self.lockRead.acquire()
            self.thermocouplesDB.display()
            self.lockWrite.release()
            sleep(0) 

    

    def addToDbThread(self,nbElements):
        compteur = 0
        while not self.stopThreadWrite:
            # le sleep permettra au pc de mettre les listes a la mm taille ça va apporter plus de fluidité
            sleep(0.1)
            print("Writing value : ")
            t1 = self.getDataFromThermocouples()
            self.lockWrite.acquire()
            self.thermocouplesDB.create(ThermoTemperature(listTemperatures=t1))
            #self.thermocouplesDB.create()
            self.lockWrite.release()
            compteur =  compteur + 1
            if(compteur == nbElements):
                self.lockWrite.release()
                self.lockRead.acquire()
                sleep(0.1)
                #compteur = 0



    def readWriteDB(self, nbElements):
        # Connexion et creation de la table
        self.thermocouplesDB.clear()
        self.lockRead.acquire()
        # Workspace
        xRead = threading.Thread(target=self.readFromDb)
        xRead.start()
        xWrite = threading.Thread(target=self.addToDbThread, args=(nbElements,))
        xWrite.start()
        print(self.thermocouplesDB.display())


