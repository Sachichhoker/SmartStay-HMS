from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1275x590+225+215")

        #=================variables========================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomno=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #================title=========================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=2,width=1295,height=50)

    #=================logo image=============

        img2=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #==============LABEL FRAME=====================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times new roman",12,"bold"),padx=2) 
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #===============labels and entry================
        #cust contact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #==========fetch data button==============
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=340,y=4)


        #check_in Date
        check_in_date=Label(LabelFrameleft,font=("arial",13,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check_out Date
        lblcheck_out_date=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check_out Date:",padx=2,pady=6)
        lblcheck_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtcheck_out_date.grid(row=2,column=1)

        #Room Type
        Label_RoomType=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        Label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomNo=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room No :",padx=2,pady=6)
        lblRoomNo.grid(row=4,column=0,sticky=W)
        #txtRoomNo=ttk.Entry(LabelFrameleft,textvariable=self.var_roomno,font=("arial",13,"bold"),width=29)
        #txtRoomNo.grid(row=4,column=1)

        conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomno,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        #Meal
        lblMeal=Label(LabelFrameleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        #No. of Days
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        #Sub Total
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        #Total Cost
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblNoOfDays.grid(row=9,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=9,column=1)

        #==========Bill Btn=============
        btnBill=Button(LabelFrameleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #==========pay bill===========
     
        btnBill=Button(LabelFrameleft,text="Pay Bill",command=self.pay_bill,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=1,padx=1,sticky=W)

        #================btns======================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=48)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #===============Right side Image================

        img3=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\bed.jpg")
        img3=img3.resize((550,300),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=550,height=300)


        #==========Table frame search system============

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Views Details And Search System",font=("arial",11,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)


        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #==============show data table===========

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","room no","meal",
                                                                   "noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="Contact")
        self.room_Table.heading("checkin",text="check-in ")
        self.room_Table.heading("checkout",text="check-out")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("room no",text="room no.")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfdays",text="NoOfDays")
        
        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin",width=100)
        self.room_Table.column("checkout",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("room no",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfdays",width=100)
        

        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    #===============add data=============
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                print(f"Error: {es}")  # Print error in the console for debugging
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    #=================fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=====get cursor=======

    def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomno.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #==========update data===========
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                                                      
                                                                                                                                         self.var_checkin.get(),
                                                                                                                                         self.var_checkout.get(),
                                                                                                                                         self.var_roomtype.get(),
                                                                                                                                         self.var_roomno.get(),
                                                                                                                                         self.var_meal.get(),
                                                                                                                                         self.var_noofdays.get(),
                                                                                                                                         self.var_contact.get()
                                                                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully.",parent=self.root)

    #================delete data==========
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #=========reset=================
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomno.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")




    #==============all data fetch===========
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s") 
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
            #===============Gender=======================
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s") 
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

            #===============email=====================
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s") 
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                #===============nationality=====================
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s") 
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

#===============address=====================
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s") 
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)

    #============search system==========
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==========total===========
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%y") 
        outDate=datetime.strptime(outDate,"%d/%m/%y")
        self.var_noofdays.set(abs(outDate-inDate).days)    

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxary"):
            q1=float(400)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxary"):
            q1=float(500)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(150)
            q2=float(670)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(170)
            q2=float(680)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(150)
            q2=float(580)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(680)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(350)
            q2=float(780)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(780)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
    
    def pay_bill(self):
        total_str = self.var_total.get().replace("Rs.", "").strip()
        try:
            amount_due = float(total_str)
        except ValueError:
            messagebox.showerror("Error", "Please calculate the bill first.", parent=self.root)
            return

        pay_win = Toplevel(self.root)
        pay_win.title("Payment")
        pay_win.geometry("420x500")
        pay_win.config(bg="white")

        Label(pay_win, text=f"Total Amount Due: ₹{amount_due:.2f}", font=("Arial", 13, "bold"), bg="white", fg="black").pack(pady=10)

        method_var = StringVar(value="Cash")
        OptionMenu(pay_win, method_var, "Cash", "Net Banking", "Card", "QR Code", command=lambda _: show_fields()).pack(pady=5)

        field_frame = Frame(pay_win, bg="white")
        field_frame.pack(pady=10)

        input_widgets = []

        qr_label = Label(field_frame, bg="white")

        def clear_fields():
            for widget in input_widgets:
                widget.destroy()
            input_widgets.clear()
            qr_label.pack_forget()

        def add_field(label_text, show=""):
            Label(field_frame, text=label_text, font=("Arial", 10), bg="white").pack(anchor="w", padx=10)
            entry = Entry(field_frame, font=("Arial", 11), show=show)
            entry.pack(fill="x", padx=10, pady=2)
            input_widgets.append(entry)
            return entry

        def show_fields():
            clear_fields()
            method = method_var.get()

            if method == "Cash":
                add_field("Enter Cash Amount:")

            elif method == "Net Banking":
                add_field("Bank Name:")
                add_field("Account Number:")
                add_field("IFSC Code:")
                add_field("Mobile Number:")

            elif method == "Card":
                add_field("Card Number:")
                add_field("Card Holder Name:")
                add_field("Expiry Date (MM/YY):")
                add_field("CVV:", show="*")

            elif method == "QR Code":
                try:
                    from PIL import Image, ImageTk
                    import qrcode
                    qr = qrcode.make(f"upi://pay?amount={amount_due}")
                    qr = qr.resize((200, 200))
                    qr_img = ImageTk.PhotoImage(qr)
                    qr_label.config(image=qr_img)
                    qr_label.image = qr_img
                    qr_label.pack(pady=10)
                    Label(field_frame, text="Scan the QR code with your UPI app.", font=("Arial", 10), bg="white").pack()
                except Exception as e:
                    Label(field_frame, text="QR Code Error", bg="white", fg="red").pack()

        def process_payment():
            method = method_var.get()
            values = [e.get() for e in input_widgets]

            if method == "Cash":
                try:
                    cash = float(values[0])
                    if cash >= amount_due:
                        change = cash - amount_due
                        messagebox.showinfo("Payment Success", f"💵 Cash received.\nChange: ₹{change:.2f}", parent=pay_win)
                        pay_win.destroy()
                    else:
                        messagebox.showerror("Error", "Insufficient cash.", parent=pay_win)
                except ValueError:
                    messagebox.showerror("Error", "Enter a valid amount.", parent=pay_win)

            elif method == "Net Banking":
                if all(values):
                    messagebox.showinfo("Payment Success", f"🏦 Net banking successful from {values[0]}", parent=pay_win)
                    pay_win.destroy()
                else:
                    messagebox.showerror("Error", "Please fill all net banking details.", parent=pay_win)

            elif method == "Card":
                if all(values):
                    if not values[0].isdigit() or len(values[0]) < 12:
                        messagebox.showerror("Error", "Invalid card number.", parent=pay_win)
                        return
                    if not values[3].isdigit() or len(values[3]) != 3:
                        messagebox.showerror("Error", "Invalid CVV.", parent=pay_win)
                        return
                    messagebox.showinfo("Payment Success", f"💳 Card ending in {values[0][-4:]} charged successfully.", parent=pay_win)
                    pay_win.destroy()
                else:
                    messagebox.showerror("Error", "Please fill all card details.", parent=pay_win)

            elif method == "QR Code":
                messagebox.showinfo("Payment Success", "✅ Payment confirmed via QR scan.", parent=pay_win)
                pay_win.destroy()

        Button(pay_win, text="Confirm Payment", command=process_payment, font=("Arial", 11, "bold"), bg="green", fg="white").pack(pady=15)

        show_fields()



        



if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()

