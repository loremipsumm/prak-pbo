import os

class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        os.system("cls")
        print("Selamat datang di Bank Tigo")
        print("Halo,", self.__nama_pelanggan, "Pilih menu yang Anda inginkan :")
        print("1. Cek saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Log Out")

    def lihat_saldo(self):
        os.system("cls")
        print("{} memiliki saldo Rp {}".format(self.__nama_pelanggan, self.__jumlah_saldo))
        input("\nTekan enter untuk kembali ke menu")

    def tarik_tunai(self):
        os.system("cls")
        nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")
        input("\nTekan enter untuk kembali ke menu")

    def transfer(self):
        os.system("cls")
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rekening = int(input("Masukkan no rekening tujuan: "))
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rekening:
                pelanggan.__jumlah_saldo += nominal
                self.__jumlah_saldo -= nominal
                print("Transfer Rp {} ke {} sukses!".format(nominal, pelanggan.__nama_pelanggan))
                input("\nTekan enter untuk kembali ke menu")
                return
        else:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama .")
            input("\nTekan enter untuk kembali ke menu")

    def main(self):
        while True:
            os.system("cls")
            self.lihat_menu()
            input_menu = int(input("Masukkan nomor input: "))
            if input_menu == 1:
                self.lihat_saldo()
            elif input_menu == 2:
                self.tarik_tunai()
            elif input_menu == 3:
                self.transfer()
            elif input_menu == 4:
                print("Terima kasih telah menggunakan layanan kami!")
                input("\nTekan enter untuk keluar")
                break

os.system("cls")
Akun1 = AkunBank(1234, "Rafif Aditya", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

while True:
    os.system("cls")
    nomor = int(input("Masukkan nomor pelanggan: "))
    for pelanggan in AkunBank.list_pelanggan:
        if pelanggan._AkunBank__no_pelanggan == nomor:
            pelanggan.main()
            break
    else:
        print("Nomor pelanggan tidak dikenal! Silakan coba lagi.")
    input("\nTekan enter untuk mencoba lagi")
