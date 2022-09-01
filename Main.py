import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import datetime
from random import randint
#import keyboard  


from pyfirmata import ArduinoMega, util
from pyfirmata.util import Iterator
import time


port = 'COM3'
board = ArduinoMega(port)

HeadFunction = 7
RightHand = 6
LeftHand = 3

FireSensor = 7


it = util.Iterator(board)
it.start()

board.digital[22].write(1)



def takeCommand():
    

    r=sr.Recognizer()
    with sr.Microphone(1) as source: # --------------------------------------------------- Mick Change
        r.adjust_for_ambient_noise(source)
        board.digital[12].write(0)
        board.digital[13].write(1)
        print('I am listening you...')
        r.pause_threshold = 0.5#-----------------------------------
        audio = r.listen(source)


    try:
        board.digital[12].write(1)
        board.digital[13].write(0)
        print('Recognizing...')
        query = r.recognize_google(audio,language='bn')
        print(f'Your Command:{query}\n')

    except Exception as e:
        print('Say that agin please...')

       
    return query









def takeCommand1():
    
    r=sr.Recognizer()
    with sr.Microphone(1) as source: # --------------------------------------------------- Mick Change
        r.adjust_for_ambient_noise(source)
        board.digital[12].write(0)
        board.digital[13].write(1)
        print('I am listening you...')
        r.pause_threshold = 0.5
        audio = r.listen(source)

        


    try:
        board.digital[12].write(1)
        board.digital[13].write(0)
        print('Recognizing...')
        query = r.recognize_google(audio,language='bn')
        print(f'Your Command:{query}\n')

    except Exception as e:
        board.digital[12].write(0)
        board.digital[13].write(0)
        print('Say that agin please...')

       
    return query







if __name__=='__main__':
    board.digital[HeadFunction].write(1)
    board.digital[12].write(1)
    board.digital[13].write(1)
    
    
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        playsound('Audio File/YouTubeVideo/GoodMorning.mp3')

    elif hour>=12 and hour<= 17:
        #playsound('Audio File/YouTubeVideo/GoodAfterNoon.mp3')
        playsound('Audio File/YouTubeVideo/MyIntro.mp3')

    elif hour>17 and hour<=19:
        playsound('Audio File/YouTubeVideo/GoodEvening.mp3')

    else:
        playsound('Audio File/YouTubeVideo/GoodNight.mp3')

    board.digital[HeadFunction].write(0) 
    board.digital[12].write(0)
    board.digital[13].write(0)
    
    







    
    
    while True:
       

        try:
            query = takeCommand1()



            if 'হাই মিনা' in query or 'হ্যালো মিনা' in query or 'মিনা' in query or 'হেই মিনা' in query:
                playsound('Audio File/MySelf/HelloSir.mp3')
                query = takeCommand()
                
                
                board.digital[12].write(1)
                board.digital[13].write(1)
                
        
            

                if 'বঙ্গবন্ধুকে নিয়ে একটা গান বলো' in query or 'বঙ্গবন্ধুকে নিয়ে একটা গান' in query or 'বঙ্গবন্ধুকে নিয়ে একটি গান' in query: 
                    
                    ServoFunction('Audio File/BangabandhuSong.mp3')
                
                    
                if 'একটা ছড়া শোনাও' in query or 'একটা ছড়া বল' in query:
                    ServoFunction('Audio File/Chora.mp3')
                

                elif 'একটি লোকসংগীত শোনাও' in query or 'একটি লোকসংগীত' in query or 'একটি লোকসংগীত বলো' in query:
                    ServoFunction('Audio File/Age Ki Sundor din kataitam.mp3')
                    


                elif 'একটি গান শোনাও' in query or 'একটি গান বলো' in query or 'একটা সংগীত শোনাও' in query or 'একটা গান শোনাও' in query:
                    music_dir = 'Audio File/Song'
                    songs = os.listdir(music_dir)
                    RandomSong = randint(1, (len(os.listdir('Audio File/Song'))) - 1)
                    ServoFunction('Audio File/Song/'+ songs[RandomSong])



                elif 'আমাদের জাতির জনক কে' in query or 'বাংলাদেশের জাতির জনক কে' in query or 'জাতির জনক' in query:
                    ServoFunction('Audio File/FatherOfNation.mp3')
                    
                    
                    



                elif 'আমাদের বিজয় দিবস কত তারিখে' in query or 'আমাদের বিজয় দিবস কবে' in query or 'বাংলাদেশের বিজয় দিবস কত তারিখে' in query:
                    ServoFunction('Audio File/VictoryDay.mp3')
                    
            


                elif 'আমাদের স্বাধীনতা দিবস কত তারিখে' in query or 'আমাদের স্বাধীনতা দিবস কবে' in query or 'বাংলাদেশের স্বাধীনতা দিবস কত তারিখে' in query:
                    
                    ServoFunction('Audio File/Independence.mp3')
                    


                elif 'আন্তর্জাতিক মাতৃভাষা দিবস কত তারিখে' in query or 'আন্তর্জাতিক মাতৃভাষা দিবস কবে' in query or 'বাংলাদেশের মাতৃভাষা দিবস কত তারিখে' in query or 'বাংলাদেশের আন্তর্জাতিক মাতৃভাষা দিবস কত তারিখে' in query:
                    
                    ServoFunction('Audio File/LanguageDay.mp3')
                    


                elif 'বাংলাদেশের প্রধানমন্ত্রী কে' in query or 'বাংলাদেশের প্রধানমন্ত্রীর নাম কি' in query or 'প্রধানমন্ত্রী' in query:
                    
                    ServoFunction('Audio File/Primeminister.mp3')
                    


                elif 'বাংলাদেশের রাষ্ট্রপতি কে' in query or 'বাংলাদেশের রাষ্ট্রপতির নাম কি' in query:
                    
                    ServoFunction('Audio File/Presedent.mp3')
                    






                elif 'ডান হাত উঠাও' in query :
                    board.digital[RightHand].write(1)
                    playsound('Audio File/OkSir.mp3')
                    board.digital[RightHand].write(0)
                    
                    
                    
                    
                    


                elif 'বাম হাত উঠাও' in query :
                    board.digital[LeftHand].write(1)
                    playsound('Audio File/OkSir.mp3')
                    board.digital[LeftHand].write(0)
                    



                elif 'বাতি অন করো' in query or 'বাপি অন করো' in query:
                    board.digital[22].write(0)
                    ServoFunction('Audio File/OkSir.mp3')
                   
                    




                elif 'বাতি অফ করো' in query or 'বাপি অফ করো' in query:
                    board.digital[22].write(1)
                    ServoFunction('Audio File/OkSir.mp3')
                    
                    




                elif 'তুমি কি হাঁটাচলা করতে পারো' in query :
                    ServoFunction('Audio File/YouTubeVideo/CanYouRun.mp3')
                    



                elif 'তুমি কি কি করতে পারো' in query :
                    ServoFunction('Audio File/YouTubeVideo/WhatCanYouDoForUs.mp3')
                   

                elif 'তুমি কি আমাকে চেনো' in query :
                    ServoFunction('Audio File/YouTubeVideo/IKhowYouAreShantonu.mp3')
                   


                
                   

                elif 'বাংলাদেশের রাজধানীর নাম কি' in query or 'রাজধানী কোথায়' in query or 'রাজধানীর নাম কি' in query:
                    ServoFunction('Audio File/DhakaIsCapital.mp3')
                   



                

                


                









                else:
                    music_dir = 'Audio File/CanNotUnderstandSound'
                    songs = os.listdir(music_dir)
                    RandomSong = randint(1, (len(os.listdir('Audio File/CanNotUnderstandSound'))) - 1)
                    playsound('Audio File/CanNotUnderstandSound/'+ songs[RandomSong])
                    
            
                board.digital[7].write(0)
                board.digital[6].write(0)
                board.digital[3].write(0)
        except:
            print('Call Me Meena')





        def ServoFunction(SoundPath):
            board.digital[HeadFunction].write(1)
            playsound(SoundPath)
            board.digital[HeadFunction].write(0)



        """try:
            board.analog[FireSensor].enable_reporting()
            FireState = int(board.analog[FireSensor].read())
            print(FireState)
            if FireState < 1 :
                ServoFunction('Audio File/Fire.mp3')
        except:
            print('Fire Sensor Problem')
                        """