# Pertemuan Minggu 12

**Tujuan**: Mahasiswa mampu membuat _Graphical User 
Interface_ (GUI) sederhana dengan menggunakan
Tkinter dan PyQt


### Subtopik yang akan dibahas

## [12.1 Konsep Graphical User Interface](#subtopik-yang-akan-dibahas)

## [12.2 Penggunaan module `tkinter`](#subtopik-yang-akan-dibahas)

Contoh sederhana program GUI di Python   
**`python-gui-01.py`**  
```py
# Use the tkinter module
import tkinter 

# Create the top-level (or root) window
top = tkinter.Tk()

# Create a button ... 
quitButton = tkinter.Button(top, text="Quit", 
  command=top.destroy)
# ... and display it in the window
quitButton.grid()

# Start the main loop: responds to the mouse etc. 
tkinter.mainloop()
```

## [12.3 Event-driven programming](#subtopik-yang-akan-dibahas)

## [12.4 Melanjutkan program `python-gui-01.py`](#subtopik-yang-akan-dibahas)

### Istilah-istilah

### Mengubah _layout_

### Menerima masukan dari _user_

### Hal penting tentang `Entry` widget

## [12.5 Contoh program dengan _radio button_](#subtopik-yang-akan-dibahas)

## [12.5 Contoh program pemeriksa _palindrome_](#subtopik-yang-akan-dibahas)

Meskipun konsep palindrome sangat abstrak, namun sebenarnya ada salah
satu manfaatnya dalam menganalisa DNA (masuk dalam kategori bioinformatika).
Lebih lengkap lihat [_Palindrome sequence_](https://en.wikipedia.org/wiki/Palindromic_sequence)

### Mendefinisikan fungsi _palindrome_

### Pengaturan _window_ dan _widgets_

### Penambahan `Entry` widgets

### Mendefinisikan fungsi _callback_ untuk tombol Check

### Menambahkan beberapa output

### Merenungkan terkait _design_

Melakukan design suatu tampilan program bukanlah hal yang sederhana.
Cara termudah adalah melihat program yang sudah ada di pasaran.
Namun para profesional telah mengembangkan suatu cara yang efisien untuk
mendesign suatu program menggunakan _design system_.

