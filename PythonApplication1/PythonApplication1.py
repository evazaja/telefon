#modulok
import feladat_1
import beszido
import file_beolvas_2lista
import file_kiir_2lista
import csucsido
import beszido2
import fizet


ido = []
telszam = []

print("1_feladat")
feladat_1.feladat_1()
print("2_feladat")
beszido.beszido()
file_beolvas_2lista.file_beolvas_2lista(ido, telszam)
print("3_feladat")
print("percek.txt file-ba írás")
file_kiir_2lista.file_kiir_2lista(ido, telszam)
print("4_feladat")
csucsido.csucsido(ido)
print("5_feladat")
beszido2.beszido2(ido, telszam)
print("6_feladat")
fizet.fizet(ido, telszam)
