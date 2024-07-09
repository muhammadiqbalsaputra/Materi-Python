def penambahan(angka1,angka2):
    return angka1 + angka2

def pengurangan(angka1,angka2):
    return angka1 - angka2

def perkalian(angka1,angka2):
    return angka1 * angka2

def pembagian(angka1,angka2):
    return angka1 / angka2

def perpangkatan(angka1,angka2):
    return angka1 ** angka2

def ganjilgenap(angka):
    if angka %2==0:
        return 'genap'
    else:
        return 'ganjil'
    
def tampilanmenu():
    print('='*25)
    print('Pilih Operasi Bilangan')
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print('='*25)

def perhitungan(input_perhitungan):
    
    angka1 = int(input('Masukan Angka Pertama : '))
    angka2 = int(input('Masukan Angka Kedua : '))
    if input_perhitungan == '1':
        print (penambahan(angka1,angka2))
    elif input_perhitungan == '2':
        print (pengurangan(angka1,angka2))
    else:
        print (perkalian(angka1,angka2))
        