import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
mydata=''
def sh2():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Data Show')
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur=db.cursor()
        sql="select Categoryid,categoryname,description from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        global mydata
        for res in data:
            mydata=mydata+str(res[0])+"\t"
            mydata=mydata+res[1]+"\t"
            mydata=mydata+res[2]+"\t"
            mydata=mydata+"\n"
        db.close()
    a=Label(t,text='Show Produdct Data ')
    a.place(x=20,y=50)
    b=Text(t,width=250,height=300)
    b.place(x=20,y=50)
    filldata()
    b.insert(tkinter.END,mydata)
    t.mainloop()