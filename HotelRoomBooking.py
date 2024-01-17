import tkinter as tk
from tkinter import messagebox

# Dictionary to store valid usernames and passwords
valid_credentials = {
    'Kamillah': 'norkamillah',
    'Suffiya': 'anissuffiya',
    'Anis': 'aniscomel',
    'Iman': 'imanamila',

}

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username in valid_credentials and password == valid_credentials[username]:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Close the window after successful login
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
        messagebox.config(bg="mistyrose")
        
root = tk.Tk()
root.title("Login Page")
root.config(bg='pink3')

# Create and place widgets in the window
label_username = tk.Label(root, text="Username:",bg="pink3")
label_password = tk.Label(root, text="Password:",bg="pink3")

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Use show="*" to hide the password characters

button_login = tk.Button(root, text="Login", command=check_credentials)

# Grid layout
label_username.grid(row=0, column=0, sticky=tk.E)
label_password.grid(row=1, column=0, sticky=tk.E)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, column=1, pady=10)

# Run the main loop
root.mainloop()


from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime


class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Room Booking")
        self.root.geometry("1920x1080")
        self.root.config(background="powder blue")


        MainFrame =Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=14, width=1350,height=550, padx=14, relief=RIDGE,bg="pink1")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450,height=550, padx=2, relief=RIDGE,bg="pink2")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820,height=550, padx=2,pady=6, relief=RIDGE,bg="light coral")
        RightFrame.pack(side=RIGHT)
        
        BottomFrame = Frame(MainFrame, bd=10, width=1350,height=150, padx=1, pady=5, relief=RIDGE,bg="light salmon")
        BottomFrame.pack(side=BOTTOM)
        #=====================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Receipt():
            self.txtReceipt.insert(END,
                                   CusRef.get() + "\t" +
                                   fna.get() + "\t" +
                                   sna.get() + "\t"+
                                   Adr.get() + "\t" +
                                   PostCode.get() + "\t" +
                                   Mobile.get() + "\t" +
                                   State.get() + "\t" +
                                   CheckInDate.get() + "\t" +
                                   CheckOutDate.get() + "\t"
                                   )


        def Clear():
            CusRef.set("")
            fna.set("")
            sna.set("")
            Adr.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            State.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")            
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")

        def Delete():
            self.txtReceipt.delete("1.0",END)

        def Update():
            selected=self.txtReceipt.focus()
            self.txtReceipt(selected,text="",values=(CusRef.get(),fna.get(),sna.get(),Adr.get(),PostCode.get(),Mobile.get(),
                                                                Email.get(),State.get(),DOB.get(),IDType.get(),Gender.get(),CheckInDate.get(),
                                                                CheckOutDate.get(),Meal.get(),RoomType.get(),RoomNo.get(),RoomExtNo.get()))
            CusRef.delete(0,END)
            fna.delete(0,END)
            sna.delete(0,END)
            Adr.delete(0,END)
            PostCode.delete(0,END)
            Mobile.delete(0,END)
            Email.delete(0,END)
            State.delete(0,END)
            DOB.delete(0,END)
            IDType.delete(0,END)
            Gender.delete(0,END)
            CheckInDate.delete(0,END)
            CheckOutDate.delete(0,END)
            Meal.delete(0,END)
            RoomType.delete(0,END)
            RoomNo.delete(0,END)
            RoomExtNo.delete(0,END)
        
        def TotalCostandDate():

            InDate = CheckInDate.get()
            OutDate = CheckOutDate.get()
            InDate = datetime.strptime(InDate, "%d/%m/%Y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
            TotalDays.set(abs((OutDate - InDate).days))

            if (Meal.get() == "Breakfast" and RoomType.get()=="Single"):

                q1 =float(50)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and RoomType.get()=="Double"):

                q1 =float(55)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and  RoomType.get() =="Family"):
                
                q1 =float(75)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and RoomType.get()=="Suite"):

                q1 =float(75)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and RoomType.get()=="Deluxe"):

                q1 =float(75)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and RoomType.get()=="Single"):

                q1 =float(60)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and RoomType.get()=="Double"):

                q1 =float(60)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and RoomType.get()=="Family"):

                q1 =float(60)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and RoomType.get()=="Suite"):

                q1 =float(60)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and RoomType.get()=="Deluxe"):

                q1 =float(60)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Afternoon Tea" and RoomType.get()=="Single"):

                q1 =float(25)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Afternoon Tea" and RoomType.get()=="Double"):

                q1 =float(25)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Afternoon Tea" and RoomType.get()=="Family"):

                q1 =float(25)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Afternoon Tea" and RoomType.get()=="Suite"):

                q1 =float(25)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Afternoon Tea" and RoomType.get()=="Deluxe"):

                q1 =float(25)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and RoomType.get()=="Single"):

                q1 =float(65)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and RoomType.get()=="Double"):

                q1 =float(75)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and RoomType.get()=="Family"):

                q1 =float(75)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and RoomType.get()=="Suite"):

                q1 =float(75)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and RoomType.get()=="Deluxe"):

                q1 =float(75)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Supper" and RoomType.get()=="Single"):

                q1 =float(25)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Supper" and RoomType.get()=="Double"):

                q1 =float(25)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Supper" and RoomType.get()=="Family"):

                q1 =float(25)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Supper" and RoomType.get()=="Suite"):

                q1 =float(25)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Supper" and RoomType.get()=="Deluxe"):

                q1 =float(25)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Room Service" and RoomType.get()=="Single"):

                q1 =float(110)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Room Service" and RoomType.get()=="Double"):

                q1 =float(110)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Room Service" and RoomType.get()=="Family"):

                q1 =float(110)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Room Service" and RoomType.get()=="Suite"):

                q1 =float(110)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Room Service" and RoomType.get()=="Deluxe"):

                q1 =float(110)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "All" and RoomType.get()=="Single"):

                q1 =float(250)
                q2 =float(70)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "All" and RoomType.get()=="Double"):

                q1 =float(200)
                q2 =float(199)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "All" and RoomType.get()=="Family"):

                q1 =float(250)
                q2 =float(475)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "All" and RoomType.get()=="Suite"):

                q1 =float(250)
                q2 =float(659)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "All" and RoomType.get()=="Deluxe"):

                q1 =float(250)
                q2 =float(399)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="RM"+ str('%.2f'%((q5)*0.09))
                ST="RM"+ str('%.2f'%((q5)))
                TT =  "RM"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)


        CusRef =StringVar()
        fna =StringVar()
        sna =StringVar()
        Adr=StringVar()
        PostCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        State=StringVar()
        DOB=StringVar()
        IDType=StringVar()
        Gender=StringVar()            
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()
        #=======================================Widget===========================================================
        self.lblCusID =Label(LeftFrame, font=('arial',12,'bold'),text="Customer Ref:",padx=2,bg="pink2")
        self.lblCusID.grid(row=0,column=0, sticky =W)
        self.txtCusID =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CusRef,width =20)
        self.txtCusID.grid(row=0,column=1,pady=3, padx=20)

        self.lblfna =Label(LeftFrame, font=('arial',12,'bold'),text="Firstname:",padx=2,bg="pink2")
        self.lblfna.grid(row=1,column=0, sticky =W)
        self.txtfna =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =fna,width =20)
        self.txtfna.grid(row=1,column=1,pady=3, padx=20)

        self.lblsna =Label(LeftFrame, font=('arial',12,'bold'),text="Surname:",padx=2,bg="pink2")
        self.lblsna.grid(row=2,column=0, sticky =W)
        self.txtsna =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =sna,width =20)
        self.txtsna.grid(row=2,column=1,pady=3, padx=20)

        self.lblAdr =Label(LeftFrame, font=('arial', 12,'bold'), text="Address:",padx=2,pady=2 ,bg="pink2")
        self.lblAdr.grid(row=3, column=0,sticky=W)
        self.txtAdr=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Adr, width=20)
        self.txtAdr.grid(row=3, column=1, pady=3, padx=20)
        
        self.lblDOB =Label(LeftFrame, font=('arial', 12,'bold'), text="Date of Birth:",padx=2,pady=2,bg="pink2")
        self.lblDOB.grid(row=4, column=0,sticky=W)
        self.txtDOB=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = DOB, width=20)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=20)

        self.lblPoC =Label(LeftFrame, font=('arial', 12,'bold'), text="PostCode:",padx=2,pady=2 ,bg="pink2")
        self.lblPoC.grid(row=5, column=0,sticky=W)
        self.txtPoC=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = PostCode, width=20)
        self.txtPoC.grid(row=5, column=1, pady=3, padx=20)

        self.lblMobile =Label(LeftFrame, font=('arial', 12,'bold'), text="Mobile:",padx=2,pady=2,bg="pink2")
        self.lblMobile.grid(row=6, column=0,sticky=W)
        self.txtMobile=Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = Mobile,width=20)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=20)

        self.lblEmail =Label(LeftFrame, font=('arial', 12,'bold'), text="Email:",padx=2,pady=2,bg="pink2")
        self.lblEmail.grid(row=7, column=0,sticky=W)
        self.txtEmail=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Email, width=20)
        self.txtEmail.grid(row=7, column=1, pady=3, padx=20)

        self.lblState =Label(LeftFrame,font=('arial',12,'bold'),text="State:",padx=2,pady=2,bg="pink2")
        self.lblState .grid(row=8, column=0,sticky=W)
        self.cboState =ttk.Combobox(LeftFrame,textvariable= State, state='readonly', font=('arial', 12,'bold'),width=18)                                        
        self.cboState['value']=("","Johor","Melaka","Negeri Sembilan","Kuala Lumpur","Selangor","Perak","Pulau Pinang","Kedah","Perlis","Kelantan","Terengganu","Pahang","Sabah","Sarawak")
        self.cboState.current(0)
        self.cboState.grid(row=8,column=1,pady=3,padx=20)

        self.lblIDType =Label(LeftFrame, font=('arial', 12,'bold'),text="Type of ID:",padx=2,pady=2,bg="pink2")
        self.lblIDType .grid(row=9, column=0,sticky=W)
        self.cboIDType =ttk.Combobox(LeftFrame,textvariable= IDType, state='readonly', font=('arial', 12,'bold'),width=18)
        self.cboIDType['value'] = ('','Citizens','Driving Licence','Army ID','Police ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)

        self.lblGender =Label(LeftFrame, font=('arial', 12,'bold'), text="Gender:",padx=2,pady=2,bg="pink2")
        self.lblGender.grid(row=10, column=0,sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame,textvariable=Gender, state='readonly',
                                        font=('arial', 12,'bold'), width=18)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10, column=1, pady=3, padx=20)

        self.lblCheck_In_Date =Label(LeftFrame,font=('arial', 12,'bold'),text="Check In Date:",padx=2,pady=2,  bg="pink2")                                   
        self.lblCheck_In_Date.grid(row=11, column=0,sticky=W)
        self.txtCheck_In_Date=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = CheckInDate, width=20)
        self.txtCheck_In_Date.grid(row=11, column=1, pady=3, padx=20)

        self.lblCheck_Out_Date=Label(LeftFrame,font=('arial',12,'bold'),text="Check Out Date:",padx=2,pady=2,bg="pink2")                                     
        self.lblCheck_Out_Date.grid(row=12, column=0,sticky=W)
        self.txtCheck_Out_Date=Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = CheckOutDate,width=20)
        self.txtCheck_Out_Date.grid(row=12, column=1, pady=3, padx=20)

        self.lblMeal =Label(LeftFrame, font=('arial', 12,'bold'), text="Meal:",padx=2,pady=2,bg="pink2")
        self.lblMeal.grid(row=13, column=0,sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame,textvariable=Meal, state='readonly',font=('arial', 12,'bold'), width=18)                                        
        self.cboMeal['value']=('','Breakfast','Lunch','Afternoon Tea','Dinner','Supper','Room Service','All')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=20)

        self.lblRoomType=Label(LeftFrame, font=('arial', 12,'bold'), text="Room Type:",padx=2,pady=2,bg="pink2")
        self.lblRoomType.grid(row=14, column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame,textvariable=RoomType, state='readonly',font=('arial', 12,'bold'), width=18)                                        
        self.cboRoomType['value']=('','Single','Double','Family','Suite','Deluxe')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=20)

        self.lblRoomNo =Label(LeftFrame, font=('arial', 12,'bold'), text="Room No:",padx=2,pady=2,bg="pink2")
        self.lblRoomNo.grid(row=15, column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame,textvariable=RoomNo, state='readonly',font=('arial', 12,'bold'), width=18)                                        
        self.cboRoomNo['value']=('','001','002','003','004','005','006','007','008','009','010')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, pady=3, padx=20)

        self.lblRoomExtNo=Label(LeftFrame, font=('arial', 12,'bold'), text="Room Ext. No:",padx=2,pady=2,bg="pink2")
        self.lblRoomExtNo.grid(row=16, column=0,sticky=W)
        self.cboRoomExtNo=ttk.Combobox(LeftFrame,textvariable=RoomExtNo, state='readonly',font=('arial', 12,'bold'), width=18)                                        
        self.cboRoomExtNo['value']=('','101','102','103','104','105','106','107','108','109','110')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16, column=1, pady=3, padx=20)  

        #======================================Receipt==================================================================
        self.lblLabel = Label(RightFrame, font=('arial', 10, 'bold'),pady=10,padx=10,bg="light coral",
        text="Customer Ref\tFirstname\tSurname\tAdr\tPostCode\tMobile\tState\tCheckInDate\tCheckOutDate")
        self.lblLabel.grid(row = 0, column=0,columnspan=17)

        self.txtReceipt = Text(RightFrame, height = 15, width = 108,bd=16,font=('arial', 11, 'bold'))
        self.txtReceipt.grid(row=1,column=0, columnspan=10,padx=10,pady=5)
        #======================================Receipt==================================================================
        self.lblDays= Label(RightFrame,font=('arial', 14,'bold'), text="No. of Days", bd=7,bg="light coral",fg="black",)
        self.lblDays.grid(row=2,column=0, sticky=W)
        self.txtDays  = Entry(RightFrame,font=('arial', 14,'bold'), textvariable=TotalDays, bd=7, bg="white",
                               width=67, justify=LEFT)
        self.txtDays.grid(row=2,column=1)

        self.lblPaidTax = Label(RightFrame,font=('arial', 14,'bold'), text="Paid Tax", bd=7,bg="light coral",fg="black",)
        self.lblPaidTax.grid(row=3,column=0, sticky=W)
        self.txtPaidTax  = Entry(RightFrame,font=('arial', 14,'bold'), textvariable=PaidTax, bd=7, bg="white",
                               width=67, justify=LEFT)
        self.txtPaidTax.grid(row=3,column=1)

        self.lblSubTotal = Label(RightFrame,font=('arial', 14,'bold'), text="Sub Total", bd=7,bg="light coral",fg="black",)
        self.lblSubTotal.grid(row=4,column=0, sticky=W)
        self.txtSubTotal= Entry(RightFrame,font=('arial', 14,'bold'), textvariable=SubTotal, bd=7, bg="white",
                                  width=67, justify=LEFT)
        self.txtSubTotal.grid(row=4,column=1)

        self.lblTotalCost = Label(RightFrame,font=('arial', 14,'bold'), text="Total Cost", bd=7,bg="light coral",fg="black",)
        self.lblTotalCost.grid(row=5,column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame,font=('arial', 14,'bold'), textvariable=TotalCost, bd=7, bg="white",
                                  width=67)
        self.txtTotalCost.grid(row=5,column=1)
        #=================================================================================================================
        self.btnTotal=Button(BottomFrame,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2,bg="light salmon",text="Total ",command=TotalCostandDate).grid(row=0, column=3,padx=4)

        self.btnReceipt=Button(BottomFrame,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2,bg="light salmon",text="Receipt", command=Receipt).grid(row=0, column=4,padx=5)

        self.btnClear=Button(BottomFrame,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2,bg="light salmon",text="Clear",command=Clear).grid(row=0, column=5,padx=5)

        self.btnDelete=Button(BottomFrame,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2,bg="light salmon", text="Delete", command=Delete).grid(row=0, column=6,padx=5)
        
        self.btnExit=Button(BottomFrame,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2,bg="dark salmon", text="Exit", command=iExit).grid(row=0, column=7,padx=5)
        
        




if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()
