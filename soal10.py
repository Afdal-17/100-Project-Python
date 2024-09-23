harga_barang1 = 55000
harga_barang2 = 40000

barang1 = int(input("Masukan jumlah barang 1: "))
barang2 = int(input("Masukan jumlah barang 2: "))

ttl1 = harga_barang1*barang1
ttl2 = harga_barang2*barang2
ttl_barang = ttl1+ttl2

if ttl_barang >= 100:
    diskon = ttl_barang*5/100
    bayar = ttl_barang-diskon

print(f'''Total harga barang: {ttl_barang}
Diskon: {diskon}
total yang harus dibayar: {bayar}Rp''')







