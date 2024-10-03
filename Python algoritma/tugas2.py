barang1 = 20000
barang2 = 50000
barang3 = 40000
barang4 = 120000
barang = int(barang1+barang2+barang3+barang4)
total_belanja = barang

if barang >=200000:
    diskon = (barang*(7.5/100))

setelah_diskon = barang-diskon

print(f'''\033[35m          barang 1: {barang1}\r 
          barang 2: {barang2} 
          barang 3: {barang3} 
          barang 4: {barang4} 
          Total belanja: {barang}
          Diskon: {barang*7.5/100}
          Total bayar: {setelah_diskon}Rp''')
