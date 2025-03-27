import os
import inquirer
from rich.console import Console
from temperatura import sistemaTemperatura
from mru import sistemaMRU
from unidades import sistemaUnidades
from minisuper import sistemaMinisuper

console = Console()
programIsRunning = True

while programIsRunning:
    subProgramIsRunning = True
    os.system("cls" if os.name == "nt" else "clear")
    console.print("Bienvenido al sistema principal")
    userSelection = inquirer.prompt([
        inquirer.List("options",
                      "Seleccione el sistema que desea ejecutar",
                      [
                          ("1) Sistema de conversion de Temperatura", 1),
                          ("2) Sistema de conversion de MRU", 2),
                          ("3) Sistema de conversion de unidades", 3),
                          ("4) Sistema de ventas de Minisuper", 4),
                          ("0) Salir", 0)
                      ])
    ])
    seleccion = userSelection['options']

    if seleccion == 0:
        console.print("Nos vemos!")
        subProgramIsRunning = False
        programIsRunning = False
        break

    elif seleccion == 1:
        sistemaTemperatura(subProgramIsRunning)

    elif seleccion == 2:     
      sistemaMRU(subProgramIsRunning)

    elif seleccion == 3:
        sistemaUnidades(subProgramIsRunning)
    elif seleccion == 4:
        sistemaMinisuper(subProgramIsRunning)


