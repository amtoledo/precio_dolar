import tkinter as tk
from tkinter import ttk

class Dollar_table():
  def __init__(self, dollars_list):
    super().__init__()    

    root = tk.Tk()
    root.title("Precio dolar")
    style = ttk.Style()
    style.configure("Treeview", rowheight=30)  

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=("Dollar", "Buy", "Sell"), show='headings')
    tree.heading("Dollar", text="Dolar")
    tree.heading("Buy", text="Compra")
    tree.heading("Sell", text="Venta (%)")

    tree.column("Dollar", width=500)
    tree.column("Buy", width=300)
    tree.column("Sell", width=300)  
  
    # Insert dollars data into the Treeview
    for dollars in dollars_list:
        tree.insert("", "end", values=dollars)

    tree.pack(expand=True, fill="both")
    root.mainloop()