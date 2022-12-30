from tkinter import *
from tkinter import  messagebox
import tempfile
import os
import random


win = Tk()
win.title('billing management system')
win.geometry('1360x1080')
bg='orange'

#------------------------------<variables>--------------------------------------
Total=IntVar()
cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()

c_name=StringVar()
c_phone=StringVar()
c_email=StringVar()
item=StringVar()
Rate=IntVar()
Quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))

global l
l=[]

# ===========Function===============

def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,'\t Welcome hye-hi-hello Service Center')
    textarea.insert(END,f'\n\n Bill Number:\t\t{bill_no.get()}')
    textarea.insert(END,f'\n Customer Name:\t\t{c_name.get()}')
    textarea.insert(END,f'\n Phone Number:\t\t{c_phone.get()}')
    textarea.insert(END,f'\n Email ID:\t\t{c_email.get()}')
    textarea.insert(END,f'\n=======================================')
    textarea.insert(END,f'\n Product\t\t QTY\t\t Price')
    textarea.insert(END,f'\n=======================================\n')
    textarea.configure(font='arial 12 bold')

def total():
    n=Rate.get()
    m=Quantity.get()*n
    l.append(m)
    if item.get()=='':
        messagebox.showerror('Error','Please Enter the item')
    else:
        textarea.insert((11.0+float(len(l)-1)),f'\n{item.get()}\t\t{Quantity.get()}\t\t{m}')
        
def gbill():
    if c_name.get()=='' or c_phone.get()=='' or c_email.get()=='':
        messagebox.showerror('Error','Customer Details are must')
    else:
        text=textarea.get(11.0,(11.0+float(len(l))))
        welcome()
        textarea.insert(END,text)
        textarea.insert(END,f'\n======================================')
        textarea.insert(END,f'\nTotal Paybill Amount:\t\t\t{sum(l)}')
        textarea.insert(END,f'\n======================================')
        
        
def save():
    data=textarea.get(1.0,END)
    f1=open('records/'+str(bill_no.get())+'.txt','w')
    f1.write(data)
    f1.close()
    messagebox.showinfo('Saved',f'Bill no:{bill_no.get()} Saved successfully')
    
def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')

def reset():
    textarea.delete(1.0,END)
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        win.destroy()



#----------------------------------------Top Section-----------------------------------------------------------------------------------------
title=Label(win,text='Billing Management Software',bg='orange',width=67,height= 1,fg='gold',font=("arial",25,'bold'),relief=GROOVE,bd=10)
title.place(x=1,y=0)


#-------------------------------------------Customer Details---------------------------------------------------------------------------------


F1=LabelFrame(win,text='Customer Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,bg='orange',fg='gold')
F1.place(x=0,y=60,relwidth=1)


L1=Label(F1,text='Customer Name',font=('times new rommon',18,'bold'),bg='orange',fg='gold',relief=GROOVE,bd=5)
L1.grid(row=0,column=0,padx=10,pady=5)
L1=Entry(F1,width=15,font='arial 15 bold',bg='orange',fg='black',relief=SUNKEN,bd=5,textvariable=c_name)
L1.grid(row=0,column=1,padx=10,pady=5)

L2=Label(F1,text='Phone NO',font=('times new rommon',18,'bold'),bg='orange',fg='gold',relief=GROOVE,bd=5)
L2.grid(row=0,column=2,padx=10,pady=5)
L2=Entry(F1,width=15,font='arial 15 bold',bg='orange',relief=SUNKEN,bd=5,textvariable=c_phone)
L2.grid(row=0,column=3,padx=10,pady=5)

L3=Label(F1,text='Email ID',font=('time new rommon',18,'bold'),relief=GROOVE,bd=5,bg='orange',fg='gold')
L3.grid(row=0,column=4,padx=10,pady=5)
L3=Entry(F1,width=30,font='arial 15 bold',bg='orange',relief=SUNKEN,bd=5,textvariable=c_email)
L3.grid(row=0,column=5,padx=10,pady=5)


#---------------------------------------Product Details-----------------------------------------------------------------

F2=LabelFrame(win,text='Product Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,bg='orange',fg='gold')
F2.place(x=1,y=150,width=800,height=470)

itm=Label(F2,text='Product Name',font=('times new rommon',18,'bold',),bg='orange',fg='gold',relief=GROOVE,bd=7)
itm.grid(row=0,column=0,padx=30,pady=60)
itm_txt=Entry(F2,width=20,font='arial 15 bold',bg='orange',textvariable=item,relief='sunken',bd=7)
itm_txt.grid(row=0,column=1,padx=30,pady=20)

rate=Label(F2,text='Product Rate',font=('times new rommon',18,'bold',),bg='orange',fg='gold',relief=GROOVE,bd=7)
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold',bg='orange',textvariable=Rate,relief='sunken',bd=7)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

quantity=Label(F2,text='Product Quantity',font=('times new rommon',18,'bold',),bg='orange',fg='gold',relief=GROOVE,bd=7)
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold',bg='orange',textvariable=Quantity,relief='sunken',bd=7)
quantity_txt.grid(row=2,column=1,padx=30,pady=60)

b1 = Button(F2, text='Save', font='arial 15 bold',bg='yellow',fg='red',width=5,relief='raise',bd=7,command=save)
b1.place(x=600,y=55,width=150,height=50)

b2 = Button(F2, text='Generate', font='arial 15 bold',bg='yellow',fg='red',width=5,relief='raise',bd=7,command=gbill)
b2.place(x=600,y=175,width=150,height=50)

b3 = Button(F2, text='Save as data', font='arial 15 bold',bg='yellow',fg='red',width=5,relief='raise',bd=7)
b3.place(x=600,y=305,width=150,height=50)

#------------------------------------------------------------------------------------------------------------------

F2=Frame(win,relief=GROOVE,bd=10,bg='orange')
F2.place(x=800,y=150,width=560,height=470)

bill_title=Label(F2,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F2,orient=VERTICAL)
textarea=Text(F2,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()
#-------------------------------------------------------Buttons--------------------------------------------------------

F3=Frame(win,relief=GROOVE,bd=10,bg='orange')
F3.place(x=1,y=615,width=1360,height=120)

b1 = Button(F3, text='Total', font='arial 20 bold', bg='yellow',fg='red',width=5,relief='raise',bd=7,command=total)
b1.place(x=60,y=30,height=50)

b2 = Button(F3, text='Receipt', font='arial 25 bold', bg='yellow',fg='red',width=10,relief='raise',bd=7,command=welcome )
b2.place(x=220,y=30,height=50)

b3 = Button(F3, text='Print', font='arial 25 bold',  bg='yellow',fg='red',width=10,relief='raise',bd=7,command=print)
b3.place(x=490,y=30,height=50)

b4 = Button(F3, text='Reset', font='arial 25 bold', bg='yellow',fg='red',width=10,relief='raise',bd=7,command=reset)
b4.place(x=760,y=30,height=50)

b5 = Button(F3, text='Exit', font='arial 25 bold',bg='yellow',fg='red',width=5,relief='raise',bd=7,command=exit)
b5.place(x=1060,y=30,height=50)

win.mainloop()




