import math

# === FUNGSI LOGIKA & PERHITUNGAN ===
def cari_luas_persegi(sisi):
    return sisi * sisi

def cari_keliling_persegi(sisi):
    return 4 * sisi

def pemeriksa_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pemeriksa_genap_ganjil(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def cari_luas_lingkaran(r):
    return 3.14 * r * r

def cari_luas_segitiga(a, t):
    return 0.5 * a * t


# === MENU UTAMA PROGRAM ===
while True:
    print("\n----------------------------------------")
    print("     PROGRAM KALKULATOR & LOGIKA       ")
    print("----------------------------------------")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("----------------------------------------")
    
    pilihan = input("Pilihan menu (1-7): ")
    
    if pilihan == "1":
        val = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Luas Persegi: {cari_luas_persegi(val)}")
        
    elif pilihan == "2":
        val = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Keliling Persegi: {cari_keliling_persegi(val)}")
        
    elif pilihan == "3":
        num = int(input("Masukkan nilai angka: "))
        if pemeriksa_prima(num):
            print(f"Angka {num} adalah Bilangan Prima")
        else:
            print(f"Angka {num} Bukan Bilangan Prima")
            
    elif pilihan == "4":
        num = int(input("Masukkan nilai angka: "))
        print(f"Angka {num} tergolong Bilangan {pemeriksa_genap_ganjil(num)}")
            
    elif pilihan == "5":
        r = float(input("Masukkan jari-jari lingkaran: "))
        print(f"Hasil Luas Lingkaran: {cari_luas_lingkaran(r)}")

    elif pilihan == "6":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga: {cari_luas_segitiga(a, t)}")
        
    elif pilihan == "7":
        print("Selesai, terima kasih!")
        break
    else:
        print("Input tidak valid, coba masukkan angka 1-7!")
