print(".:: Program Luas Segitiga ::.")

pil = True

while (pil == True):
  
  # -- bagian untuk menanggulangi input alas
  try:
    alas = input("Alas: ")   # menerima input dari user
    alas = float(alas)       # mengubah input menjadi desimal
    if alas < 0:
      raise AssertionError()
  except ValueError:
    print("Nilai yang ada masukkan bukan berupa angka, nilai 1 akan dimasukkan sebagai nilai alas")
    alas = 1
  except AssertionError:
    print("Nilai alas tidak boleh negatif")
    alas = abs(alas)
  else:
    print("Alas yang anda masukkan sudah benar dan akan diproses")
    print("Nilai alas yang dimasukkan: ", alas)


  try:
    pass
  except ValueError:
    pass
  except AssertionError:
    pass
  else:
    pass


  # luas = alas*tingg*0.5

  # while (pilihan != 'y' and pilihan != 't'):
  #   pass
