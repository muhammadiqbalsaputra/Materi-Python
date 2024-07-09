array = [1,2,3,4,5]

print(array[1]) #output 2
print(array[3]) #output 4

# akses nilai array
array[1] = 12
print(array) #output [1, 12, 3, 4, 5]

# tambah data
array.append(6)
print(array) # output [1, 12, 3, 4, 5, 6]

# Menambahkan data pada suatu indeks tertentu
array.insert(0,15)
print(array)
# Hapus Data
array.pop(4)
print(array)

# Total Data
total_data = sum(array)
print('Total Data : ',total_data)

# Jumlah Data
Jumlah_data = len(array)
print(Jumlah_data)

# rata rata nilai
Jumlah_data = len(array)
total_data = sum(array)

rata = total_data/Jumlah_data

nilai_tertinggi = max(array)
nilai_terendah = min(array)

jumlah_nilai_diatas_rata2 = sum(True for i in array if i>rata)
nilai_diatas_rata2 = [i for i in array if i > rata]

# mengurutkan data yang terkecil ke terbesar
array.sort()
print(array)
# mengurutkan data yang terbalik
array.reverse()
print(array)

print(f'Rata Rata Nilai adalah : {rata}')
print(f'Nilai Tertinggi {nilai_tertinggi}')
print(f'Nilai Terendah {nilai_terendah}')
print(f'Jumlah Nilai diatas Rata rata {jumlah_nilai_diatas_rata2}')