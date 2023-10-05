from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.ttk import Combobox
import random as rd
from sqlite3 import *
from datetime import datetime
import time

win=Tk()
win.state("zoomed")
win.configure(bg='skyblue')
win.resizable(width=False,height=False)

title_lbl=Label(win,text='Restaurant Billing System',font=('',55,'bold','underline'),bg='skyblue')
title_lbl.place(relx=.2,rely=.05)

img1=PhotoImage(file="logo1.png")
img2=PhotoImage(file="logo2.png")

logo_lbl1=Label(win,image=img1)
logo_lbl1.place(x=0,y=0)

logo_lbl2=Label(win,image=img2)
logo_lbl2.place(relx=.85,y=0)


def home_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    user_label=Label(frm,text="Username",font=('',20,'bold'),bg='pink')
    user_entry=Entry(frm,font=('',20,'bold'),bd=10)
    user_entry.focus()

    pass_label=Label(frm,text="Password",font=('',20,'bold'),bg='pink')
    pass_entry=Entry(frm,show="*",font=('',20,'bold'),bd=10)
    
    
    login_btn=Button(frm,command=lambda:auth(),width=8,text="login",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="reset",font=('',20,'bold'),bd=10)

    user_label.place(relx=.3,rely=.2)
    user_entry.place(relx=.45,rely=.2)
    
    pass_label.place(relx=.3,rely=.3)
    pass_entry.place(relx=.45,rely=.3)

    login_btn.place(relx=.35,rely=.45)
    reset_btn.place(relx=.5,rely=.45)
    
    def reset_home():
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        user_entry.focus()

    def auth():
        u=user_entry.get()
        p=pass_entry.get()
        if(len(u)==0 or len(p)==0):
            messagebox.showwarning('Validation',"Username/Password cann't be empty")
        else:
            if(u=='admin' and p=='admin'):
                frm.destroy()
                welcome_screen()
            else:
                 messagebox.showerror('Validation',"Invalid Username/Password")


def welcome_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    billing_btn=Button(frm,command=lambda:billing(),width=12,text="Billing",font=('',20,'bold'),bd=10)
    billing_btn.place(relx=.4,rely=.1)

    addItem_btn=Button(frm,command=lambda:addItem(),width=12,text="Add Item",font=('',20,'bold'),bd=10)
    addItem_btn.place(relx=.4,rely=.25)

    editPrice_btn=Button(frm,command=lambda:editPrice(),width=12,text="Edit Price",font=('',20,'bold'),bd=10)
    editPrice_btn.place(relx=.4,rely=.4)

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()
               
    
    def addItem():
        frm.destroy()
        additem_screen()
    
    def editPrice():
        frm.destroy()
        editprice_screen()
    
    def billing():
        frm.destroy()
        billing_screen()
    
def additem_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    title_lbl=Label(frm,text="Add Item",font=('',50,'bold','italic'),bg='pink',fg='green')
    title_lbl.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)


    item_label=Label(frm,text="Item Name",font=('',20,'bold'),bg='pink')
    item_entry=Entry(frm,font=('',20,'bold'),bd=10)
    item_entry.focus()

    price_label=Label(frm,text="Price/Unit",font=('',20,'bold'),bg='pink')
    price_entry=Entry(frm,font=('',20,'bold'),bd=10)
    
    
    login_btn=Button(frm,command=lambda:addItem_db(),width=8,text="Add",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="reset",font=('',20,'bold'),bd=10)

    item_label.place(relx=.3,rely=.2)
    item_entry.place(relx=.45,rely=.2)
    
    price_label.place(relx=.3,rely=.3)
    price_entry.place(relx=.45,rely=.3)

    login_btn.place(relx=.35,rely=.45)
    reset_btn.place(relx=.5,rely=.45)

    def addItem_db():
        con=connect("restaurant.db")
        cur=con.cursor()
        it_name=item_entry.get().upper()
        it_price=price_entry.get()
        try:
            cur.execute("insert into items values(?,?)",(it_name,it_price))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Item Added..")
        except:
            messagebox.showwarning("Fail","Try with different Item..")
        
    def reset_home():
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        user_entry.focus()

    def back():
        frm.destroy()
        welcome_screen()
    
    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()


def editprice_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    title_lbl=Label(frm,text="Edit Price",font=('',50,'bold','italic'),bg='pink',fg='green')
    title_lbl.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)

    con=connect('restaurant.db')
    cur=con.cursor()
    cur.execute("select item_name,item_price_unit from items")
    rows=cur.fetchall()
    items=[]
    for row in rows:
        items.append(row[0])

    con.close()

    
    user_label=Label(frm,text="Select Item",font=('',20,'bold'),bg='pink')
    user_entry=Combobox(frm,font=('',20,'bold'),values=items)
    user_entry.current(0)
    
    pass_label=Label(frm,text="Set Price",font=('',20,'bold'),bg='pink')
    pass_entry=Entry(frm,font=('',20,'bold'),bd=10)
    
    def select_item(event):
        item=user_entry.get()
        con=connect('restaurant.db')
        cur=con.cursor()
        cur.execute("select item_price_unit from items where item_name=?",(item,))
        row=cur.fetchone()
        iprice=row[0]
        pass_entry.delete(0,END)
        pass_entry.insert(0,str(iprice))
        con.close()
        
    user_entry.bind('<<ComboboxSelected>>',select_item)

    login_btn=Button(frm,command=lambda:updatePrice_db(),width=8,text="Update",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="reset",font=('',20,'bold'),bd=10)

    user_label.place(relx=.3,rely=.2)
    user_entry.place(relx=.45,rely=.2)
    
    pass_label.place(relx=.3,rely=.3)
    pass_entry.place(relx=.45,rely=.3)

    login_btn.place(relx=.35,rely=.45)
    reset_btn.place(relx=.5,rely=.45)

    def updatePrice_db():
        item=user_entry.get()
        price=pass_entry.get()
        con=connect("restaurant.db")
        cur=con.cursor()
        cur.execute("update items set item_price_unit=? where item_name=?",(price,item))
        con.commit()
        con.close()
        messagebox.showinfo("Success","Price updated")
    
    def reset_home():
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        user_entry.focus()


    def back():
        frm.destroy()
        welcome_screen()

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()

def billing_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    title_lbl=Label(frm,text="Billing",font=('',50,'bold','italic'),bg='pink',fg='green')
    title_lbl.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)

    con=connect('restaurant.db')
    cur=con.cursor()
    cur.execute("select item_name,item_price_unit from items")
    rows=cur.fetchall()
    items=[]
    for row in rows:
        items.append(row[0])

    con.close()

    item_label=Label(frm,text="Select Item",font=('',15,'bold'),bg='pink')
    item_entry=Combobox(frm,font=('',15,'bold'),values=items)
    item_entry.current(0)

    qty_label=Label(frm,text="Select Qty",font=('',15,'bold'),bg='pink')
    qty_entry=Combobox(frm,font=('',15,'bold'),values=[1,2,3])
    qty_entry.current(0)
    
    add_btn=Button(frm,command=lambda:add_item_to_details(),width=8,text="add",font=('',15,'bold'),bd=5)
    delete_btn=Button(frm,command=lambda:delete_item_to_details(),width=8,text="delete",font=('',15,'bold'),bd=5)

    items_frm=Frame(frm,bg='white')
    items_frm.place(relx=.39,rely=.15,width=800,height=400)

    item_details=Label(items_frm,text="Billing Items",font=('',15,'bold'),bg='white',fg='red')
    item_details.pack()

    bill_btn=Button(items_frm,command=lambda:final_bill(),width=5,text="Bill",font=('',15,'bold'),bd=5)
    bill_btn.pack(side='bottom',anchor='e',padx=20,pady=20)

    Label(items_frm,text="Item",font=('',13,'bold'),bg='white',fg='black').place(relx=.05,rely=.07)
    Label(items_frm,text="Qty",font=('',13,'bold'),bg='white',fg='black').place(relx=.35,rely=.07)
    Label(items_frm,text="Price/Unit",font=('',13,'bold'),bg='white',fg='black').place(relx=.65,rely=.07)
    Label(items_frm,text="Amount",font=('',13,'bold'),bg='white',fg='black').place(relx=.9,rely=.07)

    date=time.ctime()
    Label(items_frm,text=f"{date}",font=('',13,'bold'),bg='white',fg='blue').place(relx=.01,rely=0)

    item_label.place(relx=.1,rely=.2)
    item_entry.place(relx=.2,rely=.2)
    
    qty_label.place(relx=.1,rely=.3)
    qty_entry.place(relx=.2,rely=.3)

    add_btn.place(relx=.15,rely=.45)
    delete_btn.place(relx=.25,rely=.45)

    billed_items={}

    def add_item_to_details():
        item=item_entry.get()
        qty=qty_entry.get()
        con=connect('restaurant.db')
        cur=con.cursor()
        cur.execute("select item_price_unit from items where item_name=?",(item,))
        row=cur.fetchone()
        price=row[0]
        con.close()
        billed_items[item]=[qty,price,int(qty)*price]
        show_billed_items()

    def delete_item_to_details():
        item=item_entry.get()
        try:
            billed_items.pop(item)
            show_billed_items()
        except:
            messagebox.showwarning("Fail","Item not found")

    def show_billed_items():
        y=0
        for item in billed_items:
            Label(items_frm,text=item,bg='white',fg='blue',font=('',10)).place(relx=.05,rely=.15+y)
            qty_price_amt=billed_items.get(item)
            x=0
            for val in qty_price_amt:
                Label(items_frm,text=str(val),bg='white',fg='blue',font=('',10)).place(relx=.35+x,rely=.15+y)
                x=x+.3
            y=y+.08


    def final_bill():
        amt=0
        for item in billed_items:
            amt=amt+billed_items.get(item)[-1]
        final_amt=amt+(5*amt)/100
        #messagebox.showinfo("Your Bill:",f"Total Bill:{final_amt}")
        Label(items_frm,text=f"Total Bill:Rs. {amt}",bg='white',fg='black',font=('',14,'bold')).place(relx=.65,rely=.65)
        Label(items_frm,text=f"Total Bill with 5% GST: Rs.{final_amt}",bg='white',fg='black',font=('',14,'bold')).place(relx=.65,rely=.75)
            
    
    def reset_home():
        item_entry.delete(0,END)
        qty_entry.delete(0,END)
        item_entry.focus()


    def back():
        frm.destroy()
        welcome_screen()

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()


home_screen()
win.mainloop()
