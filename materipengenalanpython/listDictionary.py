# mengkombinasi list dan dictionary
person = [{'nama':'Bagas','kelas':'2b','NIM':'222'},
          {'nama':'Robit','kelas':'2c','NIM':'335'},
          {'nama':'Prima','kelas':'2a','NIM':'200'}]

print(person)

# cara menambahkan list pada kombinasi
personNew = {'nama':'Ijat','kelas':'10A','NIM':'1945'}
person.append(personNew)
print(person)

for a in person:
    print('-',a['nama'],a['NIM'])

