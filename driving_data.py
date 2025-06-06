import tkinter as tk
from tkinter import ttk

class SimpleEditableTree:
    def __init__(self, root):
        self.root = root
        
        self.tree = ttk.Treeview(root, columns=('Toyota', 'Yaris', '2013'), show='headings')
        self.tree.pack(pady=10)
        
        for col in ('Toyota', 'Yaris', '2013'):
            self.tree.heading(col, text=f'{col}')
            self.tree.column(col, width=100)
        
        self.tree.insert('', 'end', values=('test1', 'test2', '2013'))
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        tk.Label(frame, text="Redigera:").grid(row=0, column=0)
        self.entries = []
        for i in range(3):
            entry = tk.Entry(frame, width=15)
            entry.grid(row=0, column=i+1, padx=5)
            self.entries.append(entry)
        
        tk.Button(frame, text="Uppdatera", command=self.update_selected).grid(row=0, column=4, padx=10)
        tk.Button(frame, text="Lägg till", command=self.add_row).grid(row=0, column=5, padx=5)
        
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
    
    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = self.tree.item(item, 'values')
            for i, entry in enumerate(self.entries):
                entry.delete(0, tk.END)
                entry.insert(0, values[i] if i < len(values) else '')
    
    def update_selected(self):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            new_values = [entry.get() for entry in self.entries]
            self.tree.item(item, values=new_values)
    
    def add_row(self):
        new_values = [entry.get() for entry in self.entries]
        self.tree.insert('', 'end', values=new_values)
        for entry in self.entries:
            entry.delete(0, tk.END)

root = tk.Tk()
app = SimpleEditableTree(root)
root.mainloop()