fwrite = open("file_baru.txt", "w")
# penjelasan: 
# - fwrite adalah nama variable
# - open() adalah fungsi bawaan di Python untuk melakukan pembacaan dan penulisan file
# - "file_baru.txt" adalah nama file dengan ekstensi .txt
# - "w" (biasanya disebut `flag`) yang berfungsi untuk mengatur mekanisme apa
#   yang user pilih. Dalam hal ini "w" adalah mekanisme "write" yang artinya
#   menuliskan file.
# print(fwrite)
# print(type(fwrite))
# print(dir(fwrite))

fwrite.write("Halo, baris pertama file yang saya buat\n")
# nama variabel fwrite memiliki fungsi .write() yang merupakan akibat
# dari kita telah mendefinisikan fwrite sebagai output dari perintah 
# open()

fwrite.write("Ini baris ke-2\n")
fwrite.write("Ini baris ke-3\n")
fwrite.write("Ini baris ke-4\n")
fwrite.write("Ini baris ke-5\n")
fwrite.write("Ini baris ke-6\n")
fwrite.close()   # penting sebagai pelengkap