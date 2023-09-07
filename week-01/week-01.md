# Pertemuan Minggu 01

**Tujuan**: Mahasiswa mampu menjelaskan prinsip algoritma dan dasar Python


### Sub-topik yang akan dipelajari
- [1.1 Algoritma](#11-algoritma)
- [1.2 Arsitektur Komputer](#12-arsitektur-komputer)
- [1.3 Pengantar Python](#13-pengantar-python)
- [1.4 _Interpreter_ dan _Compiler_](#14-interpreter-dan-compiler)

Mata kuliah ini lebih tepat dikatakan pengantar pemrograman menggunakan Python
daripada algoritma dan pemrograman. Konsep algorithma sendiri atau 
topik pengantar algorithma sangat jarang sekali disinggung dalam perkuliahan ini.

Di akhir semester, kita diharapkan mampu membuat program sederhana menggunakan
bahasa pemrograman Python baik dalam bentuk CLI (_Command Line Interface_)
maupun GUI (Graphical User Interface). Namun mahasiswa diharapkan secara
berkelompok mampu membuat program sederhana yang memuat beberapa topik yang
telah dipelajari setelah menyelesaikan seluruh topik. 
Terdapat 12 topik yang akan kita pelajari sepanjang
perkuliahan:
1. Definisi algoritma, arsitektur komputer, pengantar Python, _interpreter_
   dan _compiler_
2. Simbol diagram alir, sintaksis _pseudocode_, keluaran program
3. Percabangan: `if`, `if else`, `if else` bertingkat
4. Algoritma perulangan, diagram alir perulangan dengan percabangan, 
   _pseudocode `WHILE`, kode program Python dengan `WHILE`
5. _pseudocode `FOR`, kode program Python dengan `FOR`
6. `Array`
7. `String`
8. Fungsi
9. _Exception Handling_
10. _File Processing_
11. _Graphical User Interfacee_ (GUI)
12. `PyQt`

## [1.1 Algoritma](#sub-topik-yang-akan-dipelajari)

- **Algoritma**:   
  Tahapan instruksi yang jelas yang dirancang untuk 
  menyelesaikan suatu permasalahan atau melakukan tugas tertentu.


- **Logika**:    
  Suatu cabang ilmu matematika dan filsafat yang mempelajari
  secara sistematis konsep penalaran, pengambilan kesimpulan (*inference*),
  dan prinsip-prinsip yang mengatur argumen-argumen valid dan *sound* (
  premis-premis yang benar menghasilkan kesimpulan yang benar).

- **Penalaran**:    
  Kemampuan manusia untuk berpikir dengan akal tentang suatu
  permasalahan yang menghasilkan sebuah solusi, dapat dibuktikan dan
  dapat diterima akal.  

  Terjemahan bahsa inggris untuk **penalaran** (_reasoning_), yang lebih baik:
  > **Reasoning** is the cognitive process through which a person systematically
  > analyzes a problem, applies logical thinking, and arrives at a solution
  > that can be demonstrated to be valid and is intuitively acceptable

### Syarat algoritma
Secara umum terdapat tiga komponen yann harus ada untuk 
suatu objek dikatakan sebagai algoritma yaitu:
1. **Input**:    
   data yang harus diberikan kepada komputer. Ada kalanya suatu algoritma
   tidak memiliki inputan secara eksplisit dari _user_, contoh: _Pseudo Random
   Number Generator_. Inputan berupa _seed_ diambil dari keadaan internal 
   komputer.
2. **Logika** (lebih tepat: prosedur yang logis):    
   prosedur suatu algoritma
   harus memuat proses yang logis (dapat dibuktikan kebenarannya).
   Prosedur ini terdiri dari instrukss yang mampu mengubah input menjadi
   output yang diinginkan.
3. **Output** :    
   informasi yang diperoleh dari komputer.
   Ada kalanya suatu algoritma hanya menghasilkan suatu aksi dan tidak
   mengasilkan output. Biasanya disebut _side effect_.

### Domain (ruang lingkup) algoritma
Terdapat empat domain yang dapat dikaji atau dipelajari dalam suatu algoritma
1. **Program**:    
   representasi formal dari suatu algoritma dengan menggunakan
   bahasa pemrograman yang bisa dimengerti (dieksekusi/dijalankan) 
   oleh komputer.
2. **Proses**:    
   aktivitas menjalankan langkah-langkah dalam algoritma. 
   Bisa disebut proses kompilasi suatu algoritma
3. **Algoritma** (lebih tepatnya prosedur):   
   tahapan untuk menyelesaikan
   masalah. Seringkali suatu masalah dapat diselesaikan dengan lebih 
   dari satu cara (banyak kemungkinan)
4. **Masalah**:   
   Motivasi yang mendasari pembuatan algoritm.

### Contoh algoritma
Diberikan permasalahan untuk menukar isi dua gelas yang masing-masing
berisi teh dan kopi. (Ilustrasi lihat slide pertemuan Minggu 01).

1. Sediakan satu gelas kosong, kita beri label gelas X.
2. Kita namakan gelas berisi teh, T dan gelas berisi kopi, K.
2. Pindah isi gelas T ke gelas X.
3. Pindah isi gelas K ke gelas T.
4. Pindah isi gelas X ke gelas K. 
5. Didapatkan gelas T berisi kopi dan gelas K berisi teh.


### Ciri-ciri algoritma
Hampir mirip dengan syarat algoritma namun lebih lengkap dan spesifik.
Berikut adalah ciri-ciri suatu objek dikatakan algoritma:
- memiliki **input**:   
  suatu algoritma harus mampu menerima beberapa masukan yang
  terdefinisi dengan jelas. 

- memiliki **output**:    
  algoritma harus memberikan beberapa hasil sebagai suatu output, 
  sehingga kebenarannya dapat dinalar (diuji runtutan logikanya).

- bersifat **pasti** (_definiteness_):    
  algoritma memiliki instruksi-instruksi yang jelas dan tidak ambigu.
  Setiap instruksi harus cukup dispesifikasi secara pasti
  terkait dengan tiap langkah yang ia ambil.

- bersifat **terbatas** (_finiteness_):   
  algoritma harus dapat berhenti di suatu titik henti yang diatur
  oleh suatu _stopping rule_
  setelah menjalankan intruksi yang berjumlah terbatas.
  
- bersifat **efektif**:     
  algoritma sebisa mungkin harus dapat dilaksanakan dengan 
  instruksi yang efektif. Contoh intruksi yang tidak efektif adalah
  `A = A + 0` atau `A = A * 1`.

- bersifat **independen**:    
  tidak bergantung pada bahasa pemrograman 
  sebagai cara untuk mengimplementasikan algoritma. Artinya 
  setiap algoritma dapat diimplementasikan menggunakan bahasa pemrograman
  manapun.

### Struktur algoritma
Secara garis besar, algorithma memiliki struktur sebagai berikut:
- Runtunan (_sequence_):   
  Merupakan kumpulan instruksi yang dijalankan secara berurutan.    
  Urutan dari instruksi menentukan hasil akhir dari suatu algoritma.   
  Bila urutan penulisan berubah bisa jadi hasil akhir berubah:
  `(4+3)*7 = 49` (dikerjakan dulu penjumlahan baru perkalian) tidak s
  sama dengan `4+(3*7) = 25` (dikerjakan dulu perkalian baru penjumlahan)

  Contoh: (algoritma penukaran dua bilangan)   
  1. Deklarasikan variabel `A`, `B`, dan `C` sebagai bilangan bulat
  2. Masukkan nilai `A` dan `B`
  3. Masukkan nilai `A` ke dalam `C`
  4. Masukkan nilai `B` ke dalam `A`
  5. Masukkan nilai `C` ke dalam `B`
  6. Selesai

- Pemilihan (_selection_):   
  Instruksi yang dikerjakan dengan kondisi tertentu     
  Kondisi adalah persyaratan yang dapat bernilai benar atau salah

  Contoh: (algoritma penentuan bilangan genap)
  1. Tentukan nilai untuk variabel `x`
  2. Jika `x` habis dibagi 2, maka lakukan langkah (iv).
  3. Jika tidak, maka lakukan langkah (v).
  4. Cetak nilai `x`
  5. Selesai

- Perulangan (_repetition_):     
  Kegiatan mengerjakan sebuah atau sejumlah aksi yang sama 
  sebanyak jumlah yang ditentukan atau sesuai dengan kondisi yang diinginkan

  Contoh: (algoritma penambahan bilangan 1 dengan 1 sebanyak 8 kali)
  1. Atur nilai `x` menjadi 1
  2. Tambahkan nilai `x` saat ini dengan 1 
  3. Ketika `x` kurang dari 10, lakukan langkah (ii) 
  4. Selesai.

## [1.2 Arsitektur Komputer](#sub-topik-yang-akan-dipelajari)
Merupakan denah atau gambaran komponen secara garis besar bagaimana
komputer dibangun.

Berikut komponen-komponen dalam suatu arsitektur komputer
- _**Central Processing Unit**_:   
  media tempat pengeksekusian perintah, _event_, atau program.
- _**Main Memory**_:   
  media penyimpanan data yang digunakan oleh CPU.
- _**Software**_:   
  Suatu informasi yang digunakan untuk melakukan manajemen semua komponen
  yang berada di dalam komputer.
- _**Secondary Memory**_:  
   media penyimpanan data dalam jumlah besar, bersifat _non-volatile_.
- _**Input and Output Devices**_:   
   media interaksi komputer dengan _user_
- _**Network**_:  
   media yang menghubungkan suatu komputer dengan komputer yang lain


## [1.3 Pengantar Python](#sub-topik-yang-akan-dipelajari)
Di praktikum kita menggunakan PyChart, 
namun dapat juga menggunakan VSCode
dengan program Python yang disediakan 
oleh Anaconda.

## [1.4 _Interpreter_ dan _Compiler_](#sub-topik-yang-akan-dipelajari)

- _**Interpreter**_:      
  Program komputer yang berfungsi melakukan eksekusi pada sejumlah instruksi  
  yang ditulis dalam suatu bahasa pemrograman tanpa terlebih dahulu
  menyusunnya menjadi program berbahasa mesin.

- _**Compiler**_:    
  Seubah program kkomputer yang berguna untuk menerjemahkan semua kode
  pada suatu berkas (_file_) yang ditulis dalam bahasa pemrograman tertentu
  menjadi bahasa mesin.

