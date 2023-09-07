print(".:: Program Predikis Investasi ::.\n")

saldo = int(input("Masukkan Saldo Awal (Rp.) : "))
persentase = float(input("Masukkan Persentase Keuntungan Per Tahunnya (%) : "))

tahun = int(input("Masukkan Waktu Investasi (Tahun) : "))
print("Tahun ke-\t Saldo Awal\t\t Laba Investasi\t\t Saldo Akhir")

for i in range(tahun):
  laba = saldo * (persentase/100)
  saldoAkhir = saldo + laba
  print(f"{i}\t\t {saldo}\t\t\t {laba}\t\t\t {saldoAkhir}")
  saldo = saldoAkhir