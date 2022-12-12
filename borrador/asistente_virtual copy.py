import speech_recognition as sr
import pyttsx3
import pywhatkit
from time import *
from os import system, startfile
import webbrowser
import windowsapps
import whatsapp as whapp

print("Bienvenido")

name = 'alexa'
listener = sr.Recognizer()
key = ''
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    time.sleep(0.5)
    engine.say(text)
    engine.runAndWait()
    text_info.delete('1.0', 'end')
    if engine._inLoop:
        engine.endLoop()

def listen(phrase=None):
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        if phrase != None:
            talk(phrase)
        else:
            pass
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return

# def enviar_mensajes(rec):
#     talk("¿Aquien quieres enviar el mensaje")
#     contact = listen("Te escucho")
#     contact = contact.strip()
#     if contact in contacts:
#         for cont in contact:
#             if cont == contact:
#                 contact = contacts[cont]
#                 talk("Que mensaje quieres enviar")
#                 mensajes = listen("Te escucho")
#                 talk("Enviando mensajes..")
#                 whapp.send_message(contact, mensajes)

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
        pass
    # elif 'abre' in rec:
    #     orden = rec.replace('abre', '')
    #     name, appid = windowsapps.open_app(orden)
    #     talk('abriendo'+orden)

    # elif 'clima' in rec:
    #     clima = rec.replace('')
    else:
        talk('Vuelve a intentarlo, no reconozco: '+rec)

run()