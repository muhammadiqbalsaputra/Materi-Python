import pandas as pd

df = pd.DataFrame([
    [5,6,7],
    [12,7,8],
    [5,10,9],
    ])
print(df)

harijumlah = pd.DataFrame([
    [5,6,7],
    [12,7,8],
    [5,10,9],
    ], index=['senen','selasa','rabu'], columns=['a','b','c']) # index untk penamaan kebawah dan colums untuk penamaan kesamping

print(harijumlah)

# total perbaris 
total_perbaris = harijumlah.sum(axis=0)
total_perkolom = harijumlah.sum(axis=1)
print(total_perbaris)
print(total_perkolom)

# total_tertinggi
index_tertinggi = harijumlah.idxmax()
index_tertinggi_baris = harijumlah.idxmax(axis=0)
index_tertinggi_colums = harijumlah.idxmax(axis=1)
print(index_tertinggi)
print(index_tertinggi_baris)
print(index_tertinggi_colums)

# index_tertinggi_perbaris
index_tertinggi_pebaris = total_perbaris.idxmax()
print(index_tertinggi_pebaris)

# index_tertinggi_perkolom
index_tertinggi_perkolom = total_perkolom.idxmax()
print(index_tertinggi_pebaris)


# apabila ingin melakukan konversi dari pandas
nilai = [
    [1,2,3],     
    [4,5,6],     
    [7,8,9]     
         ]

nilaiDataFrame = pd.DataFrame(nilai)
print(nilaiDataFrame)

hari = ['senen','selasa','rabu']
barang = ['a','b','c']
nilaiDataFrame2 = pd.DataFrame(nilai, index=hari, columns=barang).T # .T digunakan untuk menukar posisi index dan colums
print(nilaiDataFrame2)

