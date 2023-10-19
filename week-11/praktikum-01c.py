# Berikut adalah program untuk membaca file yang bernama "file_baru.txt"
with open("file_baru.txt", "r") as fwrite:
  counter = 0
  for l in fwrite:
    counter += 1
    print(f"{counter}: {l}",end="")
    # alasan ditambahkan end="" karena isi dari file_baru.txt sudah ada \n
  print(f"Jumlah baris dari file '{fwrite.name}' adalah {counter}")