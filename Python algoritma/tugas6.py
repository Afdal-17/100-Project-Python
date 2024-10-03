nilai = int(input("Masukan nlai: "))

if nilai > 80:
    indeks = "A"
elif (nilai > 70) and (nilai < 80):
    indeks = "B"
elif (nilai > 55) and (nilai < 70):
    indeks = "C"
elif (nilai > 40) and (nilai < 55):
    indeks = "D"
else:
    indeks = "E"

print("indeks: ",indeks)