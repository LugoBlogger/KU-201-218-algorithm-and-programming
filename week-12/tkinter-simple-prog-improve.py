# Menggunakan module Tkinter
# Di dalam slide seharusnya tkinter bukan Tkinter.``
import tkinter
import tkinter.font

# Membuat top-level window
top = tkinter.Tk()

# Mengatur ukuran top-level window
top.geometry("500x500")  # dalam ukuran pixel

# Membuat tombol
quit_button = tkinter.Button(top, text="Keluar", command=top.destroy, 
                              font=("Arial", 30), background="#B70404", 
                              foreground="#FFE569")

# Mengubah font
my_font = tkinter.font.Font(size=30)
quit_button["font"] = my_font

# quit_button.grid()
# quit_button.place(x=250, y=250, anchor=tkinter.CENTER, height=200, width=200)
# quit_button.place(x=250, y=250, anchor=tkinter.CENTER)
quit_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Mulai main loop
tkinter.mainloop()
