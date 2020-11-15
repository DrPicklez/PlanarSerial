import serial
import numpy

serialOne = serial.Serial('/dev/tty5')
serialTwo = serial.Serial('/dev/ttySC0')
serialOne.baudrate = 19200
serialTwo.baudrate = serialOne.baudrate

brightness = 100
message = numpy.array([0x07, 0x01, 0x02, 0x42, 0x52, 0x49, brightness, 0x08])

global oldMessage

if message != oldMessage:
    if serialOne.is_open and serialTwo.is_open:
        serialOne.write(message)
        serialTwo.write(message)
        print("messageSent")
        oldMessage = message

