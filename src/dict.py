msg = {'es': 'Hola', 'en': 'Hello'}
lang = "es"

print(msg[lang])

for lang in msg:
    print("Idioma: '", lang,  "'", sep='')

print("Idiomas", msg.keys())

for lang in msg:
    print("Language[", lang, "]: ", msg[lang], sep='')
