for i in range(5):
    print(i)
print('\n')
    # output akan menghasilkan 0,1,2,3,4 karena index dari for dimulai dari 0

    # contoh lain
for n in range(6):
    print(f'ayo berhitung {n}')
print('\n')
    # output akan menghailkan mariberhitung 0 sampai mariberhitung 5

# cara agar for menghasilkan angka dengan batas minimal
for j in range(2,6):
    print(j)
    # output akan menghasilkan angka 2,3,4,5
print('\n')

hewan = ['kucing','sapi','kambing','anjing']
for animal in hewan:
    print(animal)
    # output kucing sapi kambing anjing
print('\n')

# cara mengambil nilai index dari data list
for index,animal in enumerate(hewan):
    print(index,animal)
    # output
    # 0 kucing
    # 1 sapi
    # 2 kambing
    # 3 anjing
print('\n')

fruits = ['anggur','strobery','blewah','duren']
numbers = [1,2,3,4,5]
for number,fruit in zip(numbers,fruits):
    print(number,fruit)

print('\n')

# Looping string 
names = 'Muhammad Iqbal Saputra'
for name in names:
    print(name)
print('\n')

# looping dictionary
biodata = {'nama' : 'iqbal', 'nim' : 23090120}
for data in biodata:
    print(data)

# mengambil value dari for loop dictionary
for value in biodata.values():
    print(value)
print('\n')

# mengambil label dan value dari for loop ditionary
for label,value in biodata.items():
    print(label,":",value)

# contoh penggunaan bilangan dalam studi kasus
# contoh penggunaan genap dan ganjil pada for loop
for angka in range(1,9):
    if angka % 2==0:
        print('bilangan genap', angka)
    else:
        print('bilangan ganjil', angka)
