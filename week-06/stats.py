import math

# kita akan membuat program statistik sederhana
# menghitung rata-rata
# mencari median
# mencari modus
# menghitung standard deviasi

data = [2, 1, 3, 6, 7, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5]
data2 = [2, 1, 3, 6, 7, 2, 3, 4, 2, 1, 2, 3, 4, 5]

# mencari banyaknya elemen suatu list
print(len(data))

# menghitung rata-rata
total = 0
for idx in range(len(data)):
  # print(data[idx], end=" ")
  total = total + data[idx]

print("total data: ", total)
rata_rata = total/len(data)
print("rata-rata: ", rata_rata)


# menghitung variance
total_sqr = 0       # akan menyimpan selisih data dengan rata dikuadratkan
for idx in range(len(data)):
  total_sqr = total_sqr + (data[idx] - rata_rata)**2
variance = total_sqr/(len(data) - 1)

# menghitung standard deviation
std = math.sqrt(variance)
print("std: ", std)


# menghitung median
panjang_data = len(data)   # banyaknya data, N
data_sorted = sorted(data)
print("data_sorted: ", data_sorted)

if (panjang_data % 2 == 1):
  idx_tengah = int((panjang_data - 1) / 2)

print("idx_tengah", idx_tengah)
median = data_sorted[idx_tengah]
print("median: ", median)


# menentukan modus
dict_kemunculan = {}

for bilangan in data:
  if bilangan in dict_kemunculan:
    dict_kemunculan[bilangan] += 1
  else:
    dict_kemunculan[bilangan] = 0

max_kemunculan = 0
for (bilangan, kemunculan) in dict_kemunculan.items():
  if (max_kemunculan < kemunculan):
    max_kemunculan = kemunculan 
    print("Bilangan max: ", bilangan)
    # index_kemunculan = kemunculan 

print(dict_kemunculan)
print("banyak muncul: ", max_kemunculan)