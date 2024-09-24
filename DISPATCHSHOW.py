import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
def shower():
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
        sql="select DispatchNO,orderID,CutomerID,ProductID,QTY,Billamount from dispatch"
        cur.execute(sql)
        data=cur.fetchall()
        global i
        for res in data:
            aa.append(res[0])
            ab.append(res[1])
            ac.append(res[2])
            ad.append(res[3])
            ae.append(res[4])
            af.append(res[5])
        db.close()
    def firstrecord():
        global i
        i=0
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        h.insert(0,ad[i])
        la.insert(0,ae[i])
        he.insert(0,af[i])
    def nextrecord():
        global i
        i=i+1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        h.insert(0,ad[i])
        la.insert(0,ae[i])
        he.insert(0,af[i])
    def prevrecord():
        global i
        i=i-1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        h.insert(0,ad[i])
        la.insert(0,ae[i])
        he.insert(0,af[i])
    def lastrecord():
        global i
        i=len(aa)-1
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
        en.insert(0,aa[i])
        f.insert(0,ab[i])
        g.insert(0,ac[i])
        h.insert(0,ad[i])
        la.insert(0,ae[i])
        he.insert(0,af[i])
        
    
    kl=Label(t,text='DispatchNO')
    kl.place(x=50,y=50)
    en=Entry(t,width=30)
    en.place(x=200,y=50)
    b=Label(t,text='orderID')
    b.place (x=50,y=100)
    f=Entry(t,width=30)
    f.place(x=200,y=100)
    c=Label(t,text=' CustomerID')
    c.place(x=50,y=150)
    g=Entry(t,width=30)
    g.place(x=200,y=150)
    d=Label(t,text='ProductID')
    d.place(x=50,y=200)
    h=Entry(t,width=30)
    h.place(x=200,y=200)
    j=Label(t,text='QTY')
    j.place(x=50,y=250)
    la=Entry(t,width=30)
    la.place(x=200,y=250)
    k=Label(t,text='Billamount')
    k.place(x=50,y=300)
    he=Entry(t,width=30)
    he.place(x=200,y=300)
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