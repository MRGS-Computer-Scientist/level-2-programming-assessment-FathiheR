import tkinter as tk
from tkinter import ttk  # Import Treeview widget

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Editable Table App")
        self.geometry("500x400")
        
        container = tk.Frame(self, bg="light blue")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, NextPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self, bg="light blue")
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        label = tk.Label(self, text="Student Tracker App", bg=bg)
        label.pack(pady=10, padx=10)
        
        button_next = tk.Button(self, text="Go to Main Page",
                                command=lambda: controller.show_frame("NextPage"))
        button_next.pack()
        
        button_exit = tk.Button(self, text="Exit", command=self.quit)
        button_exit.pack()

class NextPage(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        label = tk.Label(self, text="This is the Main Page", bg=bg)
        label.pack(pady=10, padx=10)
        
        # Creating a table (Treeview widget)
        self.tree = ttk.Treeview(self, columns=("Toilet", "Student Service", "Deans Office", "Other"))
        self.tree.heading("#0", text="Student Name")
        self.tree.heading("Toilet", text="Toilet")
        self.tree.heading("Student Service", text="Student Service")
        self.tree.heading("Deans Office", text="Deans Office")
        self.tree.heading("Other", text="Other")
        
        # Load names from file if exists
        self.load_names_from_file()
        
        self.tree.pack(pady=10, padx=10)
        
        # Enable editing when double-clicking a cell
        self.tree.bind("<Double-1>", self.on_double_click)
        
        # Entry and button for adding new names
        self.new_name_entry = tk.Entry(self)
        self.new_name_entry.pack(pady=5, padx=10)
        
        add_button = tk.Button(self, text="Add Name", command=self.add_name)
        add_button.pack()
        
        # Button for deleting selected name
        delete_button = tk.Button(self, text="Delete Name", command=self.delete_name)
        delete_button.pack()
        
        button = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
    
    def on_double_click(self, event):
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        column = column[len("#"):]  # Remove "#" from column identifier
        
        # Create Entry widget for editing
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Cell")
        
        # Get current value
        current_value = self.tree.item(item, "values")[int(column) - 1]
        
        # Entry widget to edit the value
        entry = tk.Entry(edit_window)
        entry.insert(0, current_value)
        entry.pack(padx=10, pady=10)
        
        # Save button to save the edited value
        save_button = tk.Button(edit_window, text="Save", command=lambda: self.save_edit(item, column, entry.get(), edit_window))
        save_button.pack()
    
    def save_edit(self, item, column, new_value, edit_window):
        # Update the Treeview item with the new value
        index = int(column) - 1  # Convert column index to Treeview values index
        values = list(self.tree.item(item, "values"))
        values[index] = new_value
        self.tree.item(item, values=tuple(values))
        edit_window.destroy()
        
        # Save updated names to file
        self.save_names_to_file()
    
    def load_names_from_file(self):
        try:
            with open("names.txt", "r") as file:
                for name in file:
                    name = name.strip()
                    if name:
                        self.tree.insert("", "end", text=name, values=("0", "0", "0", "0"))
        except FileNotFoundError:
            pass  # File will be created when names are added
    
    def save_names_to_file(self):
        with open("names.txt", "w") as file:
            for item in self.tree.get_children():
                name = self.tree.item(item, "text")
                file.write(name + "\n")
    
    def add_name(self):
        new_name = self.new_name_entry.get().strip()
        if new_name:
            self.tree.insert("", "end", text=new_name, values=("0", "0", "0", "0"))
            self.new_name_entry.delete(0, tk.END)  # Clear the entry field
            
            # Save names to file immediately after adding
            self.save_names_to_file()
    
    def delete_name(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
        
        # Save names to file immediately after deleting
        self.save_names_to_file()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
