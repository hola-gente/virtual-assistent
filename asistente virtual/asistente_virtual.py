import speech_recognition as sr
import pyttsx3
import pywhatkit
from time import *
from os import system, startfile
import windowsapps
import webbrowser
import pyautogui as at

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
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
            else:
                talk('Vuelve a intentarlo, no reconozco: '+rec)
    except:
        pass
    return rec

def enviar_msj(contact, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(8)
    at.press('enter')

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('reproduciendo '+music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = strftime('%H:%M %p')
        talk('Son las '+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        pywhatkit.search(order)
    elif 'salir' in rec:
        quit()
    elif 'noticias' in rec:
        webbrowser.open_new_tab("https://cnnespanol.cnn.com/category/noticias/")
    elif 'envia un mensaje' in rec:
        talk("¿A quién quieres enviar el mensaje?")
        contact = listen("Te escucho")
        contact = contact.strip()
        if contact in contacts:
            for cont in contacts:
                if cont == contact:
                    contact = contacts[cont]
                    talk("¿Qué mensaje le quieres enviar")
                    message = listen("Te escucho")
                    talk("Enviando mensaje...")
                    enviar_msj(contact, message)
        else:
            talk("Parece que ese contacto no lo tienes agregado, usa el botón de \
            agregar contacto!")
    # elif 'abre' in rec:
    #     orden = rec.replace('abre', '')
    #     name, appid = windowsapps.open_app(orden)
    #     talk('abriendo'+orden)

    # elif 'clima' in rec:
    #     clima = rec.replace('')

    else:
        talk('Vuelve a intentarlo, no reconozco: '+rec)

run()