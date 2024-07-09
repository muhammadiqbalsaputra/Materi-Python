import modulOperasi as math

while True:
    math.tampilanmenu()
    input_perhitungan = str(input('Masukan Jenis Perhitungan [1 / 2 / 3 ] dan ketik (selesai) apabila perhitungan telah selesai : '))
    if input_perhitungan == 'selesai':
        print('\n')
        print('='*25)
        print('Perhitungan Telah Selesai')
        print('='*25)
        break
    
    math.perhitungan(input_perhitungan)