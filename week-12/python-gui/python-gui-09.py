import tkinter
import string

# A palindrome function to check whether a string
# is a palindrome or not
def palindrome(s):   # s is a string
  t = s.lower()    # lower case all characters
  u = ""
  for x in t:
    if x in string.ascii_letters:
      u = u + x

  # u is just the letters from t
  v = ""   # reversed version of string u
  for x in u:
    v = x + v
  
  return u == v


# Add a callback function for the Check button

def check():
  text = entryVar.get()
  result = palindrome(text)
  resultLabel.configure(text=result)


font_setting = ("Ubuntu", 24)

top = tkinter.Tk()
top.title("Palindrome Checker")
top.geometry("800x100")

entryVar = tkinter.StringVar("")

entry = tkinter.Entry(top, width=48, 
  textvariable=entryVar, font=font_setting)
entry.grid(row=0, column=0, columnspan=3)

resultLabel = tkinter.Label(top, text="", width=34,
  font=font_setting)
resultLabel.grid(row=1, column=0)

checkButton = tkinter.Button(top, text="Check",
  command=check, font=font_setting)
checkButton.grid(row=1, column=1)

quitButton = tkinter.Button(top, text="Quit",
 command=top.destroy, font=font_setting)
quitButton.grid(row=1, column=2)


tkinter.mainloop()

