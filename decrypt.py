import sys
def transformbyte(v):
    answer = 0
    for x in v:
        answer = answer * 2 + x
    return answer

opt = []
textread = []
textbin = []
passwordbin = []
val = 0
MOD = 94

nume_fisier_intrare = sys.argv[1]
password = sys.argv[2]
nume_fisier_iesire = sys.argv[3]

for i in range(0,len(password)):
    x = ord(password[i]) - 33
    val = val * MOD + x

while val > 0 :
    passwordbin.append(val % 2)
    val = val // 2

with open(nume_fisier_intrare,"rb") as f:
    textread = f.read()

for bit in textread :
    for i in range(7,-1,-1) :
        textbin.append((bit >> i) & 1)

lentext = len(textbin)
lenpass = len(passwordbin)

rest = lenpass - lentext % lenpass

for i in range(0,rest) :
    textbin.append(0)

for i in range(0,lentext,lenpass):
    for j in range(0, lenpass) :
        textbin[i + j] = textbin[i + j] ^ passwordbin[j]

for i in range(0,lentext ,8) :
    opt.append(chr(transformbyte(textbin[i:i+8])))

with open(nume_fisier_iesire,"w") as g:
    print(*opt, sep="", file = g)
