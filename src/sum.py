sumcars = 0
sumwords = 0

for word in ['hola', 'a', 'todos']:
    print("Frase: ", word)
    sumcars += len(word)
    sumwords += 1

print("Se han mostrado ", sumwords, " palabras y ", sumcars, " caracteres")
