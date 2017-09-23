articulos = ['zapatos', 'camisa', 'abrigo']
precios = [50, 15, 70]

for i in range(len(articulos)):
    print("Precio de ", articulos[i], " = ", precios[i])

for art, price in zip(articulos, precios):
    print("Precio de ", art, " = ", price)
