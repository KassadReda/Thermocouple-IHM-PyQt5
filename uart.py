import serial
import serial.tools.list_ports
import asyncio
import struct

import threading


"""

documentation : https://pyserial.readthedocs.io/en/latest/pyserial_api.html

example : 

ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close() 

"""

class Uart() : 



    def __init__(self, baudrate=115200, timeout=2):
        serial_port = 'COM4'
        self.serial = serial.Serial(port=serial_port, baudrate=baudrate, timeout=timeout,
                                         xonxoff=False, rtscts=False, dsrdtr=False)
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

    def show_all_uart_ports(self): 
        ports = serial.tools.list_ports.comports()
        for p in ports:
            print("port :",p.device)
        print(len(ports), 'ports found')

    
    # read_bytes ==> Get the number of bytes in the input buffer
    #read() ==> number of bytes to read
    async def read_bytes(self, number_bytes):
        while self.serial.in_waiting  < number_bytes:
            await asyncio.sleep(0.2) #sleep time
        return self.serial.read(number_bytes)
 


    async def read_uint8(self):
        return int.from_bytes(await self.read_bytes(1), "little")

    async def read_float(self):
        bytes = await self.read_bytes(4)
        return float(struct.unpack("<f", bytes)[0])

    async def read_temperatures(self):
        buffer = []
        for a in range(5):
            print(a)
            #await asyncio.sleep(0.2)
            temperature = await self.read_uint8()
            print(a,temperature)
            buffer.append(temperature)            

        return buffer

    
    def test(self):

        thread = threading.Thread(target=self.read_temperatures)
        thread.start()


    
    def serial_close(self):
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        self.serial.close()

    
    
