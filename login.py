USERNAME = "fafdal@gmail.com"
PW = "trit mi like adit"

username = input("Masukan username: ")
pw = input("masukan pw: ")


if username != USERNAME:
    print("username tidak tersedia")
elif username == USERNAME and pw != PW:
    print("pw salah bang")

else:
    print("Selamat datang",username)


