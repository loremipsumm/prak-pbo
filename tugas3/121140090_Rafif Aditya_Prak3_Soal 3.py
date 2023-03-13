class Latihan3:
    
    header = "Profil Data Karyawan Perusahaan PT. RB Sejahtera"
    
    def __init__(self, karyawan, gaji, jabatan):
        self.__karyawan = karyawan
        self._gaji = gaji
        self.jabatan = jabatan
        self.bonus = 0
        
    @classmethod
    def header_perusahaan(cls):
        print(cls.header)
    
    def bonus_gaji(self):
        if self.jabatan == "Junior":
            self.bonus = 0.1 * self._gaji
        elif self.jabatan == "Middle":
            self.bonus = 0.2 * self._gaji
        elif self.jabatan == "Senior":
            self.bonus = 0.3 * self._gaji
        else:
            self.bonus = 0
    
    def gaji_tambah_bonus(self):
        return self._gaji + self.bonus
    
    def __pajak(self):
        return self.gaji_tambah_bonus() * 0.15
    
    def gaji_bersih(self):
        return self.gaji_tambah_bonus() - self.__pajak()
    
    def profil(self):
        self.bonus_gaji()
        print(f"Nama        : {self.__karyawan}")
        print(f"Jabatan     : {self.jabatan} Programmer")
        print(f"Gaji Kotor  : {self._gaji}")
        print(f"Bonus Gaji  : {self.bonus}")
        print(f"Pajak       : {self.__pajak()}")
        print(f"Gaji Bersih : {self.gaji_bersih()}")   

        
Test = Latihan3("Rafif Aditya", 3500000, "Junior")
Test.header_perusahaan()
Test.profil()