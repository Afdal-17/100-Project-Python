print("\033[78m==========SELAMAT DATANG DI TOKO ALAT TULIS===============")
harga_buku = 5000
harga_penghapus = 1000
harga_pulpen = 3000
harga_pensil = 2000
harga_penggaris = 3000
harga_penserut = 4000
harga_spidol = 2000

buku = int(input("Ingin membeli berapa buku?: "))
penghapus = int(input("Ingin membeli berapa penghapus?: "))
pulpen = int(input("Ingin membeli berapa pulpen?: "))
pensil = int(input("Ingin membeli berapa pensil?: "))
penggaris = int(input("Ingin membeli berapa penggaris?: "))
penserut = int(input("Ingin membeli berapa penserut?: "))
spidol = int(input("Ingin membeli berapa spidol?: "))

jml_buku = harga_buku*buku
jml_pnghapus = harga_penghapus*penghapus
jml_pulpen = harga_pulpen*pulpen
jml_pensil = harga_pensil*pensil
jml_penggaris = harga_penggaris*penggaris
jml_penserut = harga_penserut*penserut
jml_spidol = harga_spidol*spidol
total = jml_buku+jml_pnghapus+jml_pulpen+jml_pensil+jml_penggaris+jml_penserut+jml_spidol

diskon = total*12.5/100
jumlah = total-diskon

print("\033[34mJumlah: ",total)
print("Diskon: ",diskon)
print("Harus bayar: Rp",jumlah)