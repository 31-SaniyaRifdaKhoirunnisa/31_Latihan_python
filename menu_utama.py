import tkinter as tk
from tkinter import messagebox, ttk
import sys

# Import helper & modul asli Nisa
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat
from hitung_geometri import *
from cek_sifat_angka import *

class GUINisa:
    def __init__(self, root):
        self.root = root
        self.root.title("System Portal & Kalkulator - Nisa")
        self.root.geometry("480x600")
        self.root.resizable(False, False)
        
        self.user_aktif = None
        self.tampilkan_halaman_akses()

    # ================= Halaman Login & Register =================
    def tampilkan_halaman_akses(self):
        self.bersihkan_layar()

        tk.Label(self.root, text="SYSTEM PORTAL", font=("Helvetica", 16, "bold"), fg="#2c3e50").pack(pady=15)

        # Tab Login & Register
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        # Frame Login
        frame_login = ttk.Frame(notebook)
        notebook.add(frame_login, text="Login Akun")

        tk.Label(frame_login, text="Email / Username :", font=("Helvetica", 10)).pack(anchor="w", padx=20, pady=(15, 2))
        ent_id = tk.Entry(frame_login, width=30)
        ent_id.pack(padx=20, pady=2)

        tk.Label(frame_login, text="Password :", font=("Helvetica", 10)).pack(anchor="w", padx=20, pady=(10, 2))
        ent_pwd = tk.Entry(frame_login, width=30, show="*")
        ent_pwd.pack(padx=20, pady=2)

        def aksi_login():
            identifier = ent_id.get().strip()
            pwd = ent_pwd.get().strip()
            if not identifier or not pwd:
                messagebox.showwarning("Peringatan", "Semua kolom login harus diisi!")
                return
            
            status, uname_res, pesan = login_user(identifier, pwd)
            if status:
                messagebox.showinfo("Sukses", pesan)
                self.user_aktif = uname_res
                self.tampilkan_kalkulator()
            else:
                messagebox.showerror("Gagal", pesan)

        tk.Button(frame_login, text="Login", bg="#27ae60", fg="white", font=("Helvetica", 10, "bold"), command=aksi_login).pack(pady=20)

        # Frame Register
        frame_reg = ttk.Frame(notebook)
        notebook.add(frame_reg, text="Registrasi Baru")

        tk.Label(frame_reg, text="Email Baru :", font=("Helvetica", 10)).pack(anchor="w", padx=20, pady=(10, 2))
        ent_reg_email = tk.Entry(frame_reg, width=30)
        ent_reg_email.pack(padx=20, pady=2)

        tk.Label(frame_reg, text="Username Baru :", font=("Helvetica", 10)).pack(anchor="w", padx=20, pady=(10, 2))
        ent_reg_uname = tk.Entry(frame_reg, width=30)
        ent_reg_uname.pack(padx=20, pady=2)

        tk.Label(frame_reg, text="Password Baru :", font=("Helvetica", 10)).pack(anchor="w", padx=20, pady=(10, 2))
        ent_reg_pwd = tk.Entry(frame_reg, width=30, show="*")
        ent_reg_pwd.pack(padx=20, pady=2)

        def aksi_register():
            email = ent_reg_email.get().strip()
            uname = ent_reg_uname.get().strip()
            pwd = ent_reg_pwd.get().strip()
            if not email or not uname or not pwd:
                messagebox.showwarning("Peringatan", "Semua kolom registrasi harus diisi!")
                return
            
            status, pesan = daftar_user(email, uname, pwd)
            if status:
                messagebox.showinfo("Sukses", pesan)
            else:
                messagebox.showerror("Gagal", pesan)

        tk.Button(frame_reg, text="Daftar Sekarang", bg="#2980b9", fg="white", font=("Helvetica", 10, "bold"), command=aksi_register).pack(pady=15)

    # ================= Halaman Utama Kalkulator =================
    def tampilkan_kalkulator(self):
        self.bersihkan_layar()

        # Header Info Akun
        header = tk.Frame(self.root, bg="#34495e")
        header.pack(fill="x", ipady=5)
        tk.Label(header, text=f"Akun Aktif: {self.user_aktif.upper()}", font=("Helvetica", 11, "bold"), fg="white", bg="#34495e").pack(side="left", padx=10)
        tk.Button(header, text="Logout", bg="#e74c3c", fg="white", font=("Helvetica", 9, "bold"), command=self.tampilkan_halaman_akses).pack(side="right", padx=10)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # TAB 1: Geometri
        f_geo = ttk.Frame(notebook)
        notebook.add(f_geo, text="Hitung Geometri")

        # Luas & Keliling Persegi
        tk.Label(f_geo, text="--- Persegi ---", font=("Helvetica", 10, "bold")).pack(pady=(10, 2))
        f_p = tk.Frame(f_geo)
        f_p.pack()
        tk.Label(f_p, text="Sisi: ").pack(side="left")
        ent_sisi = tk.Entry(f_p, width=10)
        ent_sisi.pack(side="left", padx=5)

        lbl_res_geo = tk.Label(f_geo, text="", font=("Helvetica", 9, "bold"), fg="#27ae60")

        def calc_luas_persegi():
            try:
                val = float(ent_sisi.get())
                hasil = cari_luas_persegi(val)
                lbl_res_geo.config(text=f"Luas Persegi: {hasil}")
                simpan_riwayat(self.user_aktif, "Luas Persegi", hasil)
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka valid!")

        def calc_kel_persegi():
            try:
                val = float(ent_sisi.get())
                hasil = cari_keliling_persegi(val)
                lbl_res_geo.config(text=f"Keliling Persegi: {hasil}")
                simpan_riwayat(self.user_aktif, "Keliling Persegi", hasil)
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka valid!")

        btn_fp = tk.Frame(f_geo)
        btn_fp.pack(pady=5)
        tk.Button(btn_fp, text="Luas", command=calc_luas_persegi).pack(side="left", padx=2)
        tk.Button(btn_fp, text="Keliling", command=calc_kel_persegi).pack(side="left", padx=2)

        # Lingkaran & Segitiga
        tk.Label(f_geo, text="--- Lingkaran & Segitiga ---", font=("Helvetica", 10, "bold")).pack(pady=(15, 2))
        f_ls = tk.Frame(f_geo)
        f_ls.pack()
        tk.Label(f_ls, text="Jari-jari (r): ").grid(row=0, column=0, sticky="w")
        ent_r = tk.Entry(f_ls, width=8)
        ent_r.grid(row=0, column=1, padx=2)

        tk.Label(f_ls, text="Alas: ").grid(row=1, column=0, sticky="w")
        ent_a = tk.Entry(f_ls, width=8)
        ent_a.grid(row=1, column=1, padx=2)

        tk.Label(f_ls, text="Tinggi: ").grid(row=1, column=2, sticky="w")
        ent_t = tk.Entry(f_ls, width=8)
        ent_t.grid(row=1, column=3, padx=2)

        def calc_luas_lingkaran():
            try:
                r = float(ent_r.get())
                hasil = cari_luas_lingkaran(r)
                lbl_res_geo.config(text=f"Luas Lingkaran: {hasil}")
                simpan_riwayat(self.user_aktif, "Luas Lingkaran", hasil)
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka valid!")

        def calc_luas_segitiga():
            try:
                a, t = float(ent_a.get()), float(ent_t.get())
                hasil = cari_luas_segitiga(a, t)
                lbl_res_geo.config(text=f"Luas Segitiga: {hasil}")
                simpan_riwayat(self.user_aktif, "Luas Segitiga", hasil)
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka valid!")

        btn_fls = tk.Frame(f_geo)
        btn_fls.pack(pady=5)
        tk.Button(btn_fls, text="Luas Lingkaran", command=calc_luas_lingkaran).pack(side="left", padx=2)
        tk.Button(btn_fls, text="Luas Segitiga", command=calc_luas_segitiga).pack(side="left", padx=2)
        lbl_res_geo.pack(pady=5)

        # TAB 2: Sifat Angka
        f_angka = ttk.Frame(notebook)
        notebook.add(f_angka, text="Sifat Angka")

        tk.Label(f_angka, text="Masukkan Nilai Angka:").pack(pady=10)
        ent_num = tk.Entry(f_angka)
        ent_num.pack()

        lbl_res_angka = tk.Label(f_angka, text="", font=("Helvetica", 10, "bold"), fg="#8e44ad")

        def calc_prima():
            try:
                num = int(ent_num.get())
                if pemeriksa_prima(num):
                    txt = f"Angka {num} adalah Bilangan Prima"
                    simpan_riwayat(self.user_aktif, "Cek Prima", f"{num} (Bilangan Prima)")
                else:
                    txt = f"Angka {num} Bukan Bilangan Prima"
                    simpan_riwayat(self.user_aktif, "Cek Prima", f"{num} (Bukan Prima)")
                lbl_res_angka.config(text=txt)
            except ValueError:
                messagebox.showerror("Error", "Masukkan bilangan bulat valid!")

        def calc_genap_ganjil():
            try:
                num = int(ent_num.get())
                res = pemeriksa_genap_ganjil(num)
                txt = f"Angka {num} tergolong Bilangan {res}"
                simpan_riwayat(self.user_aktif, "Ganjil Genap", f"{num} ({res})")
                lbl_res_angka.config(text=txt)
            except ValueError:
                messagebox.showerror("Error", "Masukkan bilangan bulat valid!")

        btn_fa = tk.Frame(f_angka)
        btn_fa.pack(pady=10)
        tk.Button(btn_fa, text="Cek Prima", command=calc_prima).pack(side="left", padx=5)
        tk.Button(btn_fa, text="Cek Genap/Ganjil", command=calc_genap_ganjil).pack(side="left", padx=5)
        lbl_res_angka.pack(pady=10)

        # TAB 3: Riwayat Google Sheet
        f_riwayat = ttk.Frame(notebook)
        notebook.add(f_riwayat, text="Riwayat Tersimpan")

        txt_riwayat = tk.Text(f_riwayat, height=15, width=50)
        txt_riwayat.pack(pady=10, padx=10)

        def muat_riwayat():
            txt_riwayat.delete("1.0", tk.END)
            data = lihat_riwayat(self.user_aktif)
            txt_riwayat.insert(tk.END, str(data))

        tk.Button(f_riwayat, text="Refresh Riwayat Google Sheets", bg="#2980b9", fg="white", command=muat_riwayat).pack(pady=5)

    def bersihkan_layar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUINisa(root)
    root.mainloop()
