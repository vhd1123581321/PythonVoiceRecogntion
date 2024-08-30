import webbrowser
import speech_recognition as sr
speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input
while True:
    print('Python is listening...')
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print("Goodbye!")
        break
    elif "browser" in inp:  # browsing website using voice command 'browser' 
        inp = inp.replace('browser ', '')
        webbrowser.open("http://" + inp)
        continue
    elif "search" in inp: #google something using voice command 'search'
        inp = inp.replace('search ', '')
        webbrowser.open("http://google.com/search?q="+inp)
        continue




'''
print('Python is listening...')
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    inp = speech.recognize_google(audio)
print(f'You just said {inp}.') 
'''

'''
while True:
    print('Python is listening...')
    inp = "" 
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass        
        except sr.WaitTimeoutError:
            pass
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break
'''


