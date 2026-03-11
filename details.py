from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1275x590+225+215")


        #================title=========================
        lbl_title=Label(self.root,text="ROOM Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=2,width=1295,height=50)

    #=================logo image=============

        img2=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

    #==============down side==================

        img6=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\led.jpg")
        img6=img6.resize((260,400),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lblimg=Label(self.root,image=self.photoimg6,bd=0,relief=RIDGE)
        lblimg.place(x=2,y=400,width=280,height=400)

        img7=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\wardob.jpg")
        img7=img7.resize((260,400),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        lblimg=Label(self.root,image=self.photoimg7,bd=3,relief=RIDGE)
        lblimg.place(x=283,y=400,width=260,height=400)

        img8=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\dinning.jpg")
        img8=img8.resize((640,400),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        lblimg=Label(self.root,image=self.photoimg8,bd=3,relief=RIDGE)
        lblimg.place(x=543,y=400,width=640,height=400)

        #==============LABEL FRAME=====================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2) 
        LabelFrameleft.place(x=5,y=50,width=540,height=350)

        #floor
        lbl_Floor=Label(LabelFrameleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=0,column=0,sticky=W,padx=20)
        
        self.var_Floor=StringVar()
        entry_Floor=ttk.Entry(LabelFrameleft,textvariable=self.var_Floor,width=20,font=("arial",13,"bold"))
        entry_Floor.grid(row=0,column=1,sticky=W)

        #RoomNo
        lbl_RoomNo=Label(LabelFrameleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)
        
        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #RoomType
        lbl_RoomType=Label(LabelFrameleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)
        
        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

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

        btnClean=Button( text="Request Cleaning", command=self.request_cleaning, font=("arial",11,"bold"), bg="black", fg="gold", width=18)
        btnClean.place(x=14,y=310)


        #==========Table frame search system============

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Rooms Details",font=("arial",11,"bold"),padx=2)
        Table_frame.place(x=580,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_Table=ttk.Treeview(Table_frame,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("Floor",text="Floor")
        self.room_Table.heading("RoomNo",text="Room No ")
        self.room_Table.heading("RoomType",text="Room type")
        
        self.room_Table["show"]="headings"

        self.room_Table.column("Floor",width=100)
        self.room_Table.column("RoomNo",width=100)
        self.room_Table.column("RoomType",width=100)
        
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #===============add data=============
    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_Floor.get(),
                                                                                    self.var_RoomNo.get(),
                                                                                    self.var_RoomType.get()
                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully.",parent=self.root)
            except Exception as es:
                print(f"Error: {es}")  # Print error in the console for debugging
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    #=================fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_Floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])


    #==========update data===========
    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","Please enter Floor No.",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where roomno=%s",(
                                                                                                                                                                      
                                                                                        self.var_Floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_RoomNo.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)

    #================delete data==========
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this room details.",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Sachi28@',database='hotelmanagement')
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #=========reset=================
    def reset(self):
        self.var_Floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")

    #======clean=======
    def request_cleaning(self):
        room_no = self.var_RoomNo.get()
        if room_no == "":
            messagebox.showerror("Error", "Please select a room to request cleaning.", parent=self.root)
            return
        messagebox.showinfo("Cleaning Requested", f"🧹 Cleaning request has been sent for Room No: {room_no}.", parent=self.root)
   

     




if __name__ =="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()

