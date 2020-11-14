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

def switch_lampu(state):=
    if state:
        print_delay('Lampu menyala.')
    else:
        print_delay('Lampu mati.')

def input_makanan():
    return input_delay('Masukkan makanan: ')

def switch_makanan(state, name):=
    if name == '' or name.isspace():
        print_delay('Microwave kosong.')
    elif state:
        print_delay(name + ' telah dimasukkan ke dalam microwave.')
    else:
        print_delay(name + ' telah dikeluarkan dari microwave.')

def keluarkan_makanan(name):=
    keluarkan = input_delay('Keluarkan makanan? ')
    if keluarkan == 'y':
        return True
    else:
        return False

def print_mode(modes):
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

def switch_magnetron(state):
    if state:
        print_delay('Magnetron menyala.')
    else:
        print_delay('Magnetron mati.')

def switch_kipas(state):
    if state:
        print_delay('Kipas menyala.')
    else:
        print_delay('Kipas mati.')

def heat(mode, durasi):
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
