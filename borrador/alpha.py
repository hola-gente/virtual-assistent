from os import system

#Variables

alpha = ("python3 alpha.py")

print("Bienvenido a boxvoid-alpha 2.0")
print("Recuerda que en esta version no estan disponibles los caracteristicas viejas solo las nuevas")
comandos = input("/").lower



if comandos() == "juegos":

    print("Creditos a kying18 por los juegos")
    print("juegos disponibles")
    print("1. tic tac toe")
    
    print("Quieres instalarlo")
    decision = input().lower

if decision() == "si":

    print("instalando el programa...")
    system("git clone https://github.com/kying18/tic-tac-toe.git")
    print("Entra a tu carpeta boxvoid y encontraras tu juego, disfrutalo")
    print("Gracias por probar esta version")
    system(alpha)
    
if decision() == "no":

    system(alpha)


    
