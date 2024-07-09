# deklarasi python
def cetakString():
    print('Halo World')
cetakString()

# deklarasi python dengan parameter
def namaku(parameter1,parameter2):
    print(f'nama ku adalah : {parameter1}, dari kelas {parameter2}')
namaku('iqbal','1b')

print('\n')

def perkalian(angka1,angka2):
    print(f'Hasil dari {angka1} * {angka2}')
    total = angka1 * angka2
    print(f'Hasil nya {total}')
perkalian(3,3)

# fungsi untuk mengembalikan nilai  dengan menggunakan return
def luas_persegi(sisi):
    print('\n Luas Persegi')
    luas = sisi * sisi
    return luas
print(luas_persegi(5))

def ganjilGenap(angka):
    if angka %2==0:
        return 'Genap'
    else:
        return 'Ganjil'
print(ganjilGenap(6))

# Perbedaan Variabel Lokal dan Global
# variabel Global
nama = 'Iqbal'

def help():
    # Variabel lokal
    nama = 'Fahri'
    print('Nama : ',nama)

# mengakses variabel global
print('Nama : ',nama)
help()
# apabila ada fungsi akan mendahulukan variabel lokal dibanding variabel global, namun apabila dalam suatu fungsi itu tidak tedapat variabel lokal. Maka, fungsi akan mengambil variabel global