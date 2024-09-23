print("===========================")
print("     PROGRAM TABUNG        ")
print("===========================")

r = float(input("Masukan jari jari: "))
t = float(input("Masukan tinggi tabung: "))
phi = 3.14
v = phi*r*r*t
lp = (2*phi*r*t) + (phi*r*r)

print("Volume: ",v)
print("Luas permukaan: ",lp)