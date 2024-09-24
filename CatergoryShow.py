import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
def show2():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Data Show')
    aa=[]
    ab=[]
    ac=[]
    ad=[]
    ae=[]
    af=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='Store')
        cur=db.cursor()
        sql="select categoryid,categoryname,description from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        global i
        for res in data:
            aa.append(res[0])
            ab.append(res[1])
            ac.append(res[2])
        db.close()
    def firstrecord():
        global i
        i=0
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        
    def nextrecord():
        global i
        i=i+1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        
    def prevrecord():
        global i
        i=i-1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        
    def lastrecord():
        global i
        i=len(aa)-1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        
    
    kl=Label(t,text='Categoryid')
    kl.place(x=50,y=50)
    en=Entry(t,width=30)
    en.place(x=200,y=50)
    b=Label(t,text='CategoryName')
    b.place (x=50,y=100)
    f=Entry(t,width=30)
    f.place(x=200,y=100)
    c=Label(t,text='Description')
    c.place(x=50,y=150)
    g=Entry(t,width=30)
    g.place(x=200,y=150)
    l=Button(t,text='first',command=firstrecord)
    l.place(x=100,y=350)
    btn=Button(t,text='next',command=nextrecord)
    btn.place(x=200,y=350)
    btc=Button(t,text='prev',command=prevrecord)
    btc.place(x=300,y=350)
    btk=Button(t,text='last',command=lastrecord)
    btk.place(x=400,y=350)
    filldata()
    t.mainloop()