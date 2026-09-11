import os
import sys

# Jalur aman penemu folder modul
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import DB Helper
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat

# Import dari modul-modul temenmu
from hitung_geometri import *
from cek_sifat_angka import *

user_aktif = None

def portal_akses():
    global user_aktif
    while True:
        print("\n----------------------------------------")
        print("    SYSTEM PORTAL (LOGIN / REGISTER)    ")
        print("----------------------------------------")
        print("1. Login Akun")
        print("2. Registrasi Akun Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            print("\n--- LOGIN AKUN ---")
            identifier = input("Email / Username : ")
            pwd = input("Password         : ")
            status, username_res, pesan = login_user(identifier, pwd)
            print(f"-> {pesan}")
            if status:
                user_aktif = username_res
                break
                
        elif pilihan == "2":
            print("\n--- REGISTRASI AKUN BARU ---")
            email = input("Email Baru    : ")
            uname = input("Username Baru : ")
            pwd = input("Password Baru : ")
            status, pesan = daftar_user(email, uname, pwd)
            print(f"-> {pesan}")
            
        elif pilihan == "3":
            print("\nProgram dihentikan.")
            sys.exit()
        else:
            print("\nPilihan tidak valid.")

def main():
    portal_akses()
    
    while True:
        print("\n----------------------------------------")
        print(f"   PROGRAM KALKULATOR | Akun: {user_aktif.upper()}")
        print("----------------------------------------")
        print("1. Hitung Luas Persegi")
        print("2. Hitung Keliling Persegi")
        print("3. Cek Bilangan Prima")
        print("4. Cek Bilangan Genap / Ganjil")
        print("5. Hitung Luas Lingkaran")
        print("6. Hitung Luas Segitiga")
        print("7. Lihat Riwayat Tersimpan")
        print("8. Logout & Keluar")
        print("----------------------------------------")
        
        pilihan = input("Pilihan menu (1-8): ")
        
        if pilihan == "1":
            val = float(input("Masukkan panjang sisi: "))
            hasil = cari_luas_persegi(val)
            print(f"Hasil Luas Persegi: {hasil}")
            simpan_riwayat(user_aktif, "Luas Persegi", hasil)
            
        elif pilihan == "2":
            val = float(input("Masukkan panjang sisi: "))
            hasil = cari_keliling_persegi(val)
            print(f"Hasil Keliling Persegi: {hasil}")
            simpan_riwayat(user_aktif, "Keliling Persegi", hasil)
            
        elif pilihan == "3":
            num = int(input("Masukkan nilai angka: "))
            if pemeriksa_prima(num):
                print(f"Angka {num} adalah Bilangan Prima")
                simpan_riwayat(user_aktif, "Cek Prima", f"{num} (Bilangan Prima)")
            else:
                print(f"Angka {num} Bukan Bilangan Prima")
                simpan_riwayat(user_aktif, "Cek Prima", f"{num} (Bukan Prima)")
                
        elif pilihan == "4":
            num = int(input("Masukkan nilai angka: "))
            res = pemeriksa_genap_ganjil(num)
            print(f"Angka {num} tergolong Bilangan {res}")
            simpan_riwayat(user_aktif, "Ganjil Genap", f"{num} ({res})")
                
        elif pilihan == "5":
            r = float(input("Masukkan jari-jari lingkaran: "))
            hasil = cari_luas_lingkaran(r)
            print(f"Hasil Luas Lingkaran: {hasil}")
            simpan_riwayat(user_aktif, "Luas Lingkaran", hasil)

        elif pilihan == "6":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))
            hasil = cari_luas_segitiga(a, t)
            print(f"Hasil Luas Segitiga: {hasil}")
            simpan_riwayat(user_aktif, "Luas Segitiga", hasil)
            
        elif pilihan == "7":
            print(f"\n--- RIWAYAT TERSIMPAN [{user_aktif}] ---")
            print(lihat_riwayat(user_aktif))

        elif pilihan == "8":
            print(f"\nLogout dari akun {user_aktif}. Terima kasih!")
            break
        else:
            print("Input tidak valid, coba masukkan angka 1-8!")

if __name__ == "__main__":
    main()
