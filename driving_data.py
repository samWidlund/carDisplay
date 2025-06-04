import tkinter as tk
from tkinter import ttk  

# window
window=tk.Tk()
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

# variables
car_data = [
    ("Toyota", "Yaris", "2013", "15000"),
    ("Honda", "Civic", "2015", "18000"),
    ("Ford", "Focus", "2018", "20000"),
]

# treeview
tree = ttk.Treeview(window)
tree["columns"] = ("brand", "model", "year", "mileage")
tree["show"] = "headings"

# column headers n width
tree.heading("brand", text="Brand")
tree.heading("model", text="Model")
tree.heading("year", text="Year")
tree.heading("mileage", text="Mileage")
tree.column("brand", width=100)
tree.column("model", width=80)
tree.column("year", width=120)
tree.column("mileage", width=120)

# insert data into treeview
for rad in car_data:
    tree.insert("", tk.END, values=rad)

tree.pack(pady=20)

window.title("car info")

window.mainloop()