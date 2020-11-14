# -----------------------------------------------------------
# unit.py
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
# (C) 2020 Hilya F. Imania, Gibran Darmawan,
# Joy P. Sitanggang, and Rd. Elviana L.
# Jakarta, Indonesia
# Released under MIT License (MIT)
# -----------------------------------------------------------
# Program unit.py
#
# Spesifikasi
#   Menyimulasikan kerja unit-unit yang mengomposisi microwave
#
# Deskripsi
#   Unit-unit yang didefinisikan yaitu:
#   - Tombol input mode dan durasi
#   - Mekanisme pintu
#   - Display melalui standard output
#   - Lampu microwave
#   - Mekanisme kamar/ruang makanan
#   - Magnetron (pemancar gelombang mikro)
#   - Guide stirring fan (kipas penyebar gelombang)
#   - Mekanisme pemanasan dalam durasi tertentu
#
# Modul
#   time : menggunakan sleep() sebagai delay output
# -----------------------------------------------------------

# -----------------------------------------------------------
# 01: Inisialisasi (modul, library, dependency)
# -----------------------------------------------------------

# Modul time
# Prosedur yang digunakan
#   {void} sleep(secs : float)
from time import sleep

# -----------------------------------------------------------
# 02: Jantung program (deklarasi prosedur)
# -----------------------------------------------------------

# Prosedur print_delay()
#   Menyimulasikan display dengan menggunakan standard output.
#   Terdapat penundaan untuk menunjukkan sekuensialnya program.
# Parameter
#   {string} text : Teks yang ingin ditampilkan
# Algoritma
#   1) Tunggu selama n detik
#   2) Output
def print_delay(text):
    sleep(0.5)
    print(text)

# Prosedur print_delay()
#   Menyimulasikan input dengan menggunakan standard input.
#   Terdapat penundaan untuk menunjukkan sekuensialnya program.
# Parameter
#   {string} prompt : Pertanyaan yang ingin ditampilkan
# Algoritma
#   1) Tunggu selama n detik
#   2) Input dengan menampilkan juga prompt
def input_delay(prompt):
    sleep(0.5)
    return input(prompt)

# Prosedur buka_pintu()
#   Menunggu pengguna membuka pintu. Sekuens program akan
#   terhenti sampai pengguna membuka pintu.
# Algoritma
#   1) Meminta input membuka pintu
#   2) Jika pengguna tidak memilih membuka pintu,
#       kembali ke nomor (1)
#   3) Jika pengguna memilih membuka pintu,
#       lanjutkan sekuens program
def buka_pintu():
    state = input_delay('Buka pintu? (n): ')
    while state != 'y':
        state = input_delay('Buka pintu? (n): ')
    print_delay('Pintu terbuka.')

# Prosedur buka_pintu()
#   Menunggu pengguna menutup pintu. Sekuens program akan
#   terhenti sampai pengguna menutup pintu.
# Algoritma
#   1) Meminta input menutup pintu
#   2) Jika pengguna tidak memilih menutup pintu,
#       kembali ke nomor (1)
#   3) Jika pengguna memilih menutup pintu,
#       lanjutkan sekuens program
def tutup_pintu():
    state = input_delay('Tutup pintu? (n): ')
    while state != 'y':
        state = input_delay('Tutup pintu? (n): ')
    print_delay('Pintu tertutup.')

# Prosedur switch_lampu()
#   Menyalakan atau mematikan lampu
# Parameter
#   {boolean} state : permintaan keadaan
# Algoritma
#   1) Jika state adalah True, nyalakan lampu
#       jika tidak, matikan lampu
def switch_lampu(state):
    if state:
        print_delay('Lampu menyala.')
    else:
        print_delay('Lampu mati.')

# Prosedur input_makanan()
#   Meminta pengguna memasukkan makanan ke ruang microwave.
#   Apapun makanannya diizinkan, termasuk makanan kosong.
# Return
#   {string} nama makanan
# Algoritma
#   1) Minta pengguna menginput nama makanan
def input_makanan():
    return input_delay('Masukkan makanan: ')

# Prosedur has_makanan()
#   Mengecek apakah makanan tersebut ada atau kosong.
# Parameter
#   {string} food : makanan
# Return
#   {boolean} keberadaan makanan
# Algoritma
#   1) Jika makanan bukan string kosong, return True
#       jika tidak, return False
def has_makanan(food):
    return (food != '' and not food.isspace())

# Prosedur switch_makanan()
#   Menyimulasikan memasukkan/mengeluarkan makanan dengan
#   memberikan feedback terhadap keberadaan makanan di dalam
#   ruang microwave
# Parameter
#   {boolean} state : permintaan keadaan (masukkan/keluarkan)
#   {string} food : makanan
# Algoritma
#   1) Jika makanan kosong, tunjukkan
#   2) Jika makanan tidak kosong, beri feedback
#       memasukkan/mengeluarkan
def switch_makanan(state, food):
    if not has_makanan(food):
        print_delay('Microwave kosong.')
    elif state:
        print_delay(food + ' telah dimasukkan ke dalam microwave.')
    else:
        print_delay(food + ' telah dikeluarkan dari microwave.')

# Prosedur pop_makanan()
#   Meminta pengguna mengeluarkan makanan dari dalam ruang microwave.
#   Tidak menunggu seperti mekanisme pintu.
# Parameter
#   {string} food : makanan
# Return
#   {boolean} apakah pada akhirnya ada makanan/tidak di dalam ruang
# Algoritma
#   1) Jika makanan tidak kosong, minta pengguna memilih untuk
#       memasukkan atau mengeluarkan
#   2) Jika makanan kosong, tunjukkan
def pop_makanan(food):
    if has_makanan(food):
        keluarkan = input_delay('Keluarkan ' + str(makanan) + '? (n) ')
        return (keluarkan == 'y')
    else:
        print_delay('Tidak ada makanan untuk dikeluarkan!')
        return True

# Prosedur print_modes()
#   Mengelist mode-mode yang didukung oleh microwave
# Parameter
#   {string[]} modes : nama mode-mode yang didukung
def print_modes(modes):
    print_delay(modes)

# Prosedur input_mode()
#   Meminta pengguna memasukkan mode, sesuai mode-mode yang
#   didukung oleh sistem. Sekuens program akan terhenti
#   sampai pengguna memasukkan mode yang valid.
# Parameter
#   {string[]} modes : nama mode-mode yang didukung
# Return
#   {int} index dari array modes yang dipilih
# Algoritma
#   1) Meminta masukan mode
#   2) Jika pengguna memilih mode yang tidak valid,
#       kembali ke nomor (1)
#   3) Jika pengguna memilih mode yang valid,
#       lanjutkan sekuens program
def input_mode(modes):
    mode = input_delay('Pilih mode: ')
    while not (mode in modes):
        print_delay('Mode tidak valid!')
        mode = input_delay('Pilih mode: ')
    print_delay('Menggunakan mode ' + mode)
    return modes.index(mode)

# Prosedur intpu_durasi()
#   Meminta pengguna memasukkan durasi pemanasan.
#   Sekuens program akan terhenti sampai pengguna
#   memasukkan durasi berupa angka positif.
# Return
#   {int} durasi pemanasan
# Algoritma
#   1) Meminta masukan durasi
#   2) Jika pengguna memasukkan durasi yang tidak valid,
#       kembali ke nomor (1)
#   3) Jika pengguna memasukkan durasi yang valid,
#       lanjutkan sekuens program
def input_durasi():
    durasi = input_delay('Masukkan durasi: ')
    while not durasi.isnumeric() or int(durasi) <= 0:
        print_delay('Durasi tidak valid!')
        durasi = input_delay('Masukkan durasi: ')
    print_delay('Memanaskan selama ' + durasi + ' detik')
    return int(durasi)

# Prosedur switch_magnetron()
#   Menyimulasikan pengaktifan/pendeaktifan magnetron
#   (pemancar gelombang)
#   @TODO kekuatan gelombang sesuai dengan mode yang dipilih
# Parameter
#   {boolean} state : permintaan keadaan (nyalakan/matikan)
#   {int} mode = -1 : index mode yang dipilih
def switch_magnetron(state, mode =-1):
    if state:
        print_delay('Magnetron menyala.')
    else:
        print_delay('Magnetron mati.')

# Prosedur switch_magnetron()
#   Menyimulasikan pengaktifan/pendeaktifan guide stirring fan
#   (pemancar gelombang)
# Parameter
#   {boolean} state : permintaan keadaan (nyalakan/matikan)
def switch_kipas(state):
    if state:
        print_delay('Kipas menyala.')
    else:
        print_delay('Kipas mati.')

# Prosedur heat()
#   Menyimulasikan proses pemanasan sesuai durasi yang diminta
# Parameter
#   {int} duration : durasi pemanasan dalam detik
# Algoritma
#   1) Inisialisasi
#   2) Tampilkan waktu yang tersisa (dalam detik)
#   3) Beri jeda satu detik
#   4) Jika pengguna menggagalkan proses, lanjut ke no. (4)
#   5) Jika waktu belum habis, kembali ke no. (1)
#   6) Finishing
def heat(duration):
    print_delay('Mulai memanaskan...')
    print_delay('Tekan Ctrl+C untuk menghentikan pemanasan.')
    try:
        for i in range(durasi, -1, -1):
            if i > 0:
                print_delay(str(i) + ' s')
                sleep(1)
        pass
    except KeyboardInterrupt:
        print_delay('Pemanasan dihentikan.')
        pass
    print_delay('Selesai memanaskan...')

# Prosedur beep()
#   Menyimulasikan alarm microwave
def beep():
    print_delay('BEEP!')
