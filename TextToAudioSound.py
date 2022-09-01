from playsound import playsound
from gtts import gTTS


your_text = gTTS('বাংলাদেশের রাজধানীর নাম ঢাকা', lang='bn')
your_text.save("Audio File/DhakaIsCapital.mp3")
playsound('Audio File/DhakaIsCapital.mp3')




