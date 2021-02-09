def feladat_1():
    telszam1 = input("Add meg a telefonszámod: ")
    korzet_sz = telszam1[0] + telszam1[1]
    if (korzet_sz == "39" or korzet_sz == "71" or korzet_sz == "41"):
        print("A megadott szám mobil.")
    else:
        print("A megadott szám vezetékes.")
