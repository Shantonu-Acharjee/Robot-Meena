from pyfirmata import ArduinoMega
import time

port = 'COM3'
board = ArduinoMega(port)


while True:
    board.digital[7].write(0)
    
    time.sleep(1)
    board.digital[7].write(1)
    
    time.sleep(1)








