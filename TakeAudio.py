import speech_recognition as sr


while True:

    r=sr.Recognizer()
    with sr.Microphone(1) as source: #----------------------------------------------------------Mick
        print('I am listening you...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='bn')
        print(f'Your Command:{query}\n')



    except Exception as e:
        print('Say that agin please...')
        
