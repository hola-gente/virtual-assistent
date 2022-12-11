from codecs import charmap_decode
import pywhatkit
from os import mkdir, system
import speech_recognition as sr

#variables

alpha = ("python3 alpha.py")
    
print("Bienvenido a boxvoid")

while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Habla!")
            audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es-US")
            print(r.recognize_google(audio, language="es-US"))
        except sr.UnknownValueError:
            print("No te entiendo habla otra vez ")

        if "sumar" in texto:
            
            print ("Dime el primer numero")
            numero1 = int(input())
            print ("Dime el segundo numero")
            numero2 = int(input())
            print ("el resultado")
            print (numero1 + numero2)
            

        if "resta" in texto:
            
            print ("Dime el primer numero")
            numero1 = int(input())
            print ("Dime el segundo numero")
            numero2 = int(input())
            print ("el resultado")
            print (numero1 - numero2)
        
        if "multiplicacion" in texto:
            
            print ("Dime el primer numero")
            numero1 = int(input())
            print ("Dime el segundo numero")
            numero2 = int(input())
            print ("el resultado")
            print (numero1 * numero2)
            

        if "division" in texto:
            
            print ("Dime el primer numero")
            numero1 = int(input())
            print ("Dime el segundo numero")
            numero2 = int(input())
            print ("el resultado")
            print (numero1 / numero2)
        
        if "google" in texto:
            
            print("Que quieres buscar ")
            busqueda = input()
            pywhatkit.search(busqueda)
        
                
        if "musica" in texto:

            print("Que musica quieres escuchar")
            musica = input()
            pywhatkit.playonyt(musica)
            

        if "youtube" in texto:

            print("Que Quieres ver")
            videos = input()
            pywhatkit.playonyt(videos)
        
        if "actualizacion" in texto:
        
            print("Descargado el paquete...")
            update = ("git clone https://github.com/farsafar/boxvoid-1.0 ")
            system(update)
            print("metete a la carpeta boxvoid-alpha y dentro de esa carpeta habra otra carpeta con el mismo nombre mueva esa carpeta y elimine la antigua carpeta")
            quit()

        if "cmd" in texto:

            cmd = input("$ ")
            system(cmd)
            

        if "salir" in texto:

            quit()

        if "alpha" in texto:

            print("ejucatando nuevo codigo....")
            print("ejucatando nuevo codigo....")
            system("clear")
            system(alpha)
