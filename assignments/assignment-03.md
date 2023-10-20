# Assignment 03

Group members
- FullName1 (StudentID) (Problem #)
- FullName2 (StudentID) (Problem #)
- FullName3 (StudentID) (Problem #)
- etc.


## Problem 1: Moai ASCII art 1 

Diberikan contoh ilustrasi patung MOAI dengan menggunakan karakter ASCII   
sebagai berikut

```
   ________
  /        \
  |________|
  |__|  |__|
 |   |  |   |
 |   |__|   |
|   ______   |
|    ____    |
\____________/
  /        \
 |__________|
 
```
Tuliskan spesifikasi untuk gambar ASCII art tersebut. Spesifikasi tersebut 
memuat:
- Karakter ASCII yang digunakan
- Ukuran kepala (tinggi dan lebar)
- Ukuran mata (tinggi dan lebar)
- Ukuran leher (tinggi dan lebar)


### Answer

## Problem 2: Moai ASCII art 2
Buatlah fungsi untuk mencetak ilustrasi MOAI dengan masukan fungsi
seperti yang telah dispesifikasikan di Problem 1. Gunakan _keyword arguments_
untuk kasus eksekusi fungsi tanpa masukan (tanpa input) dan memberikan
gambar seperti di Problem 1.

Contoh input argument:
```py
# nilai di input arguments bukan nilai sebenarnya. kalian harus menjawab 
# problem 1 dengan benar untuk tahu nilai-nilai tersebut.
def draw_moai(vert_chars="/|\\", hor_char="_", 
              head_size=(1, 1), eye_size=(1, 1), neck_size=(1, 1)):
  ## deskripsi fungsi
```


### Answer


## Problem 3: Moai ASCII art 3
Simpan atau tulis keluaran dari fungsi di Problem 2 ke dalam file.
`fig_moai.txt`.

### Answer


## Problem 4: Calculating the mean of datetime

Diberikan data `waktu.txt` berikut

```txt
student id, time taken
16131053, 38 mins 12 secs
16131044, 42 mins 5 secs
16131014, 14 mins 21 secs
20131005, 31 mins 52 secs
16131055, 23 mins 51 secs
10131055, 48 mins 27 secs
10131066, 49 mins
11131014, 21 mins 15 secs
16131044, 36 mins 45 secs
20131022, 47 mins 1 sec
10131033, 46 mins 57 secs
16131002, 48 mins 54 secs
16131002, 49 mins 54 secs
16131005, 33 mins 36 secs
11131077, 50 mins
11131066, 50 mins
11131022, 50 mins
```
Buatlah suatu fungsi untuk membaca data `time taken` dan memberikan 
keluaran berupa total waktu pengerjaan dan rata-rata waktu pengerjaan.

Petunjuk: bentuk fungsi dapat memiliki bentuk sebggai berikut:
```py
def calcualte_time(file_input_str):
  # isi program
  return total_waktu, rata_rata_waktu
```


### Answer

## Problem 5: Read secret code 🤫 
Diberikan suatu berkas rahasia `secret.txt` yang berisi data berikut:

```txt
aaa________cccbaa/aaaaaaaa\ccbaa|________|ccbaa|__|aa|__|ccba|aaa|aa|aaa|cba|aaa|aa|aaa|cb|aaa______aaa|b|aaaa____aaaa|b\____________/baa/aaaaaaaa\ccba|__________|cb 
```

Ingat pesan rahasia diatas hanya terdiri dari satu baris.

Menggunakan aturan _decryption_ berikut:
- karakter memuat huruf `a` di ubah spasi `" "` sebanyak kemunculan karakter `a`
- karakter memuat huruf `b` berapapun kemunculannya di ubah menjadi satu karakter
  baris baru `\n`
- karakter memuat huruf `c` berapapun kemunculannya di ubah menjadi karakter kosong `""`

Tentukan pesan rahasia yang ada di dalam `secret.txt`

### Answer


## Problem 6: Read histogram data
Bacalah data dari file `inventory_table.txt` berikut

```txt
Tabel inventory:
 Emerald: **
 Diamond: ******************************
Redstone: ***********
   Brick: ****************************
    Coal: *****************
Snowball:
 Leather: **********
   Paper: *********
   Flint: ****
```

Lalu nyatakan data _inventory_ tersebut menggunakan tipe data
_dictionary_ dengan `key` nama item dan `value` adalah banyaknya
item untuk nama tersebut. 
Cetak hasil pembacaan data tersebut untuk mengecek apakah sudah
benar atau belum.

### Answer