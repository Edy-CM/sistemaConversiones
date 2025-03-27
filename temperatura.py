import os
from rich.console import Console
import inquirer

console = Console()

def kelvin_a_celsius(temp):
    return temp - 273

def kelvin_a_farenheit(temp):
    return (temp - 273.15) * 9 / 5 + 32

def farenheit_a_celsius(temp):
    return (temp - 32) * 5 / 9

def farenheit_a_kelvin(temp):
    return ((temp - 32) / 9) + 273.15

def celsius_a_kelvin(temp):
    return temp + 273.151

def celsius_a_farenheit(temp):
    return 9 * temp / 5 + 32

def sistemaTemperatura(subProgramIsRunning: bool):
    while subProgramIsRunning:
        os.system("cls" if os.name == "nt" else "clear")
        console.print("Bienvenido al Sistema de Conversor de Temperatura")
        userSelection = inquirer.prompt([
            inquirer.List("options",
                          "Seleccione el tipo de conversion que desea realizar",
                          [
                              ("1) Kelvin a Celsius", 1),
                              ("2) Kelvin a Farenheit", 2),
                              ("3) Farenheit a Celsius", 3),
                              ("4) Farenheit a Kelvin", 4),
                              ("5) Celsius a Kelvin", 5),
                              ("6) Celsius a Farenheit", 6),
                              ("0) Salir", 0)
                          ])
        ])
        seleccion = userSelection['options']

        if (seleccion == 0):
            subProgramIsRunning = False
            break

        try:
            temp = float(input("Ingrese la temperatura a convertir: "))
        except:
            console.print("[bold][red]Tipo de dato no valido, intentelo nuevamente[/bold][/red]")
            input()
            continue

        if seleccion ==1:
            print (f"Celsius: {kelvin_a_celsius(temp=temp)} °C")
            input("Presione enter para continuar...")
        elif seleccion == 2:
            print (f"Farenheit: {kelvin_a_farenheit(temp)} °F")
            input("Presione enter para continuar...")
        elif seleccion == 3:
            print (f"Celsius: {farenheit_a_celsius(temp)} °C")
            input("Presione enter para continuar...")
        elif seleccion == 4:
            print (f"Kelvin: {farenheit_a_kelvin(temp)} °K")
            input("Presione enter para continuar...")
        elif seleccion == 5:
            print (f"Kelvin: {celsius_a_kelvin(temp)} °K")
            input("Presione enter para continuar...")
        else:
            print (f"Farenheit: {celsius_a_farenheit(temp)} °F")
            input("Presione enter para continuar...")