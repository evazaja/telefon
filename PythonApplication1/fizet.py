
def fizet(lista_1, lista_2):
    csucskezd = 7
    csucsveg = 18
    vezar = 30
    mobar = 69.175
    time = 0
    fizetendo = 0

    for i in range(0, len(lista_1)):
        ora = int(lista_1[i][3]) - int(lista_1[i][0])
        perc = int(lista_1[i][4]) - int(lista_1[i][1])
        mp = int(lista_1[i][5]) - int(lista_1[i][2])
        korzet_sz = lista_2[i][0]+lista_2[i][1]
        nagyobb = 0


        if (int(lista_1[i][5]) > int(lista_1[i][2])):
            nagyobb = 1
        if (ora < 0):
            ora = (24 - int(lista_1[i][0])) + int(lista_1[i][3])
        if (perc < 0):
            perc = (60 - int(lista_1[i][1])) + int(lista_1[i][4])
        if (mp < 0):
            mp = (60 - int(lista_1[i][2])) + int(lista_1[i][5])
        if (nagyobb == 1):
            time = perc + (mp/60) + (ora*60)+1
        else:
            time = perc + (mp/60) + (ora*60)

        if (korzet_sz == "39" or korzet_sz == "71" or korzet_sz == "41"):
            fizetendo = fizetendo + time * mobar
        else:
            fizetendo = fizetendo + time * vezar

    print("")
    print("A fizetendő összeg a csúcsidő alatt: "+str(int(fizetendo))+"Ft")

