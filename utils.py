# -*- coding: utf-8 -*-
import serial

from config import SERIALPORT


def send_serial_data(data):
    # Open serial port
    try:
        ser = serial.Serial(SERIALPORT, 9600)
    except serial.SerialException:
        return

    ser.write(data)

    # Close serial port
    ser.close()


def send_command(command):
    send_serial_data('%s\n' % command)


def blink():
    send_command('blink')


def on():
    send_command('on')


def off():
    send_command('off')
