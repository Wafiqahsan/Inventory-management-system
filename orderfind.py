import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("hotel")
am=[]
def finddata():
    dc=pymysql.connect(host='localhost',user='root',password='root',database='hotel')
    cur = dc.cursor()
    xl=int(en.get())
    sql="select Name,Gmail,Phone from hotel where BookID=%d"%(xl)
    cur.execute(sql)
    data=cur.fetchone()
    f.insert(0,data[0])
    g.insert(0,data[1])
    h.insert(0,data[2])
    dc.close()
kl=Label(t,text='BookID')
kl.place(x=50,y=50)
en=Entry(t,width=30)
en.place(x=200,y=50)
b=Label(t,text='Name')
b.place (x=50,y=100)
f=Entry(t,width=30)
f.place(x=200,y=100)
c=Label(t,text='Gmail')
c.place(x=50,y=150)
g=Entry(t,width=30)
g.place(x=200,y=150)
d=Label(t,text='Phone')
d.place(x=50,y=200)
h=Entry(t,width=30)
h.place(x=200,y=200)
l=Button(t,text='Find',command=finddata)
l.place(x=200,y=350)
t.mainloop()