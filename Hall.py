from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Hall_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1275x590+225+215")

    #================title=========================
        lbl_title=Label(self.root,text="HALL DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=2,width=1295,height=50)

    #=================logo image=============

        img2=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #==============down side==================

        imgA=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\decoration.jpeg")
        imgA=imgA.resize((480,400),Image.Resampling.LANCZOS)
        self.photoimgA=ImageTk.PhotoImage(imgA)

        lblimg=Label(self.root,image=self.photoimgA,bd=0,relief=RIDGE)
        lblimg.place(x=2,y=400,width=480,height=400)

        imgB=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\weeding.webp")
        imgB=imgB.resize((400,400),Image.Resampling.LANCZOS)
        self.photoimgB=ImageTk.PhotoImage(imgB)

        lblimg=Label(self.root,image=self.photoimgB,bd=0,relief=RIDGE)
        lblimg.place(x=483,y=400,width=400,height=400)

        imgC=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\birthday.jpeg")
        imgC=imgC.resize((380,400),Image.Resampling.LANCZOS)
        self.photoimgC=ImageTk.PhotoImage(imgC)

        lblimg=Label(self.root,image=self.photoimgC,bd=0,relief=RIDGE)
        lblimg.place(x=883,y=400,width=380,height=400)

         #==============LABEL FRAME=====================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Hall Details",font=("times new roman",12,"bold"),padx=2) 
        LabelFrameleft.place(x=5,y=50,width=540,height=350)

        #Hall
        lbl_Hall=Label(LabelFrameleft,text="Hall",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Hall.grid(row=0,column=0,sticky=W,padx=20)
        
        self.var_Hall=StringVar()
        entry_Hall=ttk.Entry(LabelFrameleft,textvariable=self.var_Hall,width=20,font=("arial",13,"bold"))
        entry_Hall.grid(row=0,column=1,sticky=W)
        #combo_Hall=ttk.Combobox(LabelFrameleft,textvariable=self.var_Hall,font=("arial",12,"bold"),width=18,state="readonly")
        #combo_Hall["value"]=("1","2","3","4","5","6")
        #combo_Hall.current(0)
        #combo_Hall.grid(row=0,column=1)

        #Capacity
        lbl_Capacity=Label(LabelFrameleft,text="Capacity",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Capacity.grid(row=1,column=0,sticky=W,padx=20)
        
        self.var_Capacity=StringVar()
        entry_Capacity=ttk.Entry(LabelFrameleft,textvariable=self.var_Capacity,width=20,font=("arial",13,"bold"))
        entry_Capacity.grid(row=1,column=1,sticky=W)

        #function
        lbl_Function=Label(LabelFrameleft,text="Function",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Function.grid(row=2,column=0,sticky=W,padx=20)
        
        self.var_Function=StringVar()
        combo_Function=ttk.Combobox(LabelFrameleft,textvariable=self.var_Function,font=("arial",12,"bold"),width=18,state="readonly")
        combo_Function["value"]=("Marriage","Birthday","Kitty Party")
        combo_Function.current(0)
        combo_Function.grid(row=2,column=1)

        #schedule
        Label_Schedule=Label(LabelFrameleft,font=("arial",12,"bold"),text="Schedule :",padx=2,pady=6)
        Label_Schedule.grid(row=3,column=0,sticky=W)
        
        self.var_Schedule=StringVar()
        combo_Schedule=ttk.Combobox(LabelFrameleft,textvariable=self.var_Schedule,font=("arial",12,"bold"),width=18,state="readonly")
        combo_Schedule["value"]=("Day","Night")
        combo_Schedule.current(0)
        combo_Schedule.grid(row=3,column=1)

        #Paid Tax
        lblPaidtax=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblPaidtax.grid(row=4,column=0,sticky=W)
        self.var_Paidtax=StringVar()
        txtPaidtax=ttk.Entry(LabelFrameleft,textvariable=self.var_Paidtax,font=("arial",13,"bold"),width=20)
        txtPaidtax.grid(row=4,column=1)

        #Sub Total
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=5,column=0,sticky=W)
        self.var_actualtotal=StringVar()
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=20)
        txtNoOfDays.grid(row=5,column=1)

        #Total Cost
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        self.var_total=StringVar()
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_total,font=("arial",13,"bold"),width=20)
        txtNoOfDays.grid(row=6,column=1)

        #==========Bill Btn=============
        btnBill=Button(LabelFrameleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=7,column=0,padx=1,sticky=W)

        #=============pay bill========
        #==========Bill Btn=============
        btnBill=Button(LabelFrameleft,text="Pay Bill",command=self.pay_bill,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=7,column=1,padx=1,sticky=W)

        #================btns======================
        btn_frame=Frame(LabelFrameleft,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=280,width=412,height=48)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

         #==========Table frame search system============

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Hall Details",font=("arial",11,"bold"),padx=2)
        Table_frame.place(x=580,y=55,width=690,height=348)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.hall_Table=ttk.Treeview(Table_frame,column=("Hall","Capacity","Function","Schedule"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hall_Table.xview)
        scroll_y.config(command=self.hall_Table.yview)

        self.hall_Table.heading("Hall",text="Hall")
        self.hall_Table.heading("Capacity",text="Capacity ")
        self.hall_Table.heading("Function",text="Function")
        self.hall_Table.heading("Schedule",text="Schedule")
        
        self.hall_Table["show"]="headings"

        self.hall_Table.column("Hall",width=100)
        self.hall_Table.column("Capacity",width=100)
        self.hall_Table.column("Function",width=100)
        self.hall_Table.column("Schedule",width=100)
        
        self.hall_Table.pack(fill=BOTH,expand=1)
        self.hall_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #===============add data=============
    def add_data(self):
        if self.var_Schedule.get()=="" or self.var_Function.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hall values(%s,%s,%s,%s)",(
                                                                                    self.var_Hall.get(),
                                                                                    self.var_Capacity.get(),
                                                                                    self.var_Function.get(),
                                                                                    self.var_Schedule.get()
                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Hall Booked Successfully.",parent=self.root)
            except Exception as es:
                print(f"Error: {es}")  # Print error in the console for debugging
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

     #=================fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hall")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hall_Table.delete(*self.hall_Table.get_children())
            for i in rows:
                self.hall_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=====get cursor=======

    def get_cursor(self,event=""):
        cursor_row=self.hall_Table.focus()
        content=self.hall_Table.item(cursor_row)
        row=content["values"]

        self.var_Hall.set(row[0]),
        self.var_Capacity.set(row[1]),
        self.var_Function.set(row[2]),
        self.var_Schedule.set(row[3])

    #==========update data===========
    def update(self):
        if self.var_Hall.get()=="":
            messagebox.showerror("Error","Please enter Hall number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            my_cursor.execute("update hall set Capacity=%s,`Function`=%s,Schedule=%s where hall=%s",(
                                                                                                      self.var_Capacity.get(),
                                                                                                      self.var_Function.get(),
                                                                                                      self.var_Schedule.get(),
                                                                                                      self.var_Hall.get()
                                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Hall details has been updated successfully.",parent=self.root)


    #================delete data==========
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this Hall Details.",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            query="delete from hall where hall=%s"
            value=(self.var_Hall.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

     #=========reset=================
    def reset(self):
        self.var_Hall.set("")
        self.var_Capacity.set("")
        self.var_Function.set("")
        self.var_Schedule.set("")
        self.var_Paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    #==========total===========
    def total(self):
        function=self.var_Function.get()
        Schedule=self.var_Schedule.get()
        self.var_Paidtax.set(50000)    

        if(self.var_Schedule.get()=="Day" and self.var_Function.get()=="Marriage"):
            q1=float(100000)
            q2=float(200000)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_Schedule.get()=="Night" and self.var_Function.get()=="Marriage"):
            q1=float(400000)
            q2=float(80000)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_Schedule.get()=="Day" and self.var_Function.get()=="Birthday"):
            q1=float(30000)
            q2=float(8000)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_Schedule.get()=="Night" and self.var_Function.get()=="Birthday"):
            q1=float(40000)
            q2=float(5000)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_Schedule.get()=="Day" and self.var_Function.get()=="Kitty Party"):
            q1=float(20000)
            q2=float(800)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_Schedule.get()=="Night" and self.var_Function.get()=="Kitty Party"):
            q1=float(22000)
            q2=float(700)
            q3=float(self.var_Paidtax.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_Paidtax.set(Tax)
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
    obj=Hall_Booking(root)
    root.mainloop()
