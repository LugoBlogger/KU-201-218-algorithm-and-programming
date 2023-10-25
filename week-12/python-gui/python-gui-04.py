import tkinter 

top = tkinter.Tk()

# callback function
def display():
  messageLabel.configure(text="Hello World")

messageLabel = tkinter.Label(top, text="", width=12)
messageLabel.grid(row=0, column=0)

showButton = tkinter.Button(top, text="Show",
  command=display)
showButton.grid(row=0, column=1)

quitButton = tkinter.Button(top, text="Quit", 
  command=top.destroy)
quitButton.grid(row=0, column=2)

tkinter.mainloop()


