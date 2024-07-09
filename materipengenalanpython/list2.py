# mengakses elemen berdasarkan indeks
person = ['bintang','agus','hilmi papeda','iwan']
print(person[2])

# mengakses elemen dengan mencari index dari value atau nilai tertentu
print(person.index('hilmi papeda')) # output 2 karena 'hilmi papeda' berada di index ke 2

# menghitung data berapa kali muncul
print(person.count('hilmi papeda')) # output 1 karena nilai 'hilmi papeda' muncul sebanyak 1 kali

# manipulasi list

# .sort() mengurutkan data baik angka, maupun huruf
teman = ['robit','hilmi','agas','izat']
teman.sort()
print(teman)

# .reverse() membalikan urutan dari yang terbelakang baik angka, maupun huruf
teman.reverse()
print(teman)

# untuk menghitung jumlah data pada list
print(len(teman))