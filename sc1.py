from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
import tkinter as tk
from storeinfofinddata import *
from storeinfoShowall import *
from storeinfoupdater import *
from storeinfoshow import *
from storeinfodeleter import *
from Storeinfosavedata import *
from storeinfoshow import *
import tkinter as tk
def dash1():
    window = tk.Tk()
    window.title("Inventory Management Dashboard")
    window.geometry("400x300")
    window.configure(bg='teal') 
    
    insert_button = tk.Button(window, text="Insert",command=sav1)
    insert_button.place(x=20,y=100)
    
    update_button = tk.Button(window, text="Update",command=upd1)
    update_button.place(x=90,y=100)
    
    show_button = tk.Button(window, text="Show",command=shower)
    show_button.place(x=150,y=100)
    
    show_all_button = tk.Button(window, text="Show All",command=shhhh)
    show_all_button.place(x=200,y=100)
    
    delete_button = tk.Button(window, text="Delete",command=dele)
    delete_button.place(x=270,y=100)
    
    find_button = tk.Button(window, text="find",command=fand)
    find_button.place(x=320,y=100)
    
    window.mainloop()