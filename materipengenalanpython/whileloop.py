i = 0
while i <= 15:
    print(' Mari berhitung', i)
    i += 1

while False:
    print('iqbal')

total_perulangan = 0
while True:
    main = input('Ingin Keluar atau tidak? [ya / tidak] : ')
    if main == 'ya':
        break
    total_perulangan += 1
print('total perulangan : ',total_perulangan)

while True:
    angka = int(input("masukan Angka : "))
    if angka %2==0:
        print(angka,"merupakan bilangan genap")
    else:
        print(angka, 'merupakan bilangan ganjil')