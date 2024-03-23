lista_compras = []

productos = input("Ingrese el nombre del producto (o 'terminar' para finalizar): ")
while productos != "terminar": 
    
    lista_compras.append(productos)
    productos = input("Ingrese el nombre del producto (o 'terminar' para finalizar): ")

print("Lista de compra:")
for productos in lista_compras:
    print(productos)
