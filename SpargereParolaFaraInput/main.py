output = open("output", "rb")
textBinar = output.read()
output.close()

for lungimeCheie in range(10,16):
    possiblePassword = ""
    for caracter in range(lungimeCheie):
        frecventa = {}
        for i in range(caracter, len(textBinar), lungimeCheie):
            if textBinar[i] in frecventa:
                frecventa[textBinar[i]] += 1
            else:
                frecventa[textBinar[i]] = 1
        maxim = -1
        pozMaxim = -1
        for key in frecventa:
            if frecventa[key] > maxim:
                maxim = frecventa[key]
                pozMaxim = key
        possiblePassword = possiblePassword + chr(pozMaxim ^ ord(' '))
    print(possiblePassword)