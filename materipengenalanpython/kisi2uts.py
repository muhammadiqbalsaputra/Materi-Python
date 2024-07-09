# kISI KISI UTS
# -Flowchart
# -Tipe data
# -Operator
# -Percabangan
# -Perulangan
# -input output

# metode live coding

int1 = 1
float1 = 1.5
string1 = 'babi ganas'
boolean = True
listdata = [1,2,3,4]
setdata = {1:'ayu',2:'kira',3:'bagus'}
tupledata = (1,'iqbal',2,'kayangh',4,'fahri')

print (int1)
print (float1)
print (string1)
print (boolean)
print (listdata)
print (setdata)
print (tupledata)
print ('\n')

#operator perhitung
a = 12
b = 10

print (a + b)
print (a - b)
print (a / b)
print (a * b)
print (a ** b)
print('\n')

# operator pembanding
a = 10
b = 5

print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
print('\n')

# operator penugasan
a = 5
b = 3

a *= b
print (a)
a /= b
print (a)
a -= b
print (a)
a += b
print (a)
a **= b
print (a)
print ('\n')

# operator logika
a = True
b = False

print(a and b)
print(a or b)
print(not a)
print('\n')

# operator keanggotaan
a = [2,3,4,5,6,7]

print (10 in a)
print (10 not in a)
print('\n')

# operator identitas
a = [2,3,5]
b = [3,4,5]

print(a is b)

a = 4
b = 4
print (a is b)
print('\n')

# operator tenary 
a = 5
hasil = 'genap' if a%2 == 0 else 'ganjil' 
print (hasil)
print('\n')

# percabangan 
idris = 80
if idris >= 75:
    print(f'{idris} anda lulus')
else:
    print(f'{idris} anda tidak lulus')

# perulangan
for i in range (1,5+1):
    print(i)

a = 10
for b in range (a):
    print(b)

a = ['hewan','tumbuhan','langit']
for b in a:
    print (b)
    print(a)

# contoh soal 
nilai = 0
jumlah_anak = int(input('Masukan Jumlah Anak : '))
for i in range (1,jumlah_anak+1):
    berat = int(input(f'Masukan berat badan anak ke {i} : '))
    nilai += berat
rata2 = nilai / jumlah_anak
print(f'Jumlah rata rata dari {jumlah_anak} adalah {rata2} KG')

# input output
nama = input("masukan nama : ")
kelas = input("masukan kelas : ")
nim = int(input('Masukan NIM : '))
if nama and kelas and nim >= 2300000:
    print('Verifikasi anda Terpenuhi')
else:
    print('Verifikasi anda ada yang kurang coba lagi')