import speech_recognition as sr
import pyttsx3
import pyautogui
import pywhatkit
from time import *
import os
import webbrowser
import pyjokes
import AVMSpeechMath as sm
import json
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint
from googletrans import Translator



print("Bienvenido")

name = 'alexa'
attemts = 0

listener = sr.Recognizer()
engine = pyttsx3.init()

flag = 0
client_id = "008598b4768a442688901a9be08ccf4d"
client_secret = "a6a6c369f41846549f0942cc8e77f8fd"
autor = ''

with open('asistente virtual/src/keys.json') as json_file:
    keys = json.load(json_file)

green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# day_es = [line.rstrip('\n') for line in open('asistente virtual/src/day/day_es.txt')]
# day_en = [line.rstrip('\n') for line in open('asistente virtual/src/day/day_en.txt')]

# def iterateDays(now):
#     for i in range(len(day_en)):
#         if day_en[i] in now:
#             now = now.replace(day_en[i], day_es[i])
#     return now

# def getDay():
#     now = date.today().strftime("%A, %d de %B del %Y").lower()
#     return iterateDays(now)

# def getDaysAgo(rec):
#     value =""
#     if 'ayer' in rec:
#         days = 1
#         value = 'ayer'
#     elif 'antier' in rec:
#         days = 2
#         value = 'antier'
#     else:
#         rec = rec.replace(",","")
#         rec = rec.split()
#         days = 0

#         for i in range(len(rec)):
#             try:
#                 days = float(rec[i])
#                 break
#             except:
#                 pass
    
#     if days != 0:
#         try:
#             now = date.today() - timedelta(days=days)
#             now = now.strftime("%A, %d de %B del %Y").lower()

#             if value != "":
#                 return f"{value} fue {iterateDays(now)}"
#             else:
#                 return f"Hace {days} días fue {iterateDays(now)}"
#         except:
#             return "Aún no existíamos"
#     else:
#         return "No entendí"

#definicion de func
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    status = False

def translator():
    Traductor = Translator()
    Traduccion = Traductor.translate(get_audio, dest='en')
    talk(Traduccion)

    with sr.Microphone() as source:
        print(f"{green_color}({attemts}) Escuchando...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            # else:
            #     talk(f"Vuelve a intentarlo, no reconozco: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}



while True:
    rec_json = get_audio()

    rec = rec_json['text']
    status = rec_json['status']

    if status:
        if 'estas ahi' in rec:
            talk('Por supuesto')

    if 'reproduce' in rec:
        if 'spotify' in rec:
            song = rec.replace('reproduce en spotify', '').upper()
            if len(autor) > 0:

                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                result = sp.search(autor)

                for i in range(0, len(result["tracks"]["items"])):
                    name_song = result["tracks"]["items"][i]["name"].upper()
                    if song in name_song:
                        flag = 1
                        webbrowser.open(result["tracks"]["items"][i]["uri"])
                        sleep(8)
                        for i in range(28):
                            pyautogui.press("tab")
                        pyautogui.press("enter")

            if flag == 0:
                song= song.replace(" ", "%20")
                webbrowser.open(f'spotify:search:{song}')
                sleep(8)
                for i in range(28):
                    pyautogui.press("tab")  
                pyautogui.press("enter")
            talk('reproduciendo '+song+' en spotify')
        else:
            song = rec.replace('reproduce', '')
            talk(f'Reproduciendo {song}')
            pywhatkit.playonyt(song)

    elif 'hora' in rec:
        hora = strftime('%H:%M %p')
        talk('Son las '+hora)
    #     elif 'dia' in rec:
    #         if 'fue' in rec:
    #             talk(f"{getDaysAgo(rec)}")
    #         else:
    #             talk(f"Hoy es {getDay()}")

    elif 'busca' in rec:
        order = rec.replace('busca', '')
        pywhatkit.search(order)

    elif 'salir' or 'callate' in rec:
        quit()

    elif 'noticias' in rec:
        webbrowser.open_new_tab("https://cnnespanol.cnn.com/category/noticias/")

    elif 'chiste' in rec:
        chiste = pyjokes.get_joke("es")
        talk(chiste)

    elif 'cuanto es' in rec:
        talk(sm.getResult(rec))


    # elif 'envia un mensaje' in rec:
    #     pass

    # elif 'abre' in rec:
    #     orden = rec.replace('abre', '')
    #     name, appid = windowsapps.open_app(orden)
    #     talk('abriendo'+orden)

    # elif 'clima' in rec:
    #     clima = rec.replace('')

    else:
        talk('Vuelve a intentarlo, no reconozco: '+rec)