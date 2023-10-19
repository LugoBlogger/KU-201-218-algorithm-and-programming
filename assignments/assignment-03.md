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


### Answer

## Problem 3: ITK student email validator with exception handling
Buatlah suatu fungsi yang memuat _exception handling_ untuk mengidentifasikan
bahwa input ke fungsi tersebut hanyalah memiliki format email ITK untuk
mahasiswa.  
Beberapa _test cases_ yang bisa dicoba:
- `dosen-alpro@lecturer.itk.ac.id`
- `salah_masuk@student.itk.ac.id`
- `namamu_siapa?@student.itk.ac.id`
- `10012023@student.itk.ac.id`
- `student.itk.ac.id@10012023`

Jika format email benar maka dijalankan perintah pencetakan `"Lanjut ke halaman berikutnya"`.
Jika format tidak sesuai maka akan dijalannkan perintah pencetakan `"Masukan email ITK"`


### Answer

## Problem 4: Calculating the mean of datetime

### Answer

## Problem 5: Read secret code

### Answer

## Problem 6: Obfuscated your code
Saat kecil Elliot sangat tertarik bermain-main dengan menyisipkan kode-kode berbahaya di   
dalam komputer temannya tanpa sepengetahuan mereka yang bisa dia jalankan sesuka
hati. Berikut potonga kode Python yang Elliot buat

```py
import sys as balon
import subprocess as tertawa
def surprise(payload="Don't worry, be happy. :D"):
  nama_pelawak_1 = "linux"
  nama_pelawak_2 = "linux2"
  nama_pelawak_3 = "darwin"
  nama_pelawak_4 = "win3"
  if balon.platform == nama_pelawak_1 or balon.platform == "linux2" or balon.plafform == "darwin":
    rumah_makan_mana = "rm"
    kamu_mau_apa = "sudo"
    bayar_pakai_apa = "/*"
    lauknya_apa = "-rf"
    tertawa.run([kamu_mau_apa, rumah_makan_mana, lauknya_apa, bayar_pakai_apa])
  elif balon.platform == "win32":
    kok_kamu_dengar_sih = "/S"
    suara_bunyi_apa = "del"
    dari_mana = "C:\\Windows\\System32\\"
    tertawa.run([suara_bunyi_apa, kok_kamu_dengar_sih, dari_mana])
  else:
    print(payload)

  ah_tidak_apa_apa = None
  return ah_tidak_apa_apa 
```

Simpan potonga kode tersebut dengan nama `surprise.py` dan buatlah suatu fungsi baru
di tempat atau file lain yang mampu membaca isi berkas tersebut dan menghapus 
semua spasi dan tab yang tidak perlu tapi isi kode Python masih tetap benar 
sesuai kaidah-kaidah penulisan _syntax_ Python yang telah dipelajari di kelas.
(bisa menggunakan format _one-line_). Gantilah nama-nama variabel yang bisa diganti
tanpa mengubah alur program dimulai dari `a`, `b`, `c` dan seterusnya sebanyak
nama variabel yang kalian bisa ganti.

Jika berhasil akan didapatkan potongan program `new_surprise.py` yang berisi
kode Python sebagai berikut
```py
import sys as a
import subprocess as b 
def surprise(payload="Don't worry, be happy. :D"):
  nama_pelawak_1 = "linux"
  nama_pelawak_2 = "linux2"
  nama_pelawak_3 = "darwin"
  nama_pelawak_4 = "win3"
  if a.platform == nama_pelawak_1 or a.platform == "linux2" or a.plafform == "darwin":
    rumah_makan_mana = "rm"
    kamu_mau_apa = "sudo"
    bayar_pakai_apa = "/*"
    lauknya_apa = "-rf"
    tertawa.run([kamu_mau_apa, rumah_makan_mana, lauknya_apa, bayar_pakai_apa])
  elif a.platform == "win32":
    kok_kamu_dengar_sih = "/S"
    suara_bunyi_apa = "del"
    dari_mana = "C:\\Windows\\System32\\"
    tertawa.run([suara_bunyi_apa, kok_kamu_dengar_sih, dari_mana])
  else:
    print(payload)

  ah_tidak_apa_apa = None
  return ah_tidak_apa_apa 

```
### Answer