import tkinter 

# callback function
def display():
  name = textVar.get()
  choice = choiceVar.get()

  if choice == 1:
    message = "Hello " + name
  elif choice == 2:
    message = "Goodbye " + name
  else:
    message = ""
  
  messageLabel.configure(text=message)

font_setting = ("Ubuntu", 24)

top = tkinter.Tk()

textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top, textvariable=textVar, 
  font=font_setting, width=12)
textEntry.grid(row=0, column=0)

messageLabel = tkinter.Label(top, text="", 
  font=font_setting, width=16)
messageLabel.grid(row=1, column=0)

choiceVar = tkinter.IntVar(0)
helloButton = tkinter.Radiobutton(top, text="Hello",
  variable=choiceVar, value=1, command=display,
  font=font_setting)
goodbyeButton = tkinter.Radiobutton(top, text="Goodbye",
  variable=choiceVar, value=2, command=display,
  font=font_setting)
helloButton.grid(row=1, column=1)
goodbyeButton.grid(row=1, column=2)


quitButton = tkinter.Button(top, text="Quit", 
  command=top.destroy, font=font_setting)
quitButton.grid(row=1, column=3)

tkinter.mainloop()




