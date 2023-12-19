from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser

def make_app(lista,fecha='',url='https://dolarhoy.com/'):
  root = tk.Tk()
  root.title('dolardb')
  # root.geometry('500x500')
  
  date_act = ttk.Label(root,text=fecha) 
  date_act.grid(row=1)

  def callback():
    webbrowser.open_new(url)
  
  more_info = ttk.Label(root,text='More info') 
  more_info.grid(row=2)
  more_info.bind("<Button-1>", lambda e: callback())


  my_tree = ttk.Treeview(root)

  #Defino mis columnas
  my_tree['columns'] = ('Tipo_dolar', 'Compra','Venta')

  #Formato de mis columnas
  my_tree.column('#0', width=0, stretch=NO) #minwidth es el minimo ancho que puede tomar mi columna
  my_tree.column('Tipo_dolar', anchor=W, width=120)
  my_tree.column('Compra',anchor=CENTER,width=80)
  my_tree.column('Venta',anchor=E,width=80)

  #Create Headings
  my_tree.heading('#0',text='Label',anchor=W)
  my_tree.heading('Tipo_dolar',text='Tipo de Dolar',anchor=W)
  my_tree.heading('Compra',text='Compra',anchor=CENTER)
  my_tree.heading('Venta',text='Venta',anchor=CENTER)

  #Add Data

  i=0
  for row in lista:
    my_tree.insert(parent='', index='end', iid=i,text='',values=(row[0],row[1],row[2]))
    i += 1

  '''
  my_tree.insert(parent='0', index='end', iid=1,text='',values=('Dolar azul',200,201))
  '''
  #mostrar en pantalla
  my_tree.grid(row=0,pady=5)

  root.mainloop()