from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
import tkinter as tk
from orderfind import *
from OrderShow import *
from orderupd import *
from OrderDelete import *
from OrderShowall import *
from OrderSave import *
def dash4():
    window = tk.Tk()
    window.title("Inventory Management Dashboard")
    window.geometry("400x300")
    window.configure(bg='teal') 
    
    insert_button = tk.Button(window, text="Insert",command=sav5)
    insert_button.place(x=20,y=100)
    
    update_button = tk.Button(window, text="Update",command=upd4)
    update_button.place(x=90,y=100)
    
    show_button = tk.Button(window, text="Show",command=shower2)
    show_button.place(x=150,y=100)
    
    show_all_button = tk.Button(window, text="Show All",command=shh5)
    show_all_button.place(x=200,y=100)
    
    delete_button = tk.Button(window, text="Delete",command=dele4)
    delete_button.place(x=270,y=100)
    
    find_button = tk.Button(window, text="find",command=fand4)
    find_button.place(x=320,y=100)
    
    window.mainloop()