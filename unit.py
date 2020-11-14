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

from time import sleep

def print_delay(text):
    sleep(0.5)
    print(text)

def input_delay(prompt):
    sleep(0.5)
    return input(prompt)

def welcome():
    print_delay('Simulasi Microwave Oven')
    print_delay('Tekan Ctrl+C untuk menghentikan program.')

def goodbye():
    print_delay('\nSimulasi dihentikan.')
    print_delay('Selamat tinggal!')

def buka_pintu():
    state = input_delay('Buka pintu? (n): ')
    while state != 'y':
        state = input_delay('Buka pintu? (n): ')
    print_delay('Pintu terbuka.')

def tutup_pintu():
    state = input_delay('Tutup pintu? (n): ')
    while state != 'y':
        state = input_delay('Tutup pintu? (n): ')
    print_delay('Pintu tertutup.')

def switch_lampu(state):
    if state:
        print_delay('Lampu menyala.')
    else:
        print_delay('Lampu mati.')

def input_makanan():
    return input_delay('Masukkan makanan: ')

def has_makanan(food):
    return (food != '' and not food.isspace())

def switch_makanan(state, food):
    if not has_makanan(food):
        print_delay('Microwave kosong.')
    elif state:
        print_delay(food + ' telah dimasukkan ke dalam microwave.')
    else:
        print_delay(food + ' telah dikeluarkan dari microwave.')

def pop_makanan(food):
    if has_makanan(food):
        keluarkan = input_delay('Keluarkan ' + str(makanan) + '? (n) ')
        return (keluarkan == 'y')
    else:
        print_delay('Tidak ada makanan untuk dikeluarkan!')
        return True

def print_modes(modes):
    print_delay(modes)

def input_mode(modes):
    mode = input_delay('Pilih mode: ')
    while not (mode in modes):
        print_delay('Mode tidak valid!')
        mode = input_delay('Pilih mode: ')
    print_delay('Menggunakan mode ' + mode)
    return modes.index(mode)

def input_durasi():
    durasi = input_delay('Masukkan durasi: ')
    while not durasi.isnumeric():
        print_delay('Durasi tidak valid!')
        durasi = input_delay('Masukkan durasi: ')
    print_delay('Memanaskan selama ' + durasi + ' detik')
    return int(durasi)

def switch_magnetron(state, mode =-1):
    if state:
        print_delay('Magnetron menyala.')
    else:
        print_delay('Magnetron mati.')

def switch_kipas(state):
    if state:
        print_delay('Kipas menyala.')
    else:
        print_delay('Kipas mati.')

def heat(durasi):
    print_delay('Mulai memanaskan...')
    print_delay('Tekan Ctrl+C untuk menghentikan pemanasan.')
    sleep(1)
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

def beep():
    print_delay('BEEP!')
