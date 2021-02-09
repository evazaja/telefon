def csucsido(lista_1):
    csucskezd = 7
    csucsveg = 18
    csucsonbelul = 0
    csucsonkivul = 0

    for i in range(0, len(lista_1)):
        if(int(lista_1[i][0]) >= csucskezd and int(lista_1[i][0]) < csucsveg):
            csucsonbelul = csucsonbelul + 1
        else:
            csucsonkivul = csucsonkivul + 1

    print("")
    print("Csúcsidőn belüli hívások: "+str(csucsonbelul)+" db")
    print("Csúcsidőn kívüli hívások: "+str(csucsonkivul)+" db")
