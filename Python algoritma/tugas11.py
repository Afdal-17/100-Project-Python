def jenis_segitiga(a,b,c):
    a,b,c = sorted([a,b,c])

    if a**2 + b**2 == c**2:
        print("Segitiga siku siku")
    elif a**2 + b**2 > c**2:
        print("Segitiga Lancip")
    else:
        print("Segitiga Tumpul")

    
a = int(input("masukan panjang sisi a:"))
b = int(input("masukan panjang sisi b:"))
c = int(input("masukan panjang sisi c:"))

jenis = jenis_segitiga(a,b,c)
print(jenis)