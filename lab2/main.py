#1
def nr_repeat(l1):
    no_duplicate = list(dict.fromkeys(l1))
#transforma intrun dict fara duplicate
    return no_duplicate
l1 = [24,76,67,42,76]
k = nr_repeat(l1)
print(k)




#2
def pair(l1):
    contor = 0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if int(l1[i] % 10) == int(l1[j] / 10) and int(l1[i] / 10) == int(l1[j] % 10):
                contor += 1
		#compara ultima cifra din primul cu prima din al doilea
		#si viceversa
    return contor
m = pair(l1)
print(m)




#3
def concat(l1):
    nr = []
    while len(l1) != 0:
        max_loc = 0
        for i in range(len(l1)):
            if l1[i] > max_loc:
                max_loc = l1[i]
                icop = i #pozitia max
        nr = str(nr) + str(max_loc)
        del l1[icop] #strege de pe poz max
    return nr[2:]
l1 = [12,45,98,18]
print(concat(l1))


#4
def code(meth,l):
    crypt_l = []
    if meth == '+':
        for el in l:
            crypt_l.append(el + l[0])
    if meth == '*':
        for el in l:
            crypt_l.append(el * l[0])
    if meth == 'XOR':
        for el in l:
            crypt_l.append(el ^ l[0])
    return crypt_l
l = [7, 2, 3, 4] #apelam functia
k = code('XOR', l)
print(k)




#5
def relatie():
    x = [3 , 6 , 7 , 8 , 17 , 2 ]
    for i in range (len (x)-1):
        for j in range (i+1,len(x)):
            if x[i] < x[j]:
                if x[j] % x[i] == 0 :
                    print(x[i], x[j])
            elif( x[i]>=x[j]):
                if x[i] % x[j] == 0 :
                    print(x[i],x[j])

relatie()




#6
def Domino(l):
    secv_curenta = []
    secv_maxima = []
    for i in range(1, len(l)):
        if l[i-1] % 10 == l[i] // 10: #daca ult cif dintrun numar = prima din urm
            if secv_curenta == []:
                secv_curenta.append(l[i-1])
            secv_curenta.append(l[i])
        else:
            len(secv_curenta) > len(secv_maxima) #determ secv max
            secv_maxima = secv_curenta
            secv_curenta = []
        if len(secv_curenta) > len(secv_maxima): #in cazul in care secv max contine ult el
            secv_maxima = secv_curenta
    return secv_maxima

l = [67,78,83,31,12,59]
k = Domino(l)
print(k)



#7
def ggt(a, b):
    while b != 0:
        rest = a % b  # calculam restul lui a/b
        a = b         # transf a in b
        b = rest      # transf b in rest

    return a  # ggt

def kgv(a, b):
    return a * b // ggt(a, b)# impartim produsul la ggt

n1 = 12
n2 = 24
erg = kgv(n1, n2)
print(erg)