array_2d = {
    'senin':[1,2,3],
    'selasa':[4,5,6]}

print(array_2d['senin'])
print(array_2d['selasa'][2]) # memunculkan angka 6 pada baris selasa

for hari,value in array_2d.items():
    print(f'{hari} : {value}')
    
for day,date in array_2d.items():
    print(f'{day} : {date[0]}')


