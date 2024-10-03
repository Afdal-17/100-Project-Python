nama = input("Masukan nama karyawan: ")
golongan = input("Masukan golongan kerja: ")
jjk = int(input("masukan jumlah jam kerja dalam seminggu: "))
UPAHLEMBUR = 3000
JKN = 48

if golongan == "A":
    upj = 4000
elif golongan == "B":
    upj = 5000
elif golongan == "C":
    upj = 6000
elif golongan == "D":
    upj = 7500

if jjk < JKN:
    upah_total = jjk*upj
else:
    jamlembur = jjk - JKN
    upah_total = JKN*upj+jamlembur*UPAHLEMBUR

print("Nama karyawan: ",nama)
print("Upah total: ",upah_total)

