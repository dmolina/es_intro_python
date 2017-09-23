articulos = ['zapatos', 'camisa', 'abrigo']
precios = [50, 15, 70]

for art, price in zip(articulos, precios):
    print("Precio de ", art, " = ", price)
