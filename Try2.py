from pyfirmata import ArduinoMega
import time

port = 'COM3'
board = ArduinoMega(port)


def IAmLissening():
    board.digital[12].write(0)
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[12].write(1)
    board.digital[13].write(1)
    time.sleep(1)








