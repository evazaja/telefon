def file_kiir_2lista(lista_1, lista_2):
    f = open("percek.txt", "w")

    for i in range(0, len(lista_1)):
        ora = int(lista_1[i][3]) - int(lista_1[i][0])
        perc = int(lista_1[i][4]) - int(lista_1[i][1])
        mp = int(lista_1[i][5]) - int(lista_1[i][2])
        nagyobb = 0
        time = 0

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

        f.write(str(int(time))+' '+str(lista_2[i])+'\n')
    f.close()