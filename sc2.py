from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
import tkinter as tk
from categoryDeleter import *
from categoryfindata import *
from categorysaver import *
from CategoryUpdater import*
from Categoryshow import *
from CatergoryShow import *
def dash():
    window = tk.Tk()
    window.title("Inventory Management Dashboard")
    window.geometry("400x300")
    window.configure(bg='teal') 
    
    insert_button = tk.Button(window, text="Insert",command=sav2)
    insert_button.place(x=20,y=100)
    
    update_button = tk.Button(window, text="Update",command=upd2)
    update_button.place(x=90,y=100)
    
    show_button = tk.Button(window, text="Show",command=show2)
    show_button.place(x=150,y=100)
    
    show_all_button = tk.Button(window, text="Show All",command=sh2)
    show_all_button.place(x=200,y=100)
    
    delete_button = tk.Button(window, text="Delete",command=dele2)
    delete_button.place(x=270,y=100)
    
    find_button = tk.Button(window, text="find",command=fand2)
    find_button.place(x=320,y=100)
    
    window.mainloop()