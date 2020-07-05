import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
    
def func(event):
    if entry1.get() and entry2.get() and entry3.get() and entry4.get() != None:
        messagebox.showinfo("Completed","Database has been successfully updated!")
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
    else: 
        print("Missing entry.")
        
window.bind('<Return>', func)

entry1 = tk.Entry(width=40, bg="white", fg="black")
entry2 = tk.Entry(width=40, bg="white", fg="black")
entry3 = tk.Entry(width=40, bg="white", fg="black")
entry4 = tk.Entry(width=40, bg="white", fg="black")

entry1.insert(0, "Item Name:")
entry2.insert(0, "Type of Item:")
entry3.insert(0, "Date of Purchase:")
entry4.insert(0, "Price:")

entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()

window.mainloop()