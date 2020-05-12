#!/usr/bin/python3

################
## PARAMETERS ##
################

SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
CONVERT_LF_TO_CR = True

##########
## CODE ##
##########

from serial import Serial
from sys import stdin, stdout
from threading import Thread
from time import sleep

s = Serial(port = SERIAL_PORT, baudrate = BAUDRATE)
char_tx_delay = 0.01
line_tx_delay = 0.1

def send():
    while True:
        c = stdin.read(1)
        if CONVERT_LF_TO_CR and c == '\n':
            c = '\r'
        s.write(c.encode())
        sleep(line_tx_delay if c == '\r' else char_tx_delay)

def read():
    while True:
        c = s.read()
        if c==b'':
            continue
        stdout.buffer.write(c)
        stdout.flush()

Thread(target = send).start()
Thread(target = read).start()
