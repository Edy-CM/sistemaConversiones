import os
from rich.console import Console
import inquirer

console = Console()

def sistemaMRU(subProgramIsRunning):
    while subProgramIsRunning:
        os.system("cls" if os.name == "nt" else "clear")
        console.print("Bienvenido al sistema de MRU!")
        userSelection = inquirer.prompt([
            inquirer.List("options", "Seleccione la conversion que desea realizar",
                          [
                              ("1) Distancia", 1),
                              ("2) Tiempo", 2),
                              ("3) Velocidad", 3),
                              ("0) Salir", 0)
                          ])
        ])
        
        seleccion = userSelection['options']

        if (seleccion == 0):
            subProgramIsRunning = False
            break 
        
        if seleccion == 1:
            try:
                velocidad = float (input("Ingrese la velocidad: "))
                tiempo = float (input("Ingrese el tiempo: "))
            except:
                console.print("[bold][red]Tipo de dato ingresado no valido, intentelo nuevamente.[/bold][/red]")
                continue
            distancia = velocidad * tiempo
            print (f"La distancia es igual a {distancia} m")
            input("Presione enter para continuar...")

        elif seleccion == 2:
            try:
                distancia = float (input("Ingrese la distancia: "))
                tiempo = float (input("Ingrese el tiempo: "))
            except:
                console.print("[bold][red]Tipo de dato ingresado no valido, intentelo nuevamente.[/bold][/red]")
                continue
            velocidad = distancia / tiempo
            print (f"La velocidad es {velocidad} m/s")
            input("Presione enter para continuar...")

        elif seleccion == 3:
            try:
                velocidad = float (input("Ingrese la velocidad: "))
                distancia = float (input("Ingrese el distancia: "))
            except:
                console.print("[bold][red]Tipo de dato ingresado no valido, intentelo nuevamente.[/bold][/red]")
                continue
            tiempo = distancia / velocidad
            print (f"El tiempo es de: {tiempo} s")
            input("Presione enter para continuar...")