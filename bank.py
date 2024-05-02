from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector


tk=Tk()
tk.title("Login")
tk.state('zoomed')
lo=Label(tk,text='',width=25,bg='#a5e7ff',fg="#a5e7ff")
lo.grid(row=0,column=0)
lab3=Label(tk,text="Welcome",bg='#a5e7ff',fg='black',font=('sans serif',60,'bold'))
lab3.place(x=900,y=130)
image=Image.open('images_bank.jpg')
resize=image.resize((550,300))
img=ImageTk.PhotoImage(resize)
la=Label(tk,image=img,highlightthickness=0,borderwidth=0,padx=0,pady=0)
la.image=img
la.place(x=800,y=280)

def login():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='first'
    )
    mycursor=mydb.cursor()
    userid=ent1.get()
    password=ent2.get()
    sql="select name from login where name= %s"
    sql2="select password from login where name= %s and password=%s"
    mycursor.execute(sql,(userid,))
    myid=mycursor.fetchall()
    mycursor.execute(sql2,(userid,password))
    mypass=mycursor.fetchall()
    print(myid)   
    print(mypass)
    print(password)
    try:
       if myid and mypass:
        messagebox.showinfo('Login',"login successful")
        tk.destroy()
        bank=Tk()
        bank.state('zoomed')
        bank.title('Bank')
        bank.config(bg='#dd6200')
        lab=Label(bank,text="ICICI BANK",fg='white',bg='#730405',font=("arial",30,'bold'))
        lab.pack(fill='x')

        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[5, 5], font=('Helvetica', 8,'bold'))
        style.configure('TNotebook', tabposition='nw',backgroundwidth=3)

        note=ttk.Notebook(bank)
        note.place(x=10,y=60)
        fr1=Frame(note,width=650,height=600)
        fr2=Frame(note,width=650,height=600)
        fr11=Frame(note,width=650,height=600)
        fr22=Frame(note,width=650,height=600)
        fr1.pack(fill='both')
        fr2.pack(fill='both')
        fr11.pack(fill='both')
        fr22.pack(fill='both')

        note.add(fr1,text='SB Account')
        note.add(fr2,text='Education Loan')
        note.add(fr11,text='Home Loan')
        note.add(fr22,text='Credit Card')
        note2=ttk.Notebook(bank)
        note2.place(x=700,y=60)

        image1=Image.open('fi1.webp')
        resize1=image1.resize((650,600))
        img1=ImageTk.PhotoImage(resize1)
        labe1=Label(fr1,image=img1)
        labe1.image=img1
        labe1.pack(expand='true',fill='both')

        image2=Image.open('second11.webp')
        resize2=image2.resize((650,600))
        img2=ImageTk.PhotoImage(resize2)
        labe2=Label(fr2,image=img2)
        labe2.image=img2
        labe2.pack(expand='true',fill='both')
 
        image3=Image.open('third1.jpg')
        resize3=image3.resize((650,600))
        img3=ImageTk.PhotoImage(resize3)
        labe3=Label(fr11,image=img3)
        labe3.image=img3
        labe3.pack(expand='true',fill='both')

        image4=Image.open('four11.webp')
        resize4=image4.resize((650,600))
        img4=ImageTk.PhotoImage(resize4)
        labe4=Label(fr22,image=img4)
        labe4.image=img4
        labe4.pack(expand='true',fill='both')

        fr3=Frame(note2,width=650,height=600)
        fra4=Frame(note2,width=650,height=600)
        fra5=Frame(note2,width=650,height=600)
        fra6=Frame(note2,width=650,height=600)
        fra7=Frame(note2,width=650,height=600)
        fra8=Frame(note2,width=650,height=600)
        fra9=Frame(note2,width=650,height=600)
        fra10=Frame(note2,width=650,height=600)

        note2.add(fr3,text='Opearation')
        note2.add(fra4,text='New_account')
        note2.add(fra10,text='Updat Details')
        note2.add(fra5,text='Deposit')
        note2.add(fra6,text='Withdrawal')
        note2.add(fra7,text='Balance')
        note2.add(fra8,text='Users_Details')
        note2.add(fra9,text='Close_Account')
        
        lab2=Label(fr3,text='For New Account',font=('times',20,'bold'))
        lab8=Label(fr3,text='For update ',font=('times',20,'bold'))
        lab3=Label(fr3,text='For Amount Deposite',font=('times',20,'bold'))
        lab4=Label(fr3,text='For amount withdrawal',font=('times',20,'bold'))
        lab5=Label(fr3,text='For Balance Check',font=('times',20,'bold'))
        lab6=Label(fr3,text='For User Details',font=('times',20,'bold'))
        lab7=Label(fr3,text='For Remove Account',font=('times',20,'bold'))

        lab2.place(x=45,y=40)
        lab8.place(x=45,y=100)
        lab3.place(x=45,y=160)
        lab4.place(x=45,y=220)
        lab5.place(x=45,y=280)
        lab6.place(x=45,y=340)
        lab7.place(x=45,y=400)

        def new_acc():
           note2.select(1)
        def new():
            mycursor=mydb.cursor()
            name=en1.get()
            acc_no=en2.get()
            dob=en3.get()
            address=en4.get()
            phno=en5.get()
            amount=en6.get()
            print(acc_no)
            if len(acc_no)==10:
               check='select acc_no from new1 where acc_no = %s'
               mycur=mydb.cursor()
               mycur.execute(check,(acc_no,))
               f1=mycur.fetchall()
               print(f1)
               if not f1:
                  if len(phno)==10:
                     if name!=" "and acc_no!=" " and dob !=" " and address !=" " and phno!=" " and amount !=" ":
                        sql='insert into new1 values(%s,%s,%s,%s,%s,%s)'
                        data=(name,acc_no,dob,address,phno,amount)
                        mycursor.execute(sql,data)
                        mydb.commit()
                        sql2="insert into trans1 values(%s,%s,'opening',%s)"
                        data2=(name,acc_no,amount)
                        mycursor.execute(sql2,data2)
                        mydb.commit()
                        messagebox.showinfo("message",'Account created successfully !')
                        en1.delete(0,END)
                        en2.delete(0,END)
                        en3.delete(0,END)
                        en4.delete(0,END)
                        en5.delete(0,END)
                        en6.delete(0,END)
                     else:
                      messagebox.showerror('error','Fill all the fields')
                  else:
                   messagebox.showerror("Error","Phone Number must be 10 digit")
               else:
                  messagebox.showerror("Error","Account Number already exist")
            else:
               
               messagebox.showerror("Error","Account Number must be 10 digit")
               
        def update():
           note2.select(2)

        def update11():
           acc_no=eny1.get()
           name=eny2.get()
           address=eny3.get()
           phno=eny4.get()
           if len(acc_no)==10:
               check='select acc_no from new1 where acc_no = %s'
               mycur=mydb.cursor()
               mycur.execute(check,(acc_no,))
               f1=mycur.fetchall()
               check2='select name from new1 where name = %s'
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               if f1 and f2: 
                  if acc_no !=" " and name !=" " and address !=" " and phno !=" ":
                    data=(name,address,phno,acc_no) 
                    sql=" update new1 set name=%s,address=%s,phno=%s where acc_no=%s"
                     
                    my=mydb.cursor()
                    my.execute(sql,data)
                    mydb.commit()
                    messagebox.showinfo("message","updated successfully")
                    eny1.delete(0,END)
                    eny2.delete(0,END)
                    eny3.delete(0,END)
                    eny4.delete(0,END)
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't Find The Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")
         
        def deposit():
           note2.select(3)
        def depo():
           acc_no=et1.get()
           name=et2.get()
           amount=et3.get()
           if len(acc_no)==10:
               check='select acc_no from new1 where acc_no = %s'
               mycur=mydb.cursor()
               mycur.execute(check,(acc_no,))
               f1=mycur.fetchall()
               check2='select name from new1 where name = %s'
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               print("deposit amount =",f2)
               if f1 and f2: 
                  if acc_no !="" and name !="" and amount !="":
                     sql="select amount from trans1 where acc_no=%s"
                     mycur.execute(sql,(acc_no,))
                     old=mycur.fetchall()
                     new_amount=int(amount)+int(str(old[-1][0]))
                     sql2="insert into trans1 values(%s,%s,'+Deposit',%s)"
                     data2=(name,acc_no,new_amount)
                     mycur.execute(sql2,data2)
                     mydb.commit()
                     messagebox.showinfo("message","Amount deposited")
                     et1.delete(0,END)
                     et2.delete(0,END)
                     et3.delete(0,END)
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't Find The Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")
           
        def withdrawal():
           note2.select(4)
        def wit():
           acc_no=ety1.get()
           name=ety2.get()
           amount=ety3.get()
           if len(acc_no)==10:
               check='select acc_no from new1 where acc_no = %s'
               check2='select name from new1 where name = %s'
               mycur=mydb.cursor()
               mycur.execute(check,(acc_no,))
               f1=mycur.fetchall()
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               if f1 and f2: 
                  if acc_no !="" and name !="" and amount !="":
                     sql="select amount from trans1 where acc_no=%s"
                     mycur.execute(sql,(acc_no,))
                     old=mycur.fetchall()
                     new_amount=int(str(old[-1][0]))-int(amount)
                     sql2="insert into trans1 values(%s,%s,'-withdraw',%s)"
                     data2=(name,acc_no,new_amount)
                     mycur.execute(sql2,data2)
                     mydb.commit()
                     messagebox.showinfo("message","Amount widrawal successful")
                     ety1.delete(0,END)
                     ety2.delete(0,END)
                     ety3.delete(0,END)
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't Find The Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")
           
        def cle():
         ery1.delete(0, END)
         ery2.delete(0, END)
         balan.destroy()
         balan=Label(fra7,text="",font=("times",30,"bold"))
         balan.place(x=100,y=300)

        def balance():
           note2.select(5)
        def check():
           name=ery1.get()
           ac=ery2.get()
           if len(ac)==10:
               check='select acc_no from new1 where acc_no = %s'
               check2='select name from new1 where name =%s'
               mycur=mydb.cursor()
               mycur.execute(check,(ac,))
               f1=mycur.fetchall()
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               if f1 and f2: 
                  if ac !="" and name !="":
                     sql="select amount from trans1 where acc_no=%s"
                     mycur.execute(sql,(ac,))
                     old=mycur.fetchall()
                     balance=str(old[-1][0])
                     messagebox.showinfo("Balance",f"Balance Amount : {balance}")
                     ery1.delete(0, END)
                     ery2.delete(0, END)
                     
                     # bal=Label(fra7,text="",font=("times",30,"bold"))
                     # bal.place(x=100,y=300)
                     # balan.config(text='Balance Amount : '+balance)
                     # cle()
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't find the Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")

        # Details
        def details():
           note2.select(6)

        def users():
           name=eoy1.get()
           ac=eoy2.get()
           if len(ac)==10:
               check='select acc_no from new1 where acc_no = %s'
               check2='select name from new1 where name =%s'
               mycur=mydb.cursor()
               mycur.execute(check,(ac,))
               f11=mycur.fetchall()
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               if f11 and f2:
                  if ac !="" and name !="":
                     user=Toplevel(bank)
                     user.geometry('600x500')
                     sql='select * from new1 where acc_no=%s'
                     my=mydb.cursor()
                     my.execute(sql,(ac,))
                     f1=my.fetchall()
                     sql2='select amount from trans1 where acc_no=%s'
                     my.execute(sql2,(ac,))
                     f2=my.fetchall()
                     balance=str(f2[-1][0])
                     
                     lab1=Label(user,text='User_Details',font=("arial",20,"bold"))
                     lab2=Label(user,text='Name',font=("arial",20,"bold"))
                     lab3=Label(user,text='Account No',font=("arial",20,"bold"))
                     lab4=Label(user,text='Date Of Birth',font=("arial",20,"bold"))
                     lab5=Label(user,text='Address',font=("arial",20,"bold"))
                     lab6=Label(user,text='Phone No',font=("arial",20,"bold"))
                     lab7=Label(user,text='Current Balance',font=("arial",20,"bold"))

                     lab1.pack(fill="x")
                     lab2.place(x=25,y=60)
                     lab3.place(x=25,y=120)
                     lab4.place(x=25,y=180)
                     lab5.place(x=25,y=240)
                     lab6.place(x=25,y=300)
                     lab7.place(x=25,y=360)
                     
                     res1=Label(user,text='',font=('times',20,'bold'))
                     res2=Label(user,text='',font=('times',20,'bold'))
                     res3=Label(user,text='',font=('times',20,'bold'))
                     res4=Label(user,text='',font=('times',20,'bold'))
                     res5=Label(user,text='',font=('times',20,'bold'))
                     res6=Label(user,text='',font=('times',20,'bold'))
                     but=Button(user,text='Close',font=('times',20,'bold'),width=20,bg='red',fg='white',command=user.destroy)

                     res1.place(x=300,y=60)
                     res2.place(x=300,y=120)
                     res3.place(x=300,y=180)
                     res4.place(x=300,y=240)
                     res5.place(x=300,y=300)
                     res6.place(x=300,y=360)
                     but.pack(side='bottom',pady=20)

                     res1.config(text=f1[0][0])
                     res2.config(text=str(f1[0][1]))
                     res3.config(text=str(f1[0][2]))
                     res4.config(text=f1[0][3])
                     res5.config(text=str(f1[0][4]))
                     res6.config(text=balance)

                     eoy1.delete(0,END)
                     eoy2.delete(0,END)
                     user.mainloop()
                     # messagebox.showinfo("message","done")
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't Find The Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")
           
        # close
        def close():
           note2.select(7)

        def clo():
           name=eyy1.get()
           ac=eyy2.get()
           if len(ac)==10:
               check='select acc_no from new1 where acc_no = %s'
               check2='select name from new1 where name =%s'
               mycur=mydb.cursor()
               mycur.execute(check,(ac,))
               f1=mycur.fetchall()
               mycur.execute(check2,(name,))
               f2=mycur.fetchall()
               if f1 and f2: 
                  if ac !="" and name !="":
                     sql="delete from new1 where acc_no=%s"
                     sql2="delete from trans1 where acc_no=%s"
                     mycur.execute(sql2,(ac,))
                     mydb.commit()
                     mycur.execute(sql,(ac,))
                     mydb.commit()
                     messagebox.showinfo("message","Deleted successfully!")
                     eyy1.delete(0,END)
                     eyy2.delete(0,END)
                  else:
                    messagebox.showerror("Error","fill all fields")
               else:
                  messagebox.showerror("Error","Couldn't Find The Account")
           else:
             messagebox.showerror("Error","Account no must be 10 digit")
        
        def back():
           note2.select(0)
           eyy1.delete(0,END)
           eyy2.delete(0,END)
           eoy1.delete(0,END)
           eoy2.delete(0,END)
           ery1.delete(0,END)
           ery2.delete(0,END)
           ety1.delete(0,END)
           ety2.delete(0,END)
           ety3.delete(0,END)
           et1.delete(0,END)
           et2.delete(0,END)
           et3.delete(0,END)
           eny1.delete(0,END)
           eny2.delete(0,END)
           eny3.delete(0,END)
           en1.delete(0,END)
           en2.delete(0,END)
           en3.delete(0,END)
           en4.delete(0,END)
           en5.delete(0,END)
           en6.delete(0,END)

        # frame ===3  first page
        but2=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=new_acc)
        but9=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=update)
        but3=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=deposit)
        but4=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=withdrawal)
        but5=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=balance)
        but6=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=details)
        but7=Button(fr3,text='Click',width=10,bg='green',fg='white',font=('times',20,'bold'),command=close)
        but8=Button(fr3,text="Close",width=10,bg='red',fg='white',font=('times',20,'bold'),command=bank.destroy)

        but2.place(x=420,y=30)
        but9.place(x=420,y=90)
        but3.place(x=420,y=150)
        but4.place(x=420,y=210)
        but5.place(x=420,y=270)
        but6.place(x=420,y=330)
        but7.place(x=420,y=390)
        but8.place(x=200,y=500)

        #frame==4  New Account 
        new1=Label(fra4,text='Name',font=("times",20,'bold'))
        new2=Label(fra4,text='Account No',font=("times",20,'bold'))
        new3=Label(fra4,text='Date Of Birth',font=("times",20,'bold'))
        new4=Label(fra4,text='Address',font=("times",20,'bold'))
        new5=Label(fra4,text='Phone No',font=("times",20,'bold'))
        new6=Label(fra4,text='Open Amount',font=("times",20,'bold'))

        new1.place(x=50,y=60)
        new2.place(x=50,y=130)
        new3.place(x=50,y=200)
        new4.place(x=50,y=270)
        new5.place(x=50,y=330)
        new6.place(x=50,y=390)

        en1=Entry(fra4,width=20,font=('times',20,'bold'))
        en2=Entry(fra4,width=20,font=('times',20,'bold'))
        en3=Entry(fra4,width=20,font=('times',20,'bold'))
        en4=Entry(fra4,width=20,font=('times',20,'bold'))
        en5=Entry(fra4,width=20,font=('times',20,'bold'))
        en6=Entry(fra4,width=20,font=('times',20,'bold'))

        en1.place(x=300,y=60)
        en2.place(x=300,y=130)
        en3.place(x=300,y=200)
        en4.place(x=300,y=270)
        en5.place(x=300,y=330)
        en6.place(x=300,y=390)

        butt1=Button(fra4,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        butt2=Button(fra4,text="Submit",width=10,bg='green',fg='white',font=('times',20,'bold'),command=new)
        
        butt1.place(x=110,y=500)
        butt2.place(x=350,y=500)

        # update frame
        new1=Label(fra10,text='Account No',font=("times",20,'bold'))
        new2=Label(fra10,text='New Name',font=("times",20,'bold'))
        new3=Label(fra10,text='New Address',font=("times",20,'bold'))
        new4=Label(fra10,text='New Phone No',font=("times",20,'bold'))

        new1.place(x=50,y=60)
        new2.place(x=50,y=130)
        new3.place(x=50,y=200)
        new4.place(x=50,y=270)

        eny1=Entry(fra10,width=20,font=('times',20,'bold'))
        eny2=Entry(fra10,width=20,font=('times',20,'bold'))
        eny3=Entry(fra10,width=20,font=('times',20,'bold'))
        eny4=Entry(fra10,width=20,font=('times',20,'bold'))

        eny1.place(x=300,y=60)
        eny2.place(x=300,y=130)
        eny3.place(x=300,y=200)
        eny4.place(x=300,y=270)

        butt1=Button(fra10,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        butt2=Button(fra10,text="Update",width=10,bg='green',fg='white',font=('times',20,'bold'),command=update11)
        
        butt1.place(x=110,y=350)
        butt2.place(x=350,y=350)

        #framm=5 dposit
        dep1=Label(fra5,text='Account No',font=("times",20,'bold'))
        dep2=Label(fra5,text='Name',font=("times",20,'bold'))
        dep3=Label(fra5,text='Amount(Deposit)',font=("times",20,'bold'))
        et1=Entry(fra5,width=20,font=('times',20,'bold'))
        et2=Entry(fra5,width=20,font=('times',20,'bold'))
        et3=Entry(fra5,width=20,font=('times',20,'bold'))
        bu1=Button(fra5,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        bu2=Button(fra5,text="Deposit",width=10,bg='blue',fg='white',font=('times',20,'bold'),command=depo)
        
        bu1.place(x=110,y=275)
        bu2.place(x=350,y=275)
        dep1.place(x=75,y=60)
        dep2.place(x=75,y=120)
        dep3.place(x=75,y=180)
        et1.place(x=300,y=60)
        et2.place(x=300,y=120)
        et3.place(x=300,y=180)


        # frame==6 withdrawal
        with1=Label(fra6,text='Account No',font=("times",20,'bold'))
        with2=Label(fra6,text='Name',font=("times",20,'bold'))
        with3=Label(fra6,text='Amount(Withdrawal)',font=("times",20,'bold'))
        ety1=Entry(fra6,width=20,font=('times',20,'bold'))
        ety2=Entry(fra6,width=20,font=('times',20,'bold'))
        ety3=Entry(fra6,width=20,font=('times',20,'bold'))
        buo1=Button(fra6,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        buo2=Button(fra6,text="Withdraw",width=10,bg='green',fg='white',font=('times',20,'bold'),command=wit)
        
        buo1.place(x=110,y=275)
        buo2.place(x=350,y=275)
        with1.place(x=50,y=60)
        with2.place(x=50,y=120)
        with3.place(x=50,y=180)
        ety1.place(x=310,y=60)
        ety2.place(x=310,y=120)
        ety3.place(x=310,y=180)

        # frmae==7  balance
        bal1=Label(fra7,text='User Name',font=("times",20,'bold'))
        bal2=Label(fra7,text='Account No',font=("times",20,'bold'))
        ery1=Entry(fra7,width=20,font=('times',20,'bold'))
        ery2=Entry(fra7,width=20,font=('times',20,'bold'))
        buot1=Button(fra7,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        buot2=Button(fra7,text="Check",width=10,bg='blue',fg='white',font=('times',20,'bold'),command=check)
        buot3=Button(fra7,text="Clear",width=10,bg='red',fg='white',font=('times',20,'bold'),command=cle)
        
        buot1.place(x=60,y=200)
        buot2.place(x=250,y=200)
        buot3.place(x=440,y=200)
        bal1.place(x=75,y=60)
        bal2.place(x=75,y=120)
        ery1.place(x=310,y=60)
        ery2.place(x=310,y=120)

        # frame==8 users Details
        bal1=Label(fra8,text='User Name',font=("times",20,'bold'))
        bal2=Label(fra8,text='Account No',font=("times",20,'bold'))
        eoy1=Entry(fra8,width=20,font=('times',20,'bold'))
        eoy2=Entry(fra8,width=20,font=('times',20,'bold'))
        buot1=Button(fra8,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        buot2=Button(fra8,text="Submit",width=10,bg='green',fg='white',font=('times',20,'bold'),command=users)
        
        buot1.place(x=110,y=200)
        buot2.place(x=350,y=200)
        bal1.place(x=75,y=60)
        bal2.place(x=75,y=120)
        eoy1.place(x=310,y=60)
        eoy2.place(x=310,y=120)

        # frmae=9 close the account
        bal1=Label(fra9,text='User Name',font=("times",20,'bold'))
        bal2=Label(fra9,text='Account No',font=("times",20,'bold'))
        eyy1=Entry(fra9,width=20,font=('times',20,'bold'))
        eyy2=Entry(fra9,width=20,font=('times',20,'bold'))
        buot1=Button(fra9,text="Cancel",width=10,bg='red',fg='white',font=('times',20,'bold'),command=back)
        buot2=Button(fra9,text="Submit",width=10,bg='blue',fg='white',font=('times',20,'bold'),command=clo)
        
        buot1.place(x=110,y=200)
        buot2.place(x=350,y=200)
        bal1.place(x=75,y=60)
        bal2.place(x=75,y=120)
        eyy1.place(x=310,y=60)
        eyy2.place(x=310,y=120)
        note2.select(0)

        bank.mainloop()
       else:
          messagebox.showerror("login",'LoginFaild')
          ent1.delete(0,END)
          ent2.delete(0,END)
          print(userid)  
    
    except:
        messagebox.showerror("login",'Soming went Wrong !')
        ent1.delete(0,END)
        ent2.delete(0,END)
        print(userid)  



frame=Frame(tk,bg='black',padx=25,pady=25,highlightbackground='yellow',highlightthickness=3)
log=Label(frame,text='Login',font=('arial',50,'bold'),bg='black',fg='white')

lab1=Label(frame,text="UserID",font=('sans serif',20,"bold"),fg='white',bg='black')
lab2=Label(frame,text="Password",font=('sans serif',20,"bold"),fg='white',bg='black')
ent1=Entry(frame,fg='black',width=30,font=('times',15,'bold'))
ent2=Entry(frame,fg='black',width=30,font=('times',15,'bold'))
ent2.config(show="*")
but1=Button(frame,text="Login",font=('sans serif',15,"bold"),bg="white",fg='black',command=login)
but2=Button(frame,text="Cancel",font=('sans serif',15,"bold"),bg="white",fg='black',command=tk.destroy)


log.grid(row=0,column=0,columnspan=2,sticky='news',pady=20)
lab1.grid(row=1,column=0,sticky='news',padx=10)
ent1.grid(row=1,column=1)
lab2.grid(row=2,column=0,sticky='news',pady=30)
ent2.grid(row=2,column=1)
but1.grid(row=3,column=0,sticky=E)  
but2.grid(row=3,column=1,sticky=W,padx=40)
 
frame.grid(row=3,column=2,sticky='news',pady=100)
tk.config(bg='#a5e7ff')

tk.mainloop()










