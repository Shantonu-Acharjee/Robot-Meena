from pyfirmata import ArduinoMega, util
from pyfirmata.util import Iterator
import time

port = 'COM3'
board = ArduinoMega(port)

it = util.Iterator(board)
it.start()



while True:
    board.digital[22].write(0)
    time.sleep(1)
    board.digital[22].write(1)
    time.sleep(1)
