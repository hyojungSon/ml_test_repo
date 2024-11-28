# install
import speech_recognition as sr
from os import path
# pip install SpeechRecognition
# pip install pyaudio
# pip install pocketsphinx
 
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "news.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# Record Audio
    # with sr.Microphone() as source:
    #     audio = r.listen(source)
    #     result = r.recognize_google(audio, language="ko-KR")
    #     print(result)

# recognize speech using Sphinx
# -offline에서 가능하나 한국어 지원이 되지 않는다.
try:
    result = r.recognize_sphinx(audio)
    print(result)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
