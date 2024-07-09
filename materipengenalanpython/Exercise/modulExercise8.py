import array as arr
nilai = arr.array('i',[])


def inputSiswa():
    siswa = int(input('Masukan Jumlah Siswa : '))
    for jumlah in range(1,siswa+1):
        masukanNilai = int(input(f'Masukan Nilai ke-{jumlah} : '))
        nilai.append(masukanNilai) 

    rata2 = sum(nilai)/len(nilai)
    nilaiTertinggi = max(nilai)
    nilaiTerendah = min(nilai)
    jumlah_nilai_diatas_rata2 = sum(True for i in nilai if i>rata2)

    print(f'Nilai Rata-Rata Kelas :{rata2}')
    print(f'Nilai Tertinggi : {nilaiTertinggi}')
    print(f'Nilai Terendah : {nilaiTerendah}')
    print(f'Jumlah Siswa diatas Rata-Rata :{jumlah_nilai_diatas_rata2}')