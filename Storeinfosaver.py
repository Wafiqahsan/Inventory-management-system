import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("Store")
am=[]
def finddata():
    dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
    cur = dc.cursor()
    xl=int(b.get())
    sql="select Categoryname,Description from productcategory where CategoryID=%d"%(xl)
    cur.execute(sql)
    data=cur.fetchone()
    f.insert(0,data[0])
    g.insert(0,data[1])
    dc.close()
def savedata():
    dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
    cur = dc.cursor()
    if len(b.get())==0 or len(f.get())==0 or len(g.get())==0:
        messagebox.showerror("ERROR","Should i Fill the DATA with Spaces?")
    else:
        xa=int(b.get())
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
a=Label(t,text="CategoryID")
a.place(x=30,y=40)
b=Entry(t,width=30)
b.place(x=200,y=40)
c=Label(t,text="CategoryName")
c.place(x=30,y=100)
f=Entry(t,width=30)
f.place(x=200,y=100)
e=Label(t,text="Description")
e.place(x=30,y=160)
g=Entry(t,width=30)
g.place(x=200,y=160)
btn=Button(t,text='Find',command=finddata)
btn.place(x=100,y=500)
btb=Button(t,text='Update and Save',command=savedata)
btb.place(x=250,y=500)
t.mainloop()