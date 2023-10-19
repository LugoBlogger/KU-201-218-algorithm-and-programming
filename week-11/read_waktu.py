with open("data_waktu.txt", "r") as fread:
  
  total_waktu = 0
  for baris in list(fread)[1:]:
    waktu = baris.split(",")[1]
    waktu = waktu.strip()
    waktu = waktu.split(" ")
    baris_detik = int(waktu[0])*60 + int(waktu[2])
    print(waktu, baris_detik)
    total_waktu += baris_detik
  
  print(total_waktu)