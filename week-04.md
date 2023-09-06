# Pertemuan Minggu 04

**Tujuan**: Mahasiswa mampu membuat algoritma, diagram alir, dan
_pseudocode_ perulangan dan mengimplementasikannya dengan Python

### Subtopik yang akan dipelajari
- Algoritma perulangan
- Diagram alir perulangan dengan percabangan
- _Pseudocode_ `WHILE`
- Kode program Python dengan `WHILE`

**Contoh permasalahan**

Berikut diberikan _pseudocode_ untuk mencetak angka 1 sampai 100

```
angka: INTEGER
angka = 1
WRITE angka

angka = 2
WRITE angka

angka = 3
WRITE angka

...

angka = 100
WRITE angka
```

Berikut adalah implementasi Python untuk _pseudocode_ di atas

```py
angka = 1
print(angka)

angka = 2
print(angka)

angka = 3
print(angka)

# ... diketik sampai 99

angka = 100
print(angka)
```

Untuk mengatasi pengetikan yang berulang-ulang, dapat digunakan
perulangan sehingga program lebih ringkas.

Berikut adalah _pseudocode_ untuk perulangan dengan masalah
seperti di atas, yaitu mencetak angka 1 sampai 100

```
angka: INTEGER
FOR angka = 1 TO 100 do
  WRITE angka
ENDFOR
```

Sedangkan implementasi _pseudocode_ untuk program di atas dalam
bahasa Python adalah sebagai berikut:
```py
for angka in range(1, 101):
  print(angka)
```

4.1 Perulangan `FOR ... DO`

**_Pseudocode_**
```
FOR iterator DO

END FOR
```

**_Flowchart_**

Implementasi Python
```py
for variabel_indeks in range(start, stop):
  # aksi_1
```