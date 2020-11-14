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
# (C) 2020 Hilya F. Imania, Gibran Darmawan,
# Joy P. Sitanggang, and Rd. Elviana L.
# Jakarta, Indonesia
# Released under MIT License (MIT)
# -----------------------------------------------------------

import unit

############################

def apaini(modes):
    unit.print_mode(modes)

    mode = unit.input_mode(modes)
    durasi = unit.input_durasi()

    unit.switch_lampu(True)
    unit.switch_magnetron(True)
    unit.switch_kipas(True)
    unit.heat(mode, durasi)
    unit.switch_lampu(False)
    unit.switch_magnetron(False)
    unit.switch_kipas(False)
    unit.beep()
    unit.buka_pintu()

def main():
    modes = ['micro', 'grill', 'defrost', 'popcorn']

    while True:
        unit.buka_pintu()
        unit.switch_lampu(True)

        food = unit.input_makanan()

        unit.switch_makanan(True, food)
        unit.tutup_pintu()
        unit.switch_lampu(False)

        while True:
            apaini(modes)

            if unit.keluarkan_makanan(food):
                unit.switch_makanan(False, food)
                unit.tutup_pintu()
                break
            else:
                unit.tutup_pintu()

############################

try:
    unit.welcome()
    main()
except KeyboardInterrupt:
    unit.goodbye()
    pass
