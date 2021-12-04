output = open("output", "rb")
input = open("input.txt", "r")

binaryList = output.read()
textInitial = input.read()

for i in range(100):
    print(chr(binaryList[i] ^ ord(textInitial[i])), end="")
