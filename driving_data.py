import tkinter as tk

# window
window=tk.Tk()
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

window.title("car info")
label = tk.Label(window, text="testing")
label.pack()

window.mainloop()