class Rafif_Aditya:
    def __init__(self, nama, nim, prodi, kelas, semester, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelas = kelas
        self.semester = semester
        self.jumlah_sks = jumlah_sks
    
    def display_info(self):
        print(f"Nama       : {self.nama}")
        print(f"NIM        : {self.nim}")
        print(f"Prodi      : {self.prodi}")
        print(f"Kelas      : {self.kelas}")
        print(f"Semester   : {self.semester}")
        print(f"Jumlah SKS : {self.jumlah_sks}")

mahasiswa = Rafif_Aditya("Rafif Aditya", "121140090", "Teknik Informatika", "PBO RB", 3, 22)
mahasiswa.display_info()