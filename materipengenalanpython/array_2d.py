array_2d = [[1,2,3],
            [4,5,6],
            [7,8,9]]

# memanggil angka sembilan pada array dua dimensi
# dengan memanggil variabel dan indeks baris dan kolom
# contoh : angka sembilan berada pada indeks baris ke 2 dan kolom ke 2
print(array_2d[2][2])

# menambah dimensi lagi
array_2d.append([10,11,12])
print(array_2d)

# merapikan array dengan menggunakan for
for i in array_2d:
    print(i)

for a in array_2d:
    print(i[0]) # menghasilkan output dari setiap kolom saja

