import serial

import threading
from threading import Thread

def read_serial_data_():
    # t = Thread(target=write_data_to_azure)
    #
    # t.start()
    while True:
        data_raw = ser.readline()
        print(data_raw)


# def func2():
#     while True:
#         print 'Working 2'
#
# if __name__ == '__main__':
#     Thread(target = func1).start()
#     Thread(target = func2).start()


ser = serial.Serial(port='/dev/cu.Bluetooth-Incoming-Port', baudrate=9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
#Tried with and without the last 3 parameters, and also at 1Mbps, same happens.


ser.flushInput()
ser.flushOutput()
i = 0
with open("/Users/David/Downloads/messing.txt", 'a') as file:
    while True:
        data_raw = ser.readline()
        print i, data_raw.strip(' \t\n\r')
        file.write(data_raw)
        i += 1
