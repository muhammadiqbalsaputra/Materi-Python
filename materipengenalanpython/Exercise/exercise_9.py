import pandas as pd

jumlah = [
    [10,24,15],
    [100,34,23],
    [12,90,78],
    [2,3,5],
    [24,24,13],
    [13,24,20],
    [10,2,8],
    ]

hari = ['senen','selasa','rabu','kamis','jumat','sabtu','ahad']
barang = ['produk A','produk B','produk C']
dfJumlah = pd.DataFrame(jumlah,index=hari,columns=barang)
print(dfJumlah)

print('\n','Total Penjualan')
total_penjualan_seminggu = dfJumlah.sum()
print(total_penjualan_seminggu)

print('\n','Total Penjualan Setiap Hari')
total_penjualan_setiap_hari = dfJumlah.sum(axis=1)
print(total_penjualan_setiap_hari)

print('\n','---Produk Dengan Penjualan Terbanyak Selama Seminggu---')
produk_terbanyak_seminggu = total_penjualan_seminggu.idxmax(axis=0)
print(produk_terbanyak_seminggu)

print('\n','---Hari dengan penjualan tertinggi untuk setiap produk---'.title())
hari_dengan_penjualan_tertinggi = total_penjualan_setiap_hari.idxmax()
print(hari_dengan_penjualan_tertinggi)