import tkinter 

top = tkinter.Tk()

messageLabel = tkinter.Label(top, text="Hello World!")
messageLabel.grid()

quitButton = tkinter.Button(top, text="Quit", 
  command=top.destroy)
quitButton.grid()

tkinter.mainloop()
