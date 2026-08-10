# Input bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

# Logika Modulus (sisa pembagian dengan 2)
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan GENAP")
else:
    print(f"{bilangan} adalah bilangan GANJIL")
     # Inisialisasi variabel untuk mengontrol perulangan
    lanjut = "y"
    
    # Perulangan akan terus berjalan selama variabel lanjut bernilai 'y' atau 'Y'
    while lanjut.lower() == "y":
        # 1. Input bilangan dari pengguna
        bilangan = int(input("\nMasukkan sebuah bilangan: "))
    
        # 2. Logika Modulus (sisa pembagian dengan 2)
        if bilangan % 2 == 0:
            print(f"--> {bilangan} adalah bilangan GENAP")
        else:
            print(f"--> {bilangan} adalah bilangan GANJIL")
    
        # 3. Menanyakan apakah pengguna ingin mengulang atau keluar
        lanjut = input(
            "\nApakah ingin mengecek bilangan lain? (y/n untuk keluar): "
        )
    
    print("\nProgram selesai. Terima kasih!")