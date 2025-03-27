import os
import inquirer

def metros_a_centimetros(metros : float) -> float:
    return (metros * 100)

def metros_a_milimetros(metros : float) -> float:
    return (metros * 1_000)

def centimetros_a_milimetros(centimetros : float) -> float:
    return (centimetros * 10)

def kilometros_a_metros(kilometros : float) -> float:
    return (kilometros * 1000)

def metros_a_pies(metros : float) -> float:
    return (metros * 3.28)

def metros_a_yardas(metros : float) -> float:
    return (metros * 1.093)

def pies_a_centimetros(pies : float) -> float:
    return (pies * 30.48)

def pies_a_pulgadas(pies : float) -> float:
    return (pies * 12)

def pulgadas_a_centimetros(pulgadas : float) -> float:
    return (pulgadas * 2.54)

def millas_a_kilometros(millas : float) -> float:
    return (millas * 1.609)

def libras_a_gramos(libras : float) -> float:
    return (libras * 0.5)

def kilogramos_a_libras(kilogramos : float) -> float:
    return (kilogramos * 2)

def centimetro_cubico_a_mililitros(centimetro_cubicos : float) -> float:
    return (centimetro_cubicos * 1)

def litros_a_centimetros_cubicos(litros : float) -> float:
    return (litros * 1_000)

def litros_a_decimetros_cubicos(litros : float) -> float:
    return (litros * 1)

def galones_a_litros(galones : float) -> float:
    return (galones * 3.875)



def sistemaUnidades(subProgramIsOn):
    while subProgramIsOn:
            os.system("cls")
            userSelection = inquirer.prompt(
                [
                    inquirer.List("options",
                                  "Bienvenido al Sistema de Equivalencias!",
                                  [
                                      ("1) Metros a Centimetros", 1),
                                      ("2) Metros a Milimetros", 2),
                                      ("3) Centimetros a Milimetros", 3),
                                      ("4) Kilometro a Metros", 4),
                                      ("5) Metros a Pies", 5),
                                      ("6) Metros a Yardas", 6),
                                      ("7) Pies a Centimetros", 7),
                                      ("8) Pies a Pulgadas", 8),
                                      ("9) Pulgada a Centimetros", 9),
                                      ("10) Milla a Kilometros", 10),
                                      ("11) Libra a Gramos", 11),
                                      ("12) Kilogramo a Libras", 12),
                                      ("13) Centimetros Cubicos a Mililitros", 13),
                                      ("14) Litros a Centimetros Cubicos", 14),
                                      ("15) Litros a Decimetros Cubicos", 15),
                                      ("16) Galones a Litros", 16),
                                      ("0) Salir", 0),
                                  ])
                ]
            )
            seleccion = userSelection['options']
        
            if (seleccion == 0):
                subProgramIsOn = False
                break
            elif (seleccion < 1 or seleccion > 16):
                print("Seleccion no disponible, intentelo nuevamente!")
                input()
                continue

            try:
                cantidadAConvertir = (float(input("Ingrese la cantidad inicial: ")))
            except:
                print("Tipo de dato no valido, intentelo nuevamente")
                input()
                continue

            if (seleccion == 1):
                print(f"Centimetros: {metros_a_centimetros(cantidadAConvertir)} cm")
                input()
            elif (seleccion == 2):
                print(f"Milimetros: {metros_a_milimetros(cantidadAConvertir)} mm")
                input()
            elif (seleccion == 3):
                print(f"Milimetros: {centimetros_a_milimetros(cantidadAConvertir)} mm")
                input()
            elif (seleccion == 4):
                print(f"Metros: {kilometros_a_metros(cantidadAConvertir)} m")
                input()
            elif (seleccion == 5):
                print(f"Pies: {metros_a_pies(cantidadAConvertir)} ft")
                input()
            elif (seleccion == 6):
                print(f"Yardas: {metros_a_yardas(cantidadAConvertir)} yd")
                input()
            elif (seleccion == 7):
                print(f"Centimetros: {pies_a_centimetros(cantidadAConvertir)} cm")
                input()
            elif (seleccion == 8):
                print(f"Pulgadas: {pies_a_pulgadas(cantidadAConvertir)} in")
                input()
            elif (seleccion == 9):
                print(f"Centimetros: {pulgadas_a_centimetros(cantidadAConvertir)} cm")
                input()
            elif (seleccion == 10):
                print(f"Kilometros: {millas_a_kilometros(cantidadAConvertir)} km")
                input()
            elif (seleccion == 11):
                print(f"Gramos: {libras_a_gramos(cantidadAConvertir)} g")
                input()
            elif (seleccion == 12):
                print(f"Libras: {kilogramos_a_libras(cantidadAConvertir)} lb")
                input()
            elif (seleccion == 13):
                print(f"Milimetros: {centimetro_cubico_a_mililitros(cantidadAConvertir)} mm")
                input()
            elif (seleccion == 14):
                print(f"Centimetros Cubicos: {litros_a_centimetros_cubicos(cantidadAConvertir)} cm³")
                input()
            elif (seleccion == 15):
                print(f"Decimetros Cubicos: {litros_a_decimetros_cubicos(cantidadAConvertir)} dm³")
                input()
            else:
                print(f"Litros: {galones_a_litros(cantidadAConvertir)} Lt")
                input()