import numpy as np

array_2d = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

print(array_2d[0,2]) # apabila memanggil nilai menggunakan numpy hanya dipisah dengan koma contoh [2,3] bukan [2][3]

# cara melakukan total data per baris
total_baris = np.sum(array_2d, axis=0) # axis=0 digunakan untuk total data tiap baris nya
total_kolom = np.sum(array_2d, axis=1) # axis=1 digunakan untuk total data tiap kolom nya

print(total_baris)
print(total_kolom)

# untuk mencari nilai tertinggi dari nilai max suatu baris atau kolom
nilai_tertinggi_baris = np.max(array_2d, axis=0)
nilai_tertinggi_kolom = np.max(array_2d, axis=1)

print('\n')
print(nilai_tertinggi_baris)
print(nilai_tertinggi_kolom)

# mencari indeks nilai tertinggi 
index_nilai_tertinggi_baris = np.argmax(array_2d, axis=0) 
index_nilai_tertinggi_kolom = np.argmax(array_2d, axis=1)

print(index_nilai_tertinggi_baris) #memunculkan hasil indeks tertinggi dari setiap baris
print(index_nilai_tertinggi_kolom) #memunculkan hasil indeks tertinggi dari setiap kolom