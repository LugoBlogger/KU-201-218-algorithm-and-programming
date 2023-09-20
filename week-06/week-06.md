# Pertemuan Minggu 06

**Tujuan**: Mahasiswa mampu menggunakan struktur data
`list` dan `dictonary`

### Subtopik yang akan dipelajari

## Definisi _array_
- _Array_ adalah kumpulan dari nilai-nilai data bertile
  sama dalam urutan tertentu yang menggunakan sebuah nama
  yang sama.
- Nilai-nilai data di suatu _array_ disebut dengan elemen-element
  _array_.
- Letak urutan dari elemen-elemen _array_ ditunjukkan oleh indeks.

- _Array_ bisa berupa _array_ berdimensi satu, dua tiga, 
  atau lebih.
- _Array_ berdimensi satu (_one-dimensional array_) mewakili
  bentuk suatu vektor. _Array_ berdimensi dua
  (_two-dimensional array_) mewakili bentuk dari suatu matriks
  atau table. _Array_ berdimensi tiga (_three-dimensional array_)
  mewakili bentuk dari suatu tensor.

### Contoh

**_pseudocode_**
```
bil1, bil2, bil3, bil4, bil5 : INTEGER
```

```
arr : ARRAY[1..10] OF INTEGER
```


Implementasi Python
- menggunakan `tuple` (_immutable_):

- menggunakan `list` (_mutable_):

- menggunakan `dictionary` (_generalized list_):

## Deklarasi _array_

**_pseudocode_**
```
nama_array : ARRAY[indeksAwal..indeksAkhir] OF tipe_data
```

**contoh**    
_Pseudocode_ untuk deklarasi _array_ `A` berukuran 10 dengan isi elemen bertipe 
bilangan bulan (`INTEGER`)
```
A : ARRAY[1..10] OF INTEGER
```

Dalam bahasa Python, kita tidak memerlukan deklarasi karena
Python merupakan bahsa _dynamic typing_. Tipe data secara
otomatis akan ditentukan berdasarkan nilai dari variabel.

## Mengisi nilai ke dalam _array_


### Contoh


## Mengambil nilai suatu elemen tertentu pada _array_

## Alasan dibalik penggunaan _array_

### Tanpa _array_

**_pseudocode_**

Implementasi Pyton

### Dengan _array_

**_pseudocode_**

Implementasi Python

### Pembahasan

## Contoh _flowchart_ penggunaan _array_

## _Array_ berdimensi dua

Contoh data dua dimensi adalah tabel yang menyimpan
nilai mahasiswa  dengan baris menyatakan nama mata kuliah
dan kolom adalah NIM mahasiswa

<table>
  <tr align="center">
    <td rowspan=2> <b>Mata Kuliah</b>
    <td colspan=3> <b>NIM mahasiswa</b>
  </tr>
  <tr>
    <td align="center"><b>100909</b>
    <td align="center"><b>100910</b>
    <td align="center"><b>100911</b>
  </tr>
  <tr>
    <td>Kalkulus 1
    <td>80
    <td>61
    <td>40
  </tr>
  <tr>
    <td>Fisika Dasar
    <td>76
    <td>43
    <td>86
  </tr>
  <tr>
    <td>Kimia Dasar
    <td>45
    <td>39
    <td>32
  </tr>
  <tr>
    <td>Algoritma dan Pemrograman
    <td>90
    <td>68
    <td>79
  </tr>
</table>

## Deklarasi _array_ berdimensi dua

**_pseudocode_** untuk contoh tabel di atas
```
data_nilai : ARRAY[1..4][1..3] OF INTEGER
```

Implementasi di Python tidak diperlukan karena Python
secara otomatis dapat menentukan tipe dari _array_

## Mengakses elemen _array_ berdimensi dua

Implementasi di Python adalah pembentukan _array_ berdimensi dua
```py
data_nilai = [
  [80, 61, 40],
  [76, 43, 86],
  [45, 39, 32],
  [90, 68, 79]
]
```


## Contoh
Buatlah _pseudocode_ dan _flowchart_ untuk mengurutkan 10 bilangan.
Misal diberikan _test case_
- `input`: `5 4 8 7 2 10 1 6 3 9`
- `output`: `1 2 3 4 5 6 7 8 9 10`

