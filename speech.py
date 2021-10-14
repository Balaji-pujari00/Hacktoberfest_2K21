from gtts import gTTS
from playsound import playsound

audio="dialouge.mp3"
language='en'
t=gTTS(text="Powerful people come from powerful places",lang=language,slow=False)
t.save(audio)
playsound(audio)