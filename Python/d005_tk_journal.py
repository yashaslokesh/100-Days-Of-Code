from tkinter import Tk, Text
from tkinter import ttk
from tkinter import messagebox

class Journal:

    def __init__(self, master):
        
        master.title("Daily Journal")
        master.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure("Tlabel", font = ("Avenir", 14))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, wraplength = 430, 
                  text = ("Make an entry to your journal here. You could talk about what fun activities you did today, who you met, where you visited, or even just how you enjoyed some relaxing time alone...")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = "Title:").grid(row = 0, column = 0, sticky = "w")
        ttk.Label(self.frame_content, text = "Date:").grid(row = 2, column = 0, sticky = "w")
        ttk.Label(self.frame_content, text = "Entry:").grid(row = 4, column = 0, sticky = "w")
        
        self.entry_title = ttk.Entry(self.frame_content, width = 30, font = ("Avenir", 12))
        self.entry_date = ttk.Entry(self.frame_content, width = 20, font = ("Avenir", 12))
        self.entry_text = Text(self.frame_content, width = 60, height = 20, font = ("Avenir", 12))
        
        self.entry_title.grid(row = 1, column = 0, sticky = "w")
        self.entry_date.grid(row = 3, column = 0, sticky = "w")
        self.entry_text.grid(row = 5, column = 0, columnspan = 2, sticky = "w")
        
        ttk.Button(self.frame_content, text = "Submit Journal Entry",
                   command = self.add_entry).grid(row = 6, column = 0)

    def add_entry(self):
        print(f"Title of Entry: {self.entry_title.get()}")
        print(f"Date of Entry: {self.entry_date.get()}")
        text = self.entry_text.get(1.0, "end")
        print(f"Journal entry text: {text}")

        self.clear_fields()

        messagebox.showinfo(title = "Daily Journal", message = "Journal entry submitted!")
    
    def clear_fields(self):
        self.entry_title.delete(0, "end")
        self.entry_date.delete(0, "end")
        self.entry_text.delete(1.0, "end")
         
def main():            
    
    root = Tk()
    Journal(root)
    root.mainloop()
    
if __name__ == "__main__": main()
