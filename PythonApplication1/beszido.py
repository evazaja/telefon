def beszido():
    kezd_ora = int(input("Add meg a kezdeti órát: "))
    kezd_perc = int(input("Add meg a kezdeti percet: "))
    kezd_mp = int(input("Add meg a kezdeti másodpercet: "))

    print("")

    veg_ora = int(input("Add meg a befejezési órát: "))
    veg_perc = int(input("Add meg a befejezési percet: "))
    veg_mp = int(input("Add meg a befejezési másodpercet: "))

    print("")

    ora = veg_ora - kezd_ora
    perc = veg_perc - kezd_perc
    mp = veg_mp - kezd_mp

    if (ora == 0 and mp == 0):
        print(str(perc)+" percig tartott a hívás.")
    if (ora < 0):
        ora = (24 - kezd_ora) + veg_ora
    if (perc < 0):
        perc = (60 - kezd_perc) + veg_perc
    if (mp < 0):
        mp = (60 - kezd_mp) + veg_mp


    print("")
    print("A beszélgetett idő: "+str(ora)+":"+str(perc-1)+":"+str(mp))
    print("A számlázás szempontjából "+str(int(perc + (mp/60) + (ora*60)))+" perces volt a beszélgetés.")

