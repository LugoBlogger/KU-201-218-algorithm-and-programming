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