import tkinter 
from tkinter import *
import pymysql
from tkinter import messagebox
def dele4():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("screen")
    def deletedata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='STORE')
        cur = dc.cursor()
        xa=int(e.get())
        sql="delete from supplies where suppliesID=%d"%(xa)
        cur.execute(sql)
        dc.commit()
        messagebox.showinfo('hi','DATA delete')
        dc.close()
        e.delete(0,100)
    a=Label(t,text='SuppliesID')
    a.place(x=50,y=50)
    e=Entry(t,width=30)
    e.place(x=200,y=50)
    k=Button(t,text='DELETE',command=deletedata)
    k.place(x=100,y=350)
    t.mainloop()