import tkinter as tk
from tkinter import ttk

class SimpleEditableTree:

    totalDistance = 0.0
    totalFuel = 0.0
    avgFuelConsumption = 0.0
    columns = ('Antal mil (mil)', 'Tankad mängd (Liter)', 'Datum', 'Medel förbrukning (L/Mil)')

    def __init__(self, root):
        self.root = root
        self.root.title("Driving Data")
        
        self.tree = ttk.Treeview(root, columns=self.columns, show='headings')
        self.tree.pack(pady=10)
        
        for col in (self.columns):
            self.tree.heading(col, text=f'{col}')
            self.tree.column(col, width=100)
        
        self.tree.insert('', 'end', values=('xxxx', 'xx,x', 'xx-xx-xx', self.avgFuelConsumption))
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        self.entries = []
        for i in range(4):
            entry = tk.Entry(frame, width=15)
            entry.grid(row=0, column=i+1, padx=5)
            self.entries.append(entry)
        
        tk.Button(frame, text="Lägg till", command=self.add_row).grid(row=0, column=6, padx=5)
        tk.Button(frame, text="Uppdatera", command=self.update_selected).grid(row=0, column=7, padx=5)
        
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
            # Calculate average for this row only
            try:
                distance = float(new_values[0])
                fuel = float(new_values[1])
                new_values[3] = round(fuel / distance if distance > 0 else 0.0, 2)
            except (ValueError, TypeError):
                new_values[3] = 0.0
            self.tree.item(item, values=new_values)
            self.update_totals()
    
    def add_row(self):
        new_values = [entry.get() for entry in self.entries]
        # Calculate average for this row only
        try:
            distance = float(new_values[0])
            fuel = float(new_values[1])
            new_values[3] = round(fuel / distance if distance > 0 else 0.0, 2)
        except (ValueError, TypeError):
            new_values[3] = 0.0
        self.tree.insert('', 'end', values=new_values)
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.update_totals()

    def update_totals(self):
        self.totalDistance = 0.0
        self.totalFuel = 0.0
        for item in self.tree.get_children():
            values = self.tree.item(item)['values']
            try:
                self.totalDistance += float(values[0])
                self.totalFuel += float(values[1])
            except (ValueError, TypeError):
                continue
        
        # calculate new average and update all rows
        self.avgFuelConsumption = round((self.totalFuel / self.totalDistance if self.totalDistance > 0 else 0.0), 2)
        
    def update_avg_consumption(self, new_value):
        self.avgFuelConsumption = new_value

root = tk.Tk()
app = SimpleEditableTree(root)
root.mainloop()