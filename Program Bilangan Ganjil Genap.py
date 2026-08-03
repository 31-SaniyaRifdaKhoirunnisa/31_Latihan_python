# Input bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

# Logika Modulus (sisa pembagian dengan 2)
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan GENAP")
else:
    print(f"{bilangan} adalah bilangan GANJIL")