import  serial
import time
import nifty_sql
from threading import Thread
from math import log

def send_data_to_database(parsed_data):
    parsed_data = [parsed_data]
    nifty_sql.insert(column_names=["Timestamp", "Temperature", "Humidity", "SoundDecibels"], values=parsed_data)
    print(parsed_data)

ser = serial.Serial(port='/dev/cu.RNBT-2625-RNI-SPP', baudrate=9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
#Tried with and without the last 3 parameters, and also at 1Mbps, same happens.

def to_db(i):
    return round(12 * log(int(i) ^ 2))

def parse_data(raw_data):
    """
    :param raw_data:
    :return: [timestamp, temperature, humidity, soundDb]
    """

    t = [str(int(time.time()))]
    split_data = raw_data.strip(' \t\n\r').split(", ")

    #Adds Time, temp, and humidity
    t.extend(split_data[0:2] )

    #Reformats sound to decibels and then adds
    t.append(to_db(split_data[2]))
    return t


ser.flushInput()
ser.flushOutput()

while True:
    raw_data = ser.readline()
    parsed_data = parse_data(raw_data)
    print parsed_data

    # file.write(str(parsed_data))

    t = Thread( target = send_data_to_database, kwargs={'parsed_data' : parsed_data} )
    t.start()
