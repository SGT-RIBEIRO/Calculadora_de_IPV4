def Conversao_Binario(num):
    binario = []
    num = num
    sub = 128
    while sub >= 1:
        if num < sub:
            binario.append(0)
            sub = sub / 2
        else:
            binario.append(1)
            num = num - sub
            sub = sub / 2
    return binario
rede = []
NumRede = list(input('Digite o numero da rede: [utilize os pontos e a barra final ao digitar o IP]\n'))
NumRedeSb = 0
bits = 0
if NumRede[-2] == '/':
    NumRedeSb = NumRede[:-2]
    bits = NumRede[-1]
else:
    NumRedeSb = NumRede[:-3]
    bits = NumRede[-2] + NumRede[-1]
CalcBits = (32 - int(bits))
NumRedeSP = []
Ip_Valido = 2**CalcBits - 2
cont = 1
indice = 0
while cont <= int(len(NumRedeSb)):
    nuns = ''
    for i in range(0, int(len(NumRedeSb))+1):
        if NumRedeSb[indice] != ".":
            nuns = (nuns + NumRedeSb[indice]).strip()
            indice += 1
            cont += 1
            if indice > int(len(NumRedeSb)-1):
                break
        else:
            break
    NumRedeSP.append(nuns)
    indice += 1
    cont += 1

Octeto1 = Conversao_Binario(int(NumRedeSP[0]))
Octeto2 = Conversao_Binario(int(NumRedeSP[1]))
Octeto3 = Conversao_Binario(int(NumRedeSP[2]))
Octeto4 = Conversao_Binario(int(NumRedeSP[3]))
RedeBinario = Octeto1 + Octeto2 + Octeto3 + Octeto4

c = 0
RedeMascara = []
while c < 32:
    if c < int(bits):
        RedeMascara.append(1)
    else:
        RedeMascara.append(0)
    c += 1
bitsDisponiveis = RedeMascara.count(0)
Mascara = 128
redeMascarasoma = []
if bitsDisponiveis == 8:
    Mascara = '255.255.255.0'
elif bitsDisponiveis < 8:
    us = 8 - int(bitsDisponiveis)
    while True:
        redeMascarasoma.append(Mascara)
        Mascara /= 2
        us -= 1
        if us == 0:
            break
    m1 = int(sum(redeMascarasoma))
    Mascara = '255.255.255.'+str(m1)
elif bitsDisponiveis == 16:
    Mascara = '255.255.0.0'
elif bitsDisponiveis < 16 and bitsDisponiveis > 8:
    us = 16 - int(bitsDisponiveis)
    while True:
        redeMascarasoma.append(Mascara)
        Mascara /= 2
        us -= 1
        if us == 0:
            break
    m2 = int(sum(redeMascarasoma))
    Mascara = '255.255.'+str(m2)+'.0'
elif bitsDisponiveis == 24:
    Mascara = '255.0.0.0'
elif bitsDisponiveis < 24 and bitsDisponiveis > 16:
    us = 24 - int(bitsDisponiveis)
    while True:
        redeMascarasoma.append(Mascara)
        Mascara /= 2
        us -= 1
        if us == 0:
            break
    m3 = int(sum(redeMascarasoma))
    Mascara = '255.'+str(m3)+'.0.0'
elif bitsDisponiveis == 32:
    Mascara = '0.0.0.0'
elif bitsDisponiveis < 32 and bitsDisponiveis > 24:
    us = 32 - int(bitsDisponiveis)
    while True:
        redeMascarasoma.append(Mascara)
        Mascara /= 2
        us -= 1
        if us == 0:
            break
    m4 = int(sum(redeMascarasoma))
    Mascara = str(m4)+'.0.0.0'

AndLogico = []

for c, binario in enumerate(RedeBinario):
    if binario == RedeMascara[c]:
        AndLogico.append(1)
    else:
        AndLogico.append(0)

Redeinicial = AndLogico[:-int(bitsDisponiveis)]
RedeFinal = AndLogico[:-int(bitsDisponiveis)]
for i in range(0, int(bitsDisponiveis)):
    Redeinicial.append(0)

for c in range(0, int(bitsDisponiveis)):
    RedeFinal.append(1)

redeI = []
redeIn = 0
r = 128
if bitsDisponiveis == 8:
    redeIn = NumRedeSP[0]+'.'+NumRedeSP[1]+'.'+NumRedeSP[2]+'.''0/'+bits
elif bitsDisponiveis < 8:
    d = 24
    r = 128
    while True:
        if d > 31:
            break
        else:
            if Redeinicial[d] == 1:
                redeI.append(r)
                r /= 2
                d += 1
            else:
                redeI.append(0)
                r /= 2
                d += 1
    a = int(sum(redeI))
    redeIn = NumRedeSP[0]+'.'+NumRedeSP[1]+'.'+NumRedeSP[2]+'.'+str(a)+'/'+bits
elif bitsDisponiveis == 16:
    redeIn = NumRedeSP[0]+'.'+NumRedeSP[1]+'.0.0/'+bits
elif bitsDisponiveis < 16:
    d = 16
    r = 128
    while True:
        if d > 23:
            break
        else:
            if Redeinicial[d] == 1:
                redeI.append(r)
                r /= 2
                d += 1
            else:
                redeI.append(0)
                r /= 2
                d += 1
    b1 = int(sum(redeI))
    redeIn = NumRedeSP[0] + '.' + NumRedeSP[1] + '.'+str(b1)+'.' + '0/' + bits
elif bitsDisponiveis == 24:
    redeIn = NumRedeSP[0] + '.0.0.0'
elif bitsDisponiveis < 24:
    d = 8
    r = 128
    while True:
        if d > 15:
            break
        else:
            if Redeinicial[d] == 1:
                redeI.append(r)
                r /= 2
                d += 1
            else:
                redeI.append(0)
                r /= 2
                d += 1
    c1 = int(sum(redeI))
    redeIn = NumRedeSP[0] + '.' +str(c1)+'.0.0/' + bits
elif bitsDisponiveis == 32:
    redeIn ='0.0.0.0'+bits
elif bitsDisponiveis < 32:
    d = 0
    r = 128
    while True:
        if d > 7:
            break
        else:
            if Redeinicial[d] == 1:
                redeI.append(r)
                r /= 2
                d += 1
            else:
                redeI.append(0)
                r /= 2
                d += 1

    d1 = sum(redeI)
    redeIn = str(d1) + '.0.0.0/' + bits

redeF1 = []
redeFim = 0
rf = 128
if bitsDisponiveis == 8:
    redeFim = NumRedeSP[0]+'.'+NumRedeSP[1]+'.'+NumRedeSP[2]+'.''255/'+bits
elif bitsDisponiveis < 8:
    df = 24
    rf = 128
    while True:
        if df > 31:
            break
        else:
            if RedeFinal[df] == 1:
                redeF1.append(rf)
                rf /= 2
                df += 1
            else:
                redeF1.append(0)
                rf /= 2
                df += 1
    af = int(sum(redeF1))
    redeFim = NumRedeSP[0]+'.'+NumRedeSP[1]+'.'+NumRedeSP[2]+'.'+str(af)+'/'+bits
elif bitsDisponiveis == 16:
    redeFim = NumRedeSP[0]+'.'+NumRedeSP[1]+'.255.255/'+bits
elif bitsDisponiveis < 16:
    df = 16
    rf = 128
    while True:
        if df > 23:
            break
        else:
            if RedeFinal[df] == 1:
                redeF1.append(rf)
                rf /= 2
                df += 1
            else:
                redeF1.append(0)
                rf /= 2
                df += 1

    b12 = int(sum(redeF1))
    redeFim = NumRedeSP[0] + '.' + NumRedeSP[1] + '.'+str(b12)+'.' + '255/' + bits
elif bitsDisponiveis == 24:
    redeFim = NumRedeSP[0] + '.255.255.255'
elif bitsDisponiveis < 24:
    df = 8
    rf = 128
    while True:
        if df > 15:
            break
        else:
            if RedeFinal[df] == 1:
                redeF1.append(rf)
                rf /= 2
                df += 1
            else:
                redeF1.append(0)
                rf /= 2
                df += 1

    c12 = int(sum(redeF1))
    redeFim = NumRedeSP[0] + '.' +str(c12)+'.255.255/' + bits
elif bitsDisponiveis == 32:
    redeFim ='255.255.255.255'+bits
elif bitsDisponiveis < 32:
    df = 0
    rf = 128
    while True:
        if df > 7:
            break
        else:
            if RedeFinal[df] == 1:
                redeF1.append(rf)
                rf /= 2
                df += 1
            else:
                redeF1.append(0)
                rf /= 2
                df += 1

    d12 = int(sum(redeF1))
    redeFim = str(d12) + '.255.255.255/' + bits
print()
print('O referido Endereço de rede tem as seguintes características:\n')
print('-=-'*11)
print(f'''Máscara de rede: {Mascara}
{'-=-'*11}
Ips Válidos: {Ip_Valido}
{'-=-'*11}
Rede Inicial: {redeIn}
{'-=-'*11}
Broadcast: {redeFim}
{'-=-'*11}''')






