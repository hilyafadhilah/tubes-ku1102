# -----------------------------------------------------------
# main.py
#
# Tugas Besar Mata Kuliah Pengenalan Komputasi KU1102
# Simulasi Sistem Smart Microwave Oven
#
# Oleh: Kelompok 6 - K22
# 16520148 Rd. Elviana La'salina Muhlis
# 16520168 Joyata Pirma P Sitanggang
# 16520298 Gibran Darmawan
# 16520488 Hilya Fadhilah Imania
#
# Semester Ganjil TPB 2020
#
# (C) 2020 Hilya Imania, Gibran Darmawan,
# Joyata Sitanggang, and Rd. Elviana Muhlis
# Jakarta, Indonesia
# Released under MIT License (MIT)
# -----------------------------------------------------------
# Program main.py
#
# Spesifikasi
#   Menyimulasikan sistem kerja smart microwave oven dengan
#   unit-unit yang terdekomposisinya.
#
# Deskripsi
#   Sistem ini telah disimplifikasi sehingga pengguna tidak
#   bisa melakukan input dengan urutan yang berbeda atau input
#   di saat bersamaan. Selain itu benda yang dimasukkan ke
#   dalam microwave bisa apa saja dan tidak akan terjadi error
#   seperti ledakan microwave.
#
# Prosedur
#   main() : sistem pemanasan microwave secara garis besar
#   run() : subsistem untuk melakukan pemanasan
#
# Modul
#   ./unit.py : unit-unit penyusun sistem microwave
# -----------------------------------------------------------

# -----------------------------------------------------------
# 01: Inisialisasi (modul, library, dependency)
# -----------------------------------------------------------

# Modul ./unit.py
#   Terdiri atas prosedur-prosedur untuk menggunakan unit-unit
#   di dalam microwave
# Prosedur yang digunakan
#   {void}      buka_pintu()
#   {void}      tutup_pintu()
#   {void}      switch_lampu(state =boolean)
#   {string}    input_makanan()
#   {void}      switch_makanan(state =boolean, food =string)
#   {void}      print_modes(modes =array)
#   {string}    input_mode(modes =array)
#   {int}       input_durasi()
#   {void}      switch_magnetron(state =boolean)
#   {void}      switch_kipas(state =boolean)
#   {void}      heat(durasi =int)
#   {void}      beep()
#   {boolean}   pop_makanan(food =string)
import unit

# -----------------------------------------------------------
# 02: Rangka program (deklarasi prosedur)
# -----------------------------------------------------------

# Prosedur run()
#   Subsistem proses pemanasan yang mengaktifkan dan
#   mendeaktifkan unit-unit yang berkaitan
# Parameter
#   {int} mode : index mode pemanasan yang dipilih
#   {int} durasi : durasi pemanasan dalam detik
# Algoritma
#   1) Nyalakan lampu microwave
#   2) Nyalakan magnetron sesuai mode yang diminta
#   3) Nyalakan guide fan
#   4) Tunggu sesuai durasi yang diminta
#   5) Matikan guide fan
#   6) Matikan magnetron
#   7) Matikan lampu microwave
def run(mode, durasi):
    unit.switch_lampu(True)
    unit.switch_magnetron(True)
    unit.switch_kipas(True)
    unit.heat(durasi)
    unit.switch_kipas(False)
    unit.switch_magnetron(False)
    unit.switch_lampu(False)

# Prosedur main()
#   Sistem utama yang mengatur jalannya simulasi microwave mulai
#   dari input, proses, dan output. Sistem ini akan terus menunggu
#   menunggu input dari pengguna dan akan berjalan selamanya,
#   yakni sampai program dihentikan secara eksternal (di luar
#   prosedur main).
# Kamus
#   {array}     modes
#   {string}    food
#   {boolean}   is_makanan_inside
#   {int}       mode
#   {int}       durasi
# Algoritma
#   1)  Tentukan nama dan konfigurasi mode-mode pemanasan
#       microwave yang didukung oleh simulasi
#   2)  Tunggu pengguna membuka pintu
#   3)  Nyalakan lampu
#   4)  Persilakan pengguna memasukkan makanan
#   5)  Tunggu pengguna menutup pintu
#   6)  Pengguna memasukkan mode pemanasan sesuai yang tersedia
#   7)  Pengguna memasukkan durasi pemanasan
#   8)  Lakukan pemanasan sesuai mode dan durasi
#   9)  Nyalakan alarm
#   10) Tunggu pengguna membuka pintu
#   11) Jika pengguna memilih mengeluarkan makanan:
#       a) Tunggu pengguna menutup pintu
#       b) Kembali ke nomor (2)
#       Jika pengguna tidak mengeluarkan makanan:
#       c) Tunggu pengguna menutup pintu
#       d) Kembali ke nomor (6)
def main():
    # (1)
    modes = ['micro', 'grill', 'defrost', 'popcorn']

    # (2) - (11), terus berulang
    while True:
        unit.buka_pintu()
        unit.switch_lampu(True)

        food = unit.input_makanan()

        unit.switch_makanan(True, food=food)
        unit.tutup_pintu()
        unit.switch_lampu(False)

        # (6) - (12), terus berulang selama pengguna
        # tidak mengeluarkan makanan dari microwave
        is_makanan_inside = True
        while is_makanan_inside:
            unit.print_modes(modes)

            mode = unit.input_mode(modes)
            durasi = unit.input_durasi()

            run(mode, durasi)
            
            unit.beep()
            unit.buka_pintu()

            if unit.pop_makanan(food):
                unit.switch_makanan(False, food=food)
                is_makanan_inside = False
            unit.tutup_pintu()

# Prosedur welcome()
#   Menampilkan pesan pembuka
def welcome():
    unit.print_delay('Simulasi Microwave Oven')
    unit.print_delay('Tekan Ctrl+C untuk menghentikan program.')

# Prosedur goodbye()
#   Menampilkan pesan penutup
def goodbye():
    unit.print_delay('\nSimulasi dihentikan.')
    unit.print_delay('Selamat tinggal!')

# -----------------------------------------------------------
# 03: Jantung program
#
# Algoritma
#   1) Tunjukkan pesan pengantar
#   2) Jalankan simulasi microwave, yang tak hingga
#   3) Jika pengguna melakukan KeyboardInterrupt (Ctrl+C),
#       tunjukkan pesan penutup dan akhiri program
# -----------------------------------------------------------

try:
    welcome()
    main()
except KeyboardInterrupt:
    goodbye()
    pass
