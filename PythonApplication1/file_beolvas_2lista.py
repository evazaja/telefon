def file_beolvas_2lista(lista_1, lista_2):
    f = open("hivasok.txt")
    for i in f:
        lista_1.append(i.strip().split(' '))
        lista_2.append(str(f.readline()))
    f.close()
