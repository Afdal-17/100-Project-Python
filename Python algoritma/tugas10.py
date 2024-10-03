angka1 = int(input("Masukan angka 1:"))
angka2 = int(input("Masukan angka 2:"))
angka3 = int(input("Masukan angka 3:"))

if angka1 > angka2:
    angka1, angka2 = angka2, angka1
if angka1 > angka3:
    angka1, angka3 = angka3, angka1
if angka2 > angka3:
    angka2, angka3 = angka3, angka2

print(f"angka terkecil {angka1},{angka2},{angka3}")