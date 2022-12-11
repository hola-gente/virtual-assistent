import speech_recognition as sr
import pyttsx3
import pywhatkit
from time import *
from os import system, startfile
import windowsapps
import webbrowser

print("Bienvenido")

name = 'alexa'
listener = sr.Recognizer()
key = ''
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
            else:
                talk('Vuelve a intentarlo, no reconozco: '+rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', 'Reproduciendo')
        talk(music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = strftime('%H:%M %p')
        talk('Son las '+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        pywhatkit.search(order)
    elif 'salir' in rec:
        quit()
    elif 'noticia' in rec:
        webbrowser.open_new_tab("https://cnnespanol.cnn.com/category/noticias/")

    # elif 'abre' in rec:
    #     orden = rec.replace('abre', '')
    #     name, appid = windowsapps.open_app(orden)
    #     talk('abriendo'+orden)

    # elif 'clima' in rec:
    #     clima = rec.replace('')

    else:
        talk('Vuelve a intentarlo, no reconozco: '+rec)

run()