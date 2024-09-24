import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
import tkinter as tk
from storeinfofinddata import *
from storeinfoshow import *
from storeinfodeleter import *
from storeinfoupdater import *
from Storeinfosavedata import *
from storeinfoShowall import *
from scorder import *
from SCDISPATCH import *
from SCSUPPLY import *
from sc2 import *
from Sc3 import *
from sc1 import *
from SCSTOCKIN import *
window = tk.Tk()
window.title("Inventory Management Dashboard")
window.geometry("800x800")
window.configure(bg='darkturquoise') 
store_info_button = tk.Button(window, text="Store Info",command=dash1)
store_info_button.place(x=150,y=100)
product_category_button = Button(window, text="Product Category",command=dash)
product_category_button.place(x=150,y=200)
products_button =Button(window, text="Products",command=dash3)
products_button.place(x=150,y=300)
supplies_button =Button(window, text="Supplies",command=dashsu)
supplies_button.place(x=150,y=400)
stockin_button =Button(window, text="Stockins",command=dashst)
stockin_button.place(x=150,y=500)
orders_button = tk.Button(window, text="Orders",command=dash4)
orders_button.place(x=150,y=600)
dispatch_button = tk.Button(window, text="Dispatch",command=dashdis)
dispatch_button.place(x=150,y=700)

window.mainloop()