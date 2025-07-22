import tkinter as tk
from tkinter import ttk
from datetime import date
import csv

class SimpleEditableTree:

    # instance variables
    totalDistance = 0.0
    previousTotalDistance = 0.0
    distanceDiff = 0.0
    totalFuel = 0.0
    currentPrice = 0.0
    avgFuel = 0.0
    date = date.today()
    fileName = "driving_data.csv"

    columns = ('Datum', 'Miltal', 'Tankat (L)', 'Pris (kr/L)', 'Forbrukning (L/Mil)')

    def __init__(self, root):

        # display
        self.root = root
        self.root.title("Fuel Data")
        self.tree = ttk.Treeview(root, columns=self.columns, show='headings')
        self.tree.pack(pady=10)
        headers = {
            'Datum': 'Datum',
            'Miltal': 'Miltal',
            'Tankat (L)': 'Tankat (L)',
            'Pris (kr/L)': 'Pris (kr/L)',
            'Forbrukning (L/Mil)': 'Forbrukning (L/Mil)',
        }
        
        for col in self.columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=200) 
                
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        self.entries = []
        for i in range(3):
            entry = tk.Entry(frame, width=15)
            entry.grid(row=0, column=i+1, padx=5)
            self.entries.append(entry)
        
        tk.Button(frame, text="Lägg till", command=self.add_row).grid(row=0, column=8, padx=5)
        tk.Button(frame, text="Uppdatera", command=self.update_selected).grid(row=0, column=9, padx=5)
        tk.Button(frame, text="Radera rad", command=self.delete_selected).grid(row=0, column=10, padx=5)
        tk.Button(frame, text="Rensa allt", command=self.clear_rows).grid(row=0, column=11, padx=5)
        
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = self.tree.item(item, 'values')
            for i, entry in enumerate(self.entries):
                entry.delete(0, tk.END)
                entry.insert(0, values[i+1] if i+1 < len(values) else '')
    
    def update_selected(self):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            old_values = self.tree.item(item, 'values')
            new_values = [old_values[0]] + [entry.get() for entry in self.entries]
            try:
                current_distance = float(new_values[1])
                fuel = float(new_values[2])
                items = self.tree.get_children()
                index = items.index(item)
                if index > 0:
                    prev_item = items[index - 1]
                    prev_values = self.tree.item(prev_item)['values']
                    prev_distance = float(prev_values[1])
                    distance_diff = current_distance - prev_distance
                    avg = round(fuel / distance_diff if distance_diff > 0 else 0.0, 2)
                else:
                    avg = "N/A"
                new_values.append(avg)
            except (ValueError, TypeError):
                new_values.append(0.0)
            self.tree.item(item, values=new_values)
            self.update_totals()
            self.save_to_csv()

    def add_row(self):
        new_values = [self.date] + [entry.get() for entry in self.entries]
        try:
            current_distance = float(new_values[1])
            fuel = float(new_values[2])
            items = self.tree.get_children()
            if items:
                prev_item = items[-1]
                prev_values = self.tree.item(prev_item)['values']
                prev_distance = float(prev_values[1])
                distance_diff = current_distance - prev_distance
                avg = round(fuel / distance_diff if distance_diff > 0 else 0.0, 2)
            else:
                avg = "N/A"  # first row with no previous row
            new_values.append(avg)
        except (ValueError, TypeError):
            new_values.append(0.0)
        self.tree.insert('', 'end', values=new_values)
        self.latest_row_values = new_values # save current row in variable
        
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.update_totals()
        self.save_to_csv()

    def update_totals(self):
        items = self.tree.get_children()
        if len(items) > 0:

            # get previous row
            latest_item = items[-1]
            latest_values = self.tree.item(latest_item)['values']
            
            try:
                # new total
                self.totalDistance = float(latest_values[1])
                self.totalFuel = float(latest_values[2])
                
                # calc distance diff
                self.distanceDiff = round(self.totalDistance - self.previousTotalDistance, 2)
                
                # calc new consumption based on new total and distance diff
                self.avgFuel = round((self.totalFuel / self.distanceDiff if self.distanceDiff > 0 else 0.0), 2)
                
                # upd previousTotalDistance for next calc
                self.previousTotalDistance = self.totalDistance
                
            except (ValueError, TypeError):
                self.totalDistance = 0.0
                self.totalFuel = 0.0
                self.distanceDiff = 0.0
                self.avgFuel = 0.0

    def update_avg_consumption(self, new_value):
        self.avgFuel = new_value

    def clear_rows(self):
        allRows = self.tree.get_children()
        for row in allRows:
            self.tree.delete(row)

    def save_to_csv(self):
        with open(self.fileName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.latest_row_values) # append latest row to file    

    def delete_selected(self):
        selection = self.tree.selection()
        print(selection)
        for item in selection:
            self.tree.delete(item)
            
root = tk.Tk()
app = SimpleEditableTree(root)
root.mainloop()