max_global = 0
while True:
    #introducem numere pana introducem -1 cand se termina programul
    #cand introducem 0 se reseteaza secventa, respectiv maximul local
    n = int(input("Zahl:"))
    max_local = 0
    if n == -1:
        break
    while True:
        n = int(input("Zahl1:"))
        if n > max_local:
            max_local = n
        if n == 0:
            break
    if max_local > max_global:
        max_global = max_local
    print("MAX_LOCAL:", max_local)
print("MAX_GLOBAL", max_global)






def interval(number, min_interval, max_interval):
    secv_curenta = []
    secv_maxima = []

    for nr in number:
        if min_interval <= nr <= max_interval:
            secv_curenta.append(nr)
        else:
            if len(secv_curenta) > len(secv_maxima):
                secv_maxima = secv_curenta
            secv_curenta = []

        if len(secv_curenta) > len(secv_maxima):
                secv_maxima = secv_curenta

    return secv_maxima
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30, 30]
min_interval = 6
max_interval = 40

secv_maxima = interval(number, min_interval, max_interval)
print("Langste secvenz:",secv_maxima)
