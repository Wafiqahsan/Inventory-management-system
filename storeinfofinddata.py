import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
def fand():
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
    def finddata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur = dc.cursor()
        xl=int(en.get())
        sql="select name,address,phone,email,regno from storeinfo where storeid=%d"%(xl)
        cur.execute(sql)
        data=cur.fetchone()
        f.insert(0,data[0])
        g.insert(0,data[1])
        h.insert(0,data[2])
        la.insert(0,data[3])
        he.insert(0,data[4])
        dc.close()
    kl=Label(t,text='Storeid')
    kl.place(x=50,y=50)
    en=Entry(t,width=30)
    en.place(x=200,y=50)
    b=Label(t,text='Name')
    b.place (x=50,y=100)
    f=Entry(t,width=30)
    f.place(x=200,y=100)
    c=Label(t,text='Address')
    c.place(x=50,y=150)
    g=Entry(t,width=30)
    g.place(x=200,y=150)
    d=Label(t,text='phone')
    d.place(x=50,y=200)
    h=Entry(t,width=30)
    h.place(x=200,y=200)
    j=Label(t,text='email')
    j.place(x=50,y=250)
    la=Entry(t,width=30)
    la.place(x=200,y=250)
    k=Label(t,text='Regno')
    k.place(x=50,y=300)
    he=Entry(t,width=30)
    he.place(x=200,y=300)
    l=Button(t,text='Find',command=finddata)
    l.place(x=200,y=350)
    t.mainloop()