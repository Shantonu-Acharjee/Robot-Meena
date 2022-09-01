from pyfirmata import ArduinoMega
import time

port = 'COM3'
board = ArduinoMega(port)





def ListenFunction(valu):
    if valu == 1:
        board.digital[13].write(1)
        
        

    if valu != 1:
        board.digital[13].write(0)
        






def RecognizingFunction(valu):
    if valu == 1:
        board.digital[12].write(1)
        

    if valu != 1:
        board.digital[12].write(0)




def HeadFunction(valu):
    if valu == 1:
        board.digital[7].write(1)
        

    if valu != 1:
        board.digital[7].write(0)










def RightHand(valu):
    if valu == 1:
        board.digital[6].write(1)
        

    if valu != 1:
        board.digital[6].write(0)



def LeftHand(valu):
    if valu == 1:
        board.digital[3].write(1)
        

    if valu != 1:
        board.digital[3].write(0)








