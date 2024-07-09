from queue import LifoQueue

# Deklarasi Stack (fungsi maxsize untuk melakukan stack statis/tetap apabila ingin dinamis dikosongkan saja)
stack = LifoQueue(maxsize=5)

# menambah data stack dengan menggunakan .put()
stack.put('Bagas')
stack.put('Dion Tukang Bot Stiker')
stack.put('Harto')
stack.put('Ucen')
stack.put('Jarot')

# menampilkan data stack
print(stack.queue)

# menampilkan Top elemen stack
print(f'Top/Peek Stack : {stack.queue[-1]}')

# menghapus Stack 
stack.get()
print(stack.queue)

# mengecek stack kosong atau tidak
print(f'Apakah Stack Kosong ? {stack.empty()}')

# mengecek stack full atau tidak ?
print(f'Stack Full / Tidak : {stack.full()}')

# mengecek jumlah data elemen stack
print(f'Jumlah Stack : {stack.qsize()}')