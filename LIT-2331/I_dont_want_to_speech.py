import speech_recognition as sr
import time
import win32com.client
import pathlib


PATH = str(pathlib.Path(__file__).parent.resolve())
r = sr.Recognizer()
mic = sr.Microphone()


def say(phrase):
    win32com.client.Dispatch("SAPI.SpVoice").Speak(phrase)


while(True):
    with mic as source:
        try:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source, duration=0.5)
            re = r.recognize_google(audio)
            print(re)
            if re == 'stop' or re == 'exit':
                say('exiting in three seconds')
                for x in [3, 2, 1, 0]:
                    print('exiting in %s seconds' % x, end='\r')
                    if x != 0:
                        say(x)
                        time.sleep(1)
                say('exit!')
                break
            else:
                say(re)
                if ('read' in re) and ('document' in re):
                    with open(PATH + '\doc.txt')as doc:
                        docs = doc.read()
                        say(docs)
        except:
            print('unable to recognize', end='\r')
            continue
