with open("file_baru2.txt", "w") as fwrite:
  fwrite.write("Hai, ini file yang lain\n")
  fwrite.write("Tapi menggunakan cara yang berbeda\n")
  fwrite.write("Kira-kira apa ya bedanya\n")

  # perbedaanya adalah tidak perlu menggunakan fwrite.close()
  # karena ketika sudah keluar dari indentasi with maka fwrite akan di close
  # secara otomatis

  # fwrite.write("Halo, baris pertama file yang saya buat\n")
  # fwrite.write("Ini baris ke-2\n")
  # fwrite.write("Ini baris ke-3\n")
  # fwrite.write("Ini baris ke-4\n")
  # fwrite.write("Ini baris ke-5\n")
  # fwrite.write("Ini baris ke-6\n")
