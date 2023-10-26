# Menggunakan module Tkinter
# Di dalam slide seharusnya tkinter bukan Tkinter.``
import tkinter

# Membuat top-level window
top = tkinter.Tk()

# Mengatur ukuran top-level window
top.geometry("500x500")  # dalam ukuran pixel

# Membuat tombol
quit_button = tkinter.Button(top, text="Keluar", command=top.destroy)
# quit_button.grid()
# quit_button.place(x=250, y=250, anchor=tkinter.CENTER, height=200, width=200)
quit_button.place(x=250, y=250, anchor=tkinter.CENTER)




# Mulai main loop
tkinter.mainloop()