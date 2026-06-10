def ficha_producto(nombre, precio, stock):
    print("===============================")
    print(f"Nombre del producto: {nombre}")
    print(f"Precio: {precio}")
    print(f"Stock: {stock}")
    print("===============================")

nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        stock = int(input("Ingrese el stock: "))
        if stock <= 0:
            print("Debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("Error: Debe ser números")

while True:
    try:
        precio = int(input("Ingrese el precio: "))
        if precio <= 0:
            print("Debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("Tiene que ser números")

ficha_producto(nombre, precio, stock)