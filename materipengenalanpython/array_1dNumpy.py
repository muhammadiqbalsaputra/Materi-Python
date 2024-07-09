import numpy as np

array1 = np.array([90,89,29,50,90])
print(array1)


ratarata = np.mean(array1)

nilaitengah = np.median(array1)

nilaiMax = np.max(array1)

nilaiMin = np.min(array1)

total_nilaiDiatasRata2 = np.sum(array1>ratarata)

nilaiDiatasRata2 = array1(array1>ratarata)

print(ratarata)
print(nilaitengah)
print(nilaiMax)
print(nilaiMin)
print(total_nilaiDiatasRata2)
