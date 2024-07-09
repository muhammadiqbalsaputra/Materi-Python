data = {'nama':'Muhammad','kelas':'2b','NIM':'23090120','hobi':'basket'}
print(data)

# menambah key atau value baru
data['umur']='12' # variabel[label]= nilai atau value
print(data)

# edit dictionary 
data['nama'] = 'robit nasi lengko' #variabel[label yang sudah ada] = nilai yang ingin diganti
print(data)

# hapus key dan value dictionary
del data['hobi'] # del variabel[label yang ingin dihapus]
print(data)

# memanggil value pada sebuah key atau label
print(data['nama'])