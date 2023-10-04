# Assignment 02

Group members
- FullName1 (StudentID) (Problem #)
- FullName2 (StudentID) (Problem #)
- FullName3 (StudentID) (Problem #)
- etc.


## Problem 1: Automated symbol printing 1
Menggunakan _method_ pada _String_: `.rjust()`, `.ljust()` dan `.center()`,
susunlah logo ITK berikut.

```
IIIIIIIII   TTTTTTTTT   KKK   KKK
   III         TTT      KKK KKK
   III         TTT      KKKKKK
   III         TTT      KKK KKK
IIIIIIIII      TTT      KKK   KKK
```
Logo di atas memliki lebar `n = 3`. Perhatikan untuk `n = 3`
lebar huruf `3n` dan tinggi huruf `2n - 1` dan jarak antar antar
huruf adalah `n`.

Uji untuk ukuran logo `n = 5`, `n = 7`, dan `n = 9`

### Answer

## Problem 2: Automated symbol printing 2
Melanjutkan Problem 1. Tambahkan fitur berikut:
1. Masukan oleh _user_ logo yang ingin dicetak
   `logo_name: `
2. Masukan oleh _user_ ukuran logo `n: `

Contoh program
```
logo_name: KMITK
        n: 3

Hasil cetak logo

KKK   KKK   MMM         MMM   IIIIIIIII   TTTTTTTTT   KKK   KKK
KKK KKK     MMMM       MMMM      III         TTT      KKK KKK
KKKKKK      MMMMMM   MMMMMM      III         TTT      KKKKKK
KKK KKK     MMM   MMM   MMM      III         TTT      KKK KKK
KKK   KKK   MMM         MMM   IIIIIIIII      TTT      KKK   KKK
```
Lihat acuan semua karakter _alphanumeric_ di tautan berikut
[alphanumeric specs](./letter_spesification.md)

[Opsional (boleh dikerjakan atau tidak)] Untuk `n = 5`, `n = 7`, dan `n = 9`, silahkan 
dibuat terlebih dahulu spesifikasinya.

### Answer

## Problem 3
Buatlah suatu program _String Validator_ untuk _password_ 
menggunakan _methods_ berikut:
`isalpha()`, `isalnum()`, `isdigit()`, `islower()`, `isupper()`
dengan spesifikasi sebagai berikut:
- Jumlah karakter minimum 8 maksimum 16
- Hanya terdiri dari bilangan, abjad, dan _special characters_: `_`, `+`, `?`
- Minimum karakter bilangan 1, minimum karakter abjad 1, minimum
  _special characters_ 1

[Opsional (boleh dikerjakan atau tidak)]: Susunlah kode program Python hanya dalam satu baris kode

### Answer

## Problem 4
Diberikan data _string_ di Python sebagai berikut:
```py
inventory = "apple emerald brick bone brick coal emerald bone apple brick brick coal bone emerald bone bone apple apple coal bone bone apple brick brick coal brick brick apple brick coal bone brick bone coal apple apple brick apple bone apple brick apple bone apple emerald coal emerald apple brick brick coal brick apple apple bone apple emerald bone bone brick bone bone apple emerald emerald bone brick emerald brick emerald apple bone coal coal coal bone brick bone bone emerald bone emerald coal coal emerald brick brick emerald emerald bone apple brick bone brick emerald brick apple bone apple brick"
```

Hitunglah frekuensi tiap kata dan simpanlah dalam bentuk _dict_ di Python
di variabel `inventory_dict`.

Contoh output program ketika mencetak `inventory_dict`:
```
  apple = 21
emerald = 16
  brick = 25
   bone = 25
   coal = 13
```

### Answer

## Problem 5: CLI histogram 1
Diberikan suatu data _inventory_ beberapa _materials_ di dalam _video game_
_Mineraft_ sebagai berikut, 
yang dinyatakan dalam bentuk _dict_ Python
```py
inventory = {
  "Emerald": 2,
  "Diamond": 30,
  "Redstone": 11,
  "Brick": 28,
  "Coal": 17,
  "Snowball": 0
  "Leather": 10,
  "Paper": 9,
  "Flint": 4,
}
```

Buatlah program Python yang dapat mengubah data _dict_ tersebut ke dalam 
bentuk histogram sebagai berikut:
```
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

Jumlah tanda bintang `*` menyatakan banyaknya _materials_. Misal
`"Flint": 4` maka akan tercetak empat kali tanda bintang `****`.
Perhatikan juga nama _materials_ memiliki kesejajaran (_alignment_)
rata-rata kanan dan ada satu spasi setelah `:`.

### Answer

## Problem 6: CLI histogram 2
Melanjutkan Problem 5, tambahkan beberapa fitur berikut:
1. Masukan oleh _user_ `lebar_max` dengan type data `int` 
   untuk membatasi lebar histogram.   
 
   `lebar_max` ini menyatakan berapa banyak tanda bintang `*`
   yang harus dicetak untuk _materials_ dengan jumlah terbanyak.   

   Misalkan _material_ terbanyak `"Diamond": 30` untuk `lebar_max = 50` 
   maka jumlah tanda bintang yang harus tercetak adalah 50 buah. 
   Sedangkan untuk _materials_ yang lain mengikut aturan normalisasi ini. 
   Contoh untuk `"Flint": 4`, maka tanda bintang yang tercetak sebanyak
   `(4/jumlah_material_terbanyak) * lebar_max = (4/30) * 50 = 6.7 = 7`
   (dibulatkan ke bilangan bulat terdekat). 
   
   Pembulatan dapat menggunakan 
   perintah `round()`.

2. Masukan oleh _user_ `is_sorted?` dengan jawaban `y` atau `n`
   untuk mengurutkan secara alfabet nama _materials_.
3. Tambahan angka penunjuk setelah nama _materials_ yang menyatakan
   banyaknya _materials_ tersebut dalam format digit yang sama.
   Misal nilai tertinggi 2 digit, yaitu 30, maka untuk digit-digit yang
   hanya terdiri dari satu digit perlu dilakukan _zero padding_ seperti
   yang ditampilkan contoh di bawah.

Contoh output program:
```
lebar_max: 30 
is_sorted? y

=================
 Tabel inventory 
=================
   Brick [28]: ****************************
    Coal [17]: *****************
 Diamond [30]: ******************************
 Emerald [02]: **
   Flint [04]: ****
 Leather [10]: **********
   Paper [09]: *********
Redstone [11]: ***********
Snowball [00]:
```

Lakukan pengujian untuk `lebar_max = 80` dan data _inventory_ berikut:

```py
inventory = {
  "Lead": 15,
  "Bread": 79,
  "Apple": 22,
  "Bone": 75,
  "Hoe": 1,
  "Pickaxe", 60,
  "Egg": 13,
  "Milk": 17,
  "Slimeball", 94,
  "Salmon": 29,
  "Potato": 45,
  "Gunpowder": 3,
  "Feather": 85,
  "Shears": 95,
  "Wheat": 70,
  "Bucket": 98,
  "Carrot": 26,
  "Crossbow": 23,
  "Arrow": 33,
  "Clay": 23
}
```


### Answer