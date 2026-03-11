from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom
from Hall import Hall_Booking
from tkinter import messagebox








class Hotel_Management_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")


#============ist image==================
        img1=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\hotel1.png.jpg")
        img1=img1.resize((1500,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #=================2nd image=============

        img2=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\logo.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #================title=========================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


        #================main frame===================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #=================menu========================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #===========btn frame=========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        #details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        #details_btn.grid(row=2,column=0,pady=1)

        hall_btn=Button(btn_frame,text="HALL",command=self.hallbooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        hall_btn.grid(row=2,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #================right side========================

        img3=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\wait.png")
        img3=img3.resize((1310,800),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=185,width=1310,height=800)

        #==============down side==================

        img4=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\food.jpg")
        img4=img4.resize((223,210),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=4,y=418,width=225,height=210)

        img5=Image.open(r"C:\Users\sachi\OneDrive\Pictures\Saved Pictures\photo.jpg")
        img5=img5.resize((223,210),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(self.root,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=4,y=600,width=225,height=210)


    def cust_details(self):
        self.new_window =Toplevel(self.root)
        self.app=Cust_win(self.new_window)
        
    def roombooking(self):
        self.new_window =Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def hallbooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Hall_Booking(self.new_window)
        
    def details_room(self):
        self.new_window =Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    #def logout(self):
     #   self.root.destroy()

    def logout(self):
        #"""Handles the logout functionality."""
        response = messagebox.askyesno("Logout", "Do you want to log out?",parent=self.root)
        if response:
             # Perform logout actions here (e.g., clear session, close windows)
            #print("Logging out...") # Example action
            # ... your logout code ...
            self.root.destroy() #close the window
        else:
            #print("Logout cancelled.")
            return

        









if __name__== "__main__":
    root=Tk()
    obj=Hotel_Management_System(root)
    root.mainloop()



