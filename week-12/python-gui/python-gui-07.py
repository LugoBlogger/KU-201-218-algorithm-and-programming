import tkinter

# Setting up the window and widgets

font_setting = ("Ubuntu", 24)

top = tkinter.Tk()
top.title("Palindrome Checker")
top.geometry("800x100")

entry = tkinter.Entry(top, width=48, 
  font=font_setting)
entry.grid(row=0, column=0, columnspan=3)

resultLabel = tkinter.Label(top, text="", width=34,
  font=font_setting)
resultLabel.grid(row=1, column=0)

checkButton = tkinter.Button(top, text="Check",
  font=font_setting)
checkButton.grid(row=1, column=1)

quitButton = tkinter.Button(top, text="Quit",
 command=top.destroy, font=font_setting)
quitButton.grid(row=1, column=2)


tkinter.mainloop()