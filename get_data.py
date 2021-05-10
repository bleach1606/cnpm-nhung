import serial
import numpy as np
import time
import pandas as pd


ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/cu.usbserial-0001'
ser.open()
ser.readline()


data = {"ax": [], "ay": [], "az": [], "T": [], "gx": [], "gy": [], "gz": []}

while True:
    try:
        response = ser.readline().split()
        print(response)
        ax = float(response[1])
        ay = float(response[3])
        az = float(response[5])
        T = float(response[7])
        gx = float(response[9])
        gy = float(response[11])
        gz = float(response[13])

        data['ax'].append(ax)
        data['ay'].append(ay)
        data['az'].append(az)
        data['T'].append(T)
        data['gx'].append(gx)
        data['gy'].append(gy)
        data['gz'].append(gz)

    except KeyboardInterrupt:
        df = pd.DataFrame(data=data)
        df.to_csv("/Users/v/PycharmProjects/untitled3/data.csv", index=False)
        break
        raise
