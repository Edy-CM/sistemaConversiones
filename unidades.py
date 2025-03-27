import os
from rich.console import Console
import inquirer

def metros_a_cm(metros):
    return metros * 100

def metros_a_mm(metros):
    return metros * 1000

def centimetros_a_mm(centimetros):
    return centimetros * 10

def kilometros_a_m(kilometros):
    return kilometros * 1000

def metros_a_pies(metros):
    return metros * 3.28084

def metros_a_yardas(metros):
    return metros * 1.0935

def pies_a_cm(pies):
    return pies * 30.48

def pies_a_pulgadas(pies):
    return pies * 12

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

def millas_a_km(millas):
    return millas * 1.60934

def libras_a_gramos(libras):
    return libras * 453.592

def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.2

def centimetros_cubicos_a_ml(centimetros_cubicos):
    return centimetros_cubicos * 1

def litros_a_cc(litros):
    return litros * 1000

def litros_a_decimetroscubicos(litros):
    return litros * 1000

def galones_a_litros(galones):
    return galones * 3.78541

console = Console()

def sistemaUnidades(subProgramIsRunning):
    while subProgramIsRunning:
        os.system("cls" if os.name == "nt" else "clear")
        console.print("Bienvenido al sistema de Unidades!")
        userSelection = inquirer.prompt(
            [
                inquirer.List("options", "Seleccione el tipo de conversion que desea hacer",
                              [
                                  ("1) Metros a Centimetros", 1),
                                  ("2) Metros a Milimetros",2),
                                  ("3) Centimetros a Milimetros",3),
                                  ("4) Kilometros a Metros",4),
                                  ("5) Metros a Pies",5),
                                  ("6) Metros a Yardas",6),
                                  ("7) Pies a Centimetros",7),
                                  ("8) Pies a Pulgadas",8),
                                  ("9) Pulgadas a Centimetros",9),
                                  ("10) Millas a Kilometros",10),
                                  ("11) Libras a Gramos",11),
                                  ("12) Kilogramos a Libras",12),
                                  ("13) Centimetros Cubicos a Mililitros",13),
                                  ("14) Litros a Centimetros Cubicos",14),
                                  ("15) Litros a Decimetros Cubicos",15),
                                  ("16) Galones a Litros",16),
                                  ("0) Salir", 0)
                              ])
            ]
        )
        
        seleccion = userSelection['options']

        if (seleccion == 17):
            subProgramIsRunning = False
            break
            
        try:
            unidadInicial = float(input("Ingrese la unidad inicial: "))
        except:
            console.print("[bold][red]Tipo de dato ingresado no valido, intentelo nuevamente[/red][/bold]")
            continue

        if seleccion == 1:
            print(f"{unidadInicial} metros son {metros_a_cm(unidadInicial)} centimetros")
            input("Presione enter para continuar...")
        elif seleccion == 2:
            print(f"{unidadInicial} metros son {metros_a_mm(unidadInicial)} milimetros")
            input("Presione enter para continuar...")
        elif seleccion == 3:
            print(f"{unidadInicial} centimetros son {centimetros_a_mm(unidadInicial)} milimetros")
            input("Presione enter para continuar...")
        elif seleccion == 4:
            print(f"{unidadInicial} kilometros son {kilometros_a_m(unidadInicial)} metros")
            input("Presione enter para continuar...")
        elif seleccion == 5:
            print(f"{unidadInicial} metros son {metros_a_pies(unidadInicial)} pies")
            input("Presione enter para continuar...")
        elif seleccion == 6:
            print(f"{unidadInicial} metros son {metros_a_yardas(unidadInicial)} yardas")
            input("Presione enter para continuar...")
        elif seleccion == 7:
            print(f"{unidadInicial} pies son {pies_a_cm(unidadInicial)} centimetros")
            input("Presione enter para continuar...")
        elif seleccion == 8:
            print(f"{unidadInicial} pies son {pies_a_pulgadas(unidadInicial)} pulgadas")
            input("Presione enter para continuar...")
        elif seleccion == 9:
            print(f"{unidadInicial} pulgadas son {pulgadas_a_cm(unidadInicial)} centimetros")
            input("Presione enter para continuar...")
        elif seleccion == 10:
            print(f"{unidadInicial} millas son {millas_a_km(unidadInicial)} kilometros")
            input("Presione enter para continuar...")
        elif seleccion == 11:
            print(f"{unidadInicial} libras son {libras_a_gramos(unidadInicial)} gramos")
            input("Presione enter para continuar...")
        elif seleccion == 12:
            print(f"{unidadInicial} kilogramos son {kilogramos_a_libras(unidadInicial)} libras")
            input("Presione enter para continuar...")
        elif seleccion == 13:
            print(f"{unidadInicial} centimetros cubicos son {centimetros_cubicos_a_ml(unidadInicial)} mililitros")
            input("Presione enter para continuar...")
        elif seleccion == 14:
            print(f"{unidadInicial} litros son {litros_a_cc(unidadInicial)} centimetros cubicos")
            input("Presione enter para continuar...")
        elif seleccion == 15:
            print(f"{unidadInicial} litros son {litros_a_decimetroscubicos(unidadInicial)} decimetros cubicos")
            input("Presione enter para continuar...")
        elif seleccion == 16:
            print(f"{unidadInicial} galones son {galones_a_litros(unidadInicial)} litros")
            input("Presione enter para continuar...")