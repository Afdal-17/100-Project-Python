HARI_DETIK = 60*60*24
JAM_DETIK = 60*60
detik = int(input("detik: "))
hari = int(detik/HARI_DETIK)
detik = detik%HARI_DETIK
jam = int(detik/JAM_DETIK)
detik = detik%JAM_DETIK
menit = int(detik/60)
detik = detik%60

print(hari,"hari",jam,"jam",menit,"menit","dan",detik,"detik")
