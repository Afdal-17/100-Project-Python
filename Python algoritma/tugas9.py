PS_X = 15/100

h_sayur = 20000
h_buah = 15000
h_ikan = 35000
h_bunga = 25000


sayur = int(input("Masukan sayur: "))
buah = int(input("Masukan buah: "))
ikan = int(input("Masukan ikan: "))
bunga = int(input("Masukan bunga: "))

ttl_sayur = h_sayur*sayur
ttl_buah = h_buah*buah
ttl_ikan = h_ikan*ikan
ttl_bunga = h_bunga*bunga
total_belanja = ttl_sayur+ttl_buah+ttl_ikan+ttl_bunga

if total_belanja >= 100000:
    diskon = total_belanja*PS_X
    harga_belanja = total_belanja-diskon
else:
    print("tidak dapat diskon")
print("total:",total_belanja)
print("diskon:",diskon)
print("harga belanja: ",harga_belanja)
    
