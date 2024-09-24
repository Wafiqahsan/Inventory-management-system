import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
def upd2():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("STORE")
    am=[]
    def filldata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur = dc.cursor()
        sql="select storeid from storeinfo"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            am.append(res[0])
        dc.close() 
    def updatedata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur = dc.cursor()
        xa=int(en.get())
        xb=f.get()
        xc=g.get()
        sql="insert into productcategory values (%d,'%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        dc.commit()
        messagebox.showinfo('hi','DATA SAVED')
        dc.close()
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
    kl=Label(t,text='ProdcutID')
    kl.place(x=50,y=50)
    en=Entry(t,width=30)
    en.place(x=200,y=50)
    b=Label(t,text='Categoryname')
    b.place (x=50,y=100)
    f=Entry(t,width=30)
    f.place(x=200,y=100)
    c=Label(t,text='Description')
    c.place(x=50,y=150)
    g=Entry(t,width=30)
    g.place(x=200,y=150)
    bt=Button(t,text='Update',command=updatedata)
    bt.place(x=100,y=350)
    t.mainloop()