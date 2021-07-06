import sqlite3
from datetime import datetime
from sqlite3 import Error
from thermocoupleTemperature import ThermoTemperature
from uart import Uart
import asyncio


class Connection:
    connection = None

    @staticmethod
    def getInstance():
        if not Connection.connection:
            Connection.connection = Connection(r"./thermocouples.db")
        return Connection.connection

    def __init__(self, dbfile):
        try:
            self.conn = sqlite3.connect(dbfile,check_same_thread=False)
            print("db connection  version : ",sqlite3.version)
        except Error as e:
            print(e)

    def getConnection(self):
        return self.conn

    
    
    
#con = Connection.getInstance()

class ThermoDb:
    def __init__(self):
        self.conn = Connection.getInstance().getConnection()
        #self.uart = Uart()

    def createTable(self):
        # id       INTEGER PRIMARY KEY AUTOINCREMENT,datetime    INTEGER,
        sql_create_thermocouple_table = """ CREATE TABLE IF NOT EXISTS Thermocouple (
                                            id       INTEGER PRIMARY KEY AUTOINCREMENT,
                                            t1       DOUBLE,
                                            t2       DOUBLE,
                                            t3       DOUBLE,
                                            t4       DOUBLE,
                                            t5       DOUBLE); """
        try:
            c = self.conn.cursor()
            c.execute(sql_create_thermocouple_table)
            #self.conn.commit()
        except Error as e:
            print("Erreur lors de création de table Thermocouple : ", e)

    """ https://www.sqlitetutorial.net/sqlite-python/insert/ """
    
    def create(self, thermocouple = []):
        #miss datetime
        sql = """ INSERT INTO Thermocouple(t1,t2,t3,t4,t5)
              VALUES(?,?,?,?,?) """
        data = thermocouple.getValeursTemperature()
        #data = asyncio.run(self.uart.read_temperatures())
        #print("data a ajouter",data)
        try:
            print("writing data," ,data)
            c = self.conn.cursor()
            c.execute(sql,data)
            self.conn.commit()
        except Error as e:
            print("Erreur lors de l'ajout d'un element à la table Thermocouple : ",e )

    # test

    def display(self):
        sql = """ SELECT id,t1,t2,t3,t4,t5 FROM Thermocouple; """  
        c = self.conn.cursor()
        c.execute(sql)
        return c.fetchall()

    def find_by_column(self,num,t0) : 
        sql = """ SELECT id,t1,t2,t3,t4,t5 FROM Thermocouple WHERE + id >=""" + str(t0)+ """; """  
        c = self.conn.cursor()
        c.execute(sql)
        rows =  c.fetchall()

        results = []

        for row in rows : 
            results.append(row[num])

        return results
    
    # fin test
	
    def find(self, id):
        sql = '''SELECT id, t1, t2, t3, t4, t5
            FROM `Thermocouple`
            WHERE id=?;'''
        try:
            c = self.conn.cursor()
            c.execute(sql, (id,))
            print(c.fetchall())
            row = c.fetchall()[0]
            return self.rowToObject(row)
        except Error as e:
            print("Erreur lors de lecture d'un element à la table Thermocouple",e)
        pass

    def findNElements(self, nbElements):
        sql = '''SELECT id, datetime, t1, t2, t3, t4, t5
            FROM `thermocouple`
            ORDER BY id DESC
            LIMIT ?;'''
        try:
            c = self.conn.cursor()
            c.execute(sql, (nbElements,))
            rows = c.fetchall()
            list = []
            for row in rows:
                list.append(self.rowToObject(row))

            return list
        except Error as e:
            print("Erreur lors de l'ajout d'un element à la table Thermocouple",e)
        pass

    def clear(self):
        sql = 'DELETE FROM Thermocouple'
        try:
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()
        except Error as e:
            print("Erreur lors de suppression des éléments de la table Thermocouple",e)


    def rowToObject(self, row):
        dt = row[1]
        lt = [row[2], row[3], row[4], row[5], row[6]]
        return ThermoTemperature(timestamp=dt, listTemperatures=lt)
