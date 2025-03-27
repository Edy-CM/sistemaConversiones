from rich.console import Console
from rich.table import Table
import os
import inquirer

carrito_personal = {}
discount = 0

inventario = {
    "canasta_basica": {
                    "Arroz (1 lb)": {"Precio": 9, "Cantidad": 50},
                    "Frijoles (1 lb)": {"Precio": 20, "Cantidad": 50},
                    "Azúcar (1 lb)": {"Precio": 12, "Cantidad": 35},
                    "Harina (1 lb)": {"Precio": 15, "Cantidad": 40},
                    "Tomate (1 lb)": {"Precio": 16, "Cantidad": 10},
                    "Leche (lt)": {"Precio": 37, "Cantidad": 8}
                },
    "Snacks": {
                        "Doritos": {"Precio":35, "Cantidad":40},
                        "Cheetos":{"Precio": 32, "Cantidad":40},
                        "Zambos":{"Precio": 30, "Cantidad":40},
                        "Mani": {"Precio": 15, "Cantidad":25},
                        "Yogurt":{"Precio":15, "Cantidad":15},
                        "Cereal":{"Precio": 90, "Cantidad": 8},
                    },
    "Panaderia":{
                        "Semita (Bolsa)":{"Precio":35, "Cantidad":10},
                        "Pan Molde (Bolsa)":{"Precio": 50,"Cantidad":10},
                        "Pan Integral (Bolsa)":{"Precio":65,"Cantidad":6},
                        "Galletas de Chocolate (unidad)":{"Precio":15,"Cantidad":30},
                        "Pie de limon (Bandeja)":{"Precio":200,"Cantidad":6},
                        "Cheesecake (Bandeja)":{"Precio":250,"Cantidad":6},
                    },
    "Cuidado_Hogar":{
                        "Cloro(64 onz)":{"Precio":50,"Cantidad":5},
                        "Desinfectante Multiusos Aerosol (12.5 onz)":{"Precio":150,"Cantidad":6},
                        "Desinfectante Aromatizado (2l)":{"Precio":90,"Cantidad":6},
                        "Repelente (177ml)":{"Precio":120,"Cantidad":5},
                        "Jabon lavaplatos liquido":{"Precio":40,"Cantidad":6},
                        "Pastilla desodorizante Baño":{"Precio":16,"Cantidad":15}
                    },
    "Belleza_Higiene": {
                        "Pastilla desodorante Baño (Unidad)": {"Precio": 16, "Cantidad": 15},
                        "Desodorante": {"Precio": 65, "Cantidad": 10},
                        "Jabón de olor": {"Precio": 20, "Cantidad": 20},
                        "Cepillo de diente": {"Precio": 15, "Cantidad": 50},
                        "Pasta de diente": {"Precio": 45, "Cantidad": 10},
                        "Crema humectante": {"Precio": 120, "Cantidad": 6},
                        "Perfume": {"Precio": 350, "Cantidad": 8},
                    },
    "Frutas_Verduras": {
                        "Bananos (1 lb)": {"Precio": 20, "Cantidad": 15},
                        "Uvas (1 lb)": {"Precio": 45, "Cantidad": 10},
                        "Manzanas (1 lb)": {"Precio": 30, "Cantidad": 20},
                        "Aguacate (Unidad)": {"Precio": 25, "Cantidad": 25},
                        "Chile Dulce (1 lb)": {"Precio": 18, "Cantidad": 50},
                        "Cebollas (1 lb)": {"Precio": 20, "Cantidad": 40},
                    },
    "Carnes_Pesqueria" : {
                        "Pescado (1 lb)": {"Precio": 100, "Cantidad": 20},
                        "Pollo (1 lb)": {"Precio": 70, "Cantidad": 20},
                        "Carne Res (1 lb)": {"Precio": 85, "Cantidad": 20},
                        "Carne Cerdo (1 lb)": {"Precio": 70, "Cantidad": 20},
                        "Carne Molida (1 lb)": {"Precio": 65, "Cantidad": 12},
                        "Lomo de Cerdo (1 lb)": {"Precio": 80, "Cantidad": 80},
                    }
}

def imprimirProductos(title:str, products:dict):
    os.system("cls" if os.name == "nt" else 'clear')
    table = Table(title=f"Productos de {title}")
    table.add_column("Producto", justify="left", style="white")
    table.add_column("Cantidad", justify="center", style="blue")
    table.add_column("Precio", justify="center", style="blue")

    for product, data in products.items():
        table.add_row(product, str(data['Cantidad']), f"{data['Precio']} lps")

    console.print(table)
    input("Presione enter para continuar...")

console = Console()

def agregarAlCarrito():
    os.system("cls" if os.name == "nt" else "clear")
    userSelection = inquirer.prompt(
            [
                inquirer.List("options",
                                      "Seleccione que desea agregar al carrito",
                                      [
                                          ("1) Canasta Basica", 1),
                                          ("2) Snacks", 2),
                                          ("3) Panaderia", 3),
                                          ("4) Cuidado y Hogar", 4),
                                          ("5) Belleza e Higiene", 5),
                                          ("6) Frutas y Verduras", 6),
                                          ("7) Carnes y Pesqueria", 7),
                                          ("0) Salir", 0)
                                      ])
            ]
        )
    
    seleccion = userSelection['options']
    questions = []
    category = ""
    
    if (seleccion == 0):
        return
    elif (seleccion == 1):
        category = 'canasta_basica'
    elif (seleccion == 2):
        category = 'Snacks'
    elif (seleccion == 3):
        category = 'Panaderia'
    elif (seleccion == 4):
        category = 'Cuidado_Hogar'
    elif (seleccion == 5):
        category = 'Belleza_Higiene'
    elif (seleccion == 6):
        category = 'Frutas_Verduras'
    else:
        category = 'Carnes_Pesqueria'
    questions = [ inquirer.Checkbox("productos", "Seleccione los productos a añadir a su carrito", [product for product in inventario[category]])]
    products_selected = inquirer.prompt(questions)
    amount_questions = [inquirer.Text(f"product{index}", message=f"Ingrese la cantidad de {product} que llevara: ") for index, product in enumerate(products_selected['productos'])]
    amount = inquirer.prompt(amount_questions)

    for index, product in enumerate(products_selected['productos']):
        cantidad = int(amount[f"product{index}"])
        stock_de_producto = inventario[category][product]['Cantidad']
        if  cantidad > stock_de_producto:
            console.print(f'[bold][red]La cantidad de {product} excede el inventario[/red][/bold]\nHay {stock_de_producto} disponible.')
            continue
        
        carrito_personal[product] = {
            "Cantidad": amount[f'product{index}'],
            "Precio": inventario[category][product]['Precio'],
            "Category": category
        }

def agregarDescuento():
    global discount
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(f"[bold][green]Descuento actual: {discount}%[/green][/bold]")
    discount_question = inquirer.prompt([inquirer.Text('value', "Ingrese su nuevo descuento: ")])
    discount = int(discount_question['value'])

def procederAlPago():
    global carrito_personal
    os.system('cls' if os.name == 'nt' else 'clear')
    table = Table(title="Canasta personal")
    table.add_column("Productos", justify="left", style="white")
    table.add_column("Cantidad", justify="center", style="blue")
    table.add_column("Precio", justify="center",style="blue")
    table.add_column("Subtotal", justify="center", style="green")
    subTotal = 0

    for product, data in carrito_personal.items():
        productSubTotal = int(data['Cantidad']) * float(data['Precio'])
        subTotal += productSubTotal
        table.add_row(product, str(data['Cantidad']), f"{data['Precio']} lps", f"{productSubTotal} lps")
    
    console.print(table)
    console.print(f"[bold]SubTotal:[/bold] {subTotal} lps")
    subTotalDiscount = subTotal * (discount / 100)
    subTotal -= subTotalDiscount
    console.print(f"[bold][green]Descuento {discount}%:[/green][/bold] {subTotalDiscount} lps")
    taxes = subTotal * 0.15
    total = subTotal + taxes
    console.print(f"[bold][red]Impuestos:[/red][/bold] {taxes} lps")
    console.print(f"[bold]Total:[/bold] {total} lps")
    
    console.print('[bold]Desea continuar con el pago?[/bold]')
    continuePayment = inquirer.prompt([inquirer.Confirm("confirm")])
    if (not continuePayment['confirm']):
        return
    
    console.print("[bold][green]Se ha completado el pago con exito[/green][/bold]")
    for product, data in carrito_personal.items():
        inventario[data['Category']][product]['Cantidad'] -= int(data['Cantidad'])
    
    carrito_personal = {}
    input("Presione enter para continuar")

def sistemaMinisuper(subProgramIsRunning):
    while subProgramIsRunning:
        os.system("cls" if os.name == "nt" else "clear")
        console.print("Bienvenido al sistema de Minisuper Castillo!")
        userSelection = inquirer.prompt(
            [
                inquirer.List("options",
                                      "Seleccione que desea realizar",
                                      [
                                          ("1) Canasta Basica", 1),
                                          ("2) Snacks", 2),
                                          ("3) Panaderia", 3),
                                          ("4) Cuidado y Hogar", 4),
                                          ("5) Belleza e Higiene", 5),
                                          ("6) Frutas y Verduras", 6),
                                          ("7) Carnes y Pesqueria", 7),
                                          ("8) Agregar al Carrito", 8),
                                          ("9) Aplicar descuento", 9),
                                          ("10) Proceder al pago", 10),
                                          ("0) Salir", 0)
                                      ]),
            ]
        )
        
        seleccion = userSelection['options']

        if(seleccion == 0):
            subProgramIsRunning = False
            break
        elif (seleccion == 1):
            imprimirProductos("Canasta Basica", inventario['canasta_basica'])
        elif (seleccion == 2):
            imprimirProductos("Snacks", inventario['Snacks'])
        elif (seleccion == 3):
            imprimirProductos("Panaderia", inventario['Panaderia'])
        elif (seleccion == 4):
            imprimirProductos("Cuidado y Hogar", inventario['Cuidado_Hogar'])
        elif (seleccion == 5):
            imprimirProductos("Belleza e Higiene", inventario['Belleza_Higiene'])
        elif (seleccion == 6):
            imprimirProductos("Frutas y Verduras", inventario['Frutas_Verduras'])
        elif (seleccion == 7):
            imprimirProductos("Carnes y Pesqueria", inventario['Carnes_Pesqueria'])
        elif (seleccion == 8):
            agregarAlCarrito()
        elif (seleccion == 9):
            agregarDescuento()
        else:
            procederAlPago()