import tkinter 

top = tkinter.Tk()

# callback function
def display():
  name = textVar.get()
  messageLabel.configure(text="Hello " + name)

textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top, textvariable=textVar, width=12)
textEntry.grid(row=0, column=0)

messageLabel = tkinter.Label(top, text="", width=12)
messageLabel.grid(row=1, column=0)

showButton = tkinter.Button(top, text="Show",
  command=display)
showButton.grid(row=1, column=1)

quitButton = tkinter.Button(top, text="Quit", 
  command=top.destroy)
quitButton.grid(row=1, column=2)

tkinter.mainloop()



