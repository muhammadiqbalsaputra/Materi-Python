listSaya = ['ayu','dimas','fachrul','bagus','eka','bani','cahya']
print(listSaya)

# menambahkan data list menggunakan(.append(nilai))
listSaya.append('agus')
print(listSaya)

# menyisipkan data list dengan menggunakan insert (.insert(index,value))
listSaya.insert(2,'prasetya')
print(listSaya)

# menghapus elemen tertentu dari daftar dengan menggunakan remove.
listSaya.remove('fachrul')
print(listSaya)

# menghapus elemen berdasarkan index atau range dengan menggunakan del
del listSaya[0] # del variabel[index]
print(listSaya)

listSaya.pop(1) #menggunakan .pop(index)
print(listSaya)

listSaya.pop()#menggunakan .pop() tanpa menambahkan index maka yang terhapus nilai yang berada pada akhir index
print(listSaya)