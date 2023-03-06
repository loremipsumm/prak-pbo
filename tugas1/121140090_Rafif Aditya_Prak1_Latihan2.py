username = "informatika"
password = "12345678"

i = 0
batas = 3

while (i<batas):
    id = input("Username anda :")
    pw = input("password anda :")

    if(id == username and pw == password):
        print("Berhasil login!")
        break
    elif(i==2):
        print("Anda sudah melakukan 3x percobaan, akses anda kami blokir")
        break
    else:
        print("Username atau password salah coba lagi")
        i += 1
        print("Tersisa ", batas-i, " percobaan lagi")

