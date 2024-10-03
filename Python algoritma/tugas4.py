print("\033[33m========SELAMAT DATANG DI KENZYSTORE==========")
harga_sigma = 5000
harga_rizz = 43000
harga_skibiditoilet = 95000
harga_mewing = 3000
harga_kaicenat = 55000

sigma = int(input("Masukan jumlah sigma yang ingin dibeli: "))
rizz = int(input("Masukan jumlah rizz yang ingin dibeli: "))
skibidi_toilet = int(input("Masukan jumlah Skibidi Toilet yang ingin dibeli: "))
mewing = int(input("Masukan jumlah mewing yang ingin dibeli: "))
kai_cenat = int(input("Masukan jumlah Kai Cenat yang ingin dibeli: "))

jml_s = harga_sigma*sigma
jml_r = harga_rizz*rizz
jml_sk = harga_skibiditoilet*skibidi_toilet
jml_m = harga_mewing*mewing
jml_k = harga_kaicenat*kai_cenat
total = jml_s+jml_r+jml_sk+jml_m+jml_k

if total>100:
    print("\033[31mAnda mendapat diskon: ",total*7.3/100)
    print("Sebelum diskon: ",total)

else:
    print("Tidak dapat diskon,silahkan bayar: ",total)
