import tkinter as tk                
import mysql.connector as mysql
import datetime
import uuid


current_balance= 1000
current_name= 'Joe'
current_pin= 223
def_id= ''


#Defines the frame that appears on screen
class ATMFrame(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.shared_data={'Balance':tk.IntVar()}
        #Creates the frame 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomeScreen, MenuPage, WithdrawPage, DepositPage, BalancePage, RegistrationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

    #chooses which of the pages to display first
        self.show_frame("HomeScreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomeScreen(tk.Frame):

    def __init__(self, parent, controller):

        #creates the display of the start page
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller

        self.controller.title('Sunset Savings')
        #Opens the frame in full screen
        self.controller.state('zoomed')

        #Creates the Bank name at the top
        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        space_label= tk.Label(self,height=4,bg='#000066')
        space_label.pack()

        #A label that creates the text "Please Enter Your Password"
        pass_label = tk.Label(self,
                              text="Please Enter Your PIN",
                              font=('Lucida Sans Unicode',15),
                              bg='#000066',
                              foreground='white')
        pass_label.pack(pady=10)

        #Entry box for the password
        my_password=tk.StringVar()
        pass_entry=tk.Entry(self,
                            textvariable=my_password,
                            font=('Lucida Sans Unicode', 12),
                            width=22)

        pass_entry.focus_set()
        pass_entry.pack(ipady=7)

        def handle_focus(_):
            pass_entry.configure(show='*', fg='black')
            
        pass_entry.bind('<FocusIn>',handle_focus)


        def check_pass():
            global def_id
            pin= int(my_password.get())
            #print ('pin:' ,(pin))
            mysql_conn = mysql.connect(user='youssefmoustafa', password='Lollol123456789',
                              host='localhost',
                              database='atm_database')
            cursor = mysql_conn.cursor()

            query = ('select userid from users where pin=%s limit %s')
            

            cursor.execute(query, (pin, 1))
            result = cursor.fetchall()
            if len(result)>0:
                for (userid) in result:
                    def_id = userid[0]
                controller.show_frame('MenuPage')
                print('logn id: ', def_id)  
                    

            else:
                wrong_pass['text']='Incorrect PIN, Please Try Again'
                
            cursor.close()
            mysql_conn.commit()
            mysql_conn.close()
            
            #if my_password.get() == '0000':
                #my_password.set('')
                #wrong_pass['text']=''
            #controller.show_frame('MenuPage')
            
            
        enter_button=tk.Button(self,
                               relief='raised',
                               borderwidth=5,
                               width=30,
                               height=3,
                               fg='white',
                               bg='black',
                               command=check_pass,
                               text='Enter')
        enter_button.pack(pady=10)


        def reg_screen():
            controller.show_frame('RegistrationPage')
        register_button= tk.Button(self,
                                   relief='raised',
                                   borderwidth=5,
                                   width=30,
                                   height=3,
                                   fg='white',
                                   bg='blue',
                                   command=reg_screen,
                                   text='Register')
        register_button.pack()
                                   

        wrong_pass=tk.Label(self,
                            text='',
                            font=('Lucida Sans Unicode',13),
                            fg='red',
                            bg='#000066')
        wrong_pass.pack()





class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#000066')
        self.controller = controller

        #Creates the Bank name at the top
        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        mainMenu_label=tk.Label(self,
                                text='Welcome to the Main Menu, Please Select A Service.',
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                width=130,
                                height=2)
        mainMenu_label.pack()
        

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill='both',expand=True)


        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button=tk.Button(button_frame,
                                  text='Withdraw',
                                  relief='raised',
                                  borderwidth=5,
                                  width=50,
                                  height=5,
                                  bg='#000066',
                                  fg='white',
                                  command=withdraw)
        withdraw_button.grid(row=0,column=5,pady=10,padx=470)


        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button=tk.Button(button_frame,
                                  text='Deposit',
                                  relief='raised',
                                  borderwidth=5,
                                  width=50,
                                  height=5,
                                  bg='#000066',
                                  fg='white',
                                  command=deposit)
        deposit_button.grid(row=1,column=5,pady=10)


        def balance():
            controller.show_frame('BalancePage')
            
        balance_button=tk.Button(button_frame,
                                  text='Balance',
                                  relief='raised',
                                  borderwidth=5,
                                  width=50,
                                  height=5,
                                  bg='#000066',
                                  fg='white',
                                  command=balance)
        balance_button.grid(row=2,column=5,pady=10)


        def exit():
            controller.show_frame('HomeScreen')
            
        exit_button=tk.Button(button_frame,
                                  text='Exit',
                                  relief='raised',
                                  borderwidth=5,
                                  width=50,
                                  height=5,
                                  bg='#c83200',
                                  fg='black',
                                  command=exit)
        exit_button.grid(row=3,column=5,pady=10)


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#000066')
        self.controller = controller

        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        chooseAmount_label=tk.Label(self,
                                text='Choose An Amount You Would like to Withdraw.',
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                width=130,
                                height=2)
        chooseAmount_label.pack()
        

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            global def_id
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            mysql_conn = mysql.connect(user='youssefmoustafa', password='Lollol123456789',
                              host='localhost',
                              database='atm_database')
            cursor = mysql_conn.cursor()

            query = ("insert into withdraw(withdrawid,userid, withdraw_amount, withdraw_time) values"
                     "(%s, %s, %s, %s)")

            withid= str(uuid.uuid1())
            id= def_id
            amt = amount
            # ct stores current time
            time = datetime.datetime.now()

            cursor.execute(query, (withid, id, amt, time))

            cursor.close()
            mysql_conn.commit()
            mysql_conn.close()
        
        twenty_button= tk.Button(button_frame,
                                 text='20',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(20))
        twenty_button.grid(row=0,column=0,pady=10,padx=200)


        forty_button= tk.Button(button_frame,
                                 text='40',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(40))
        forty_button.grid(row=1,column=0,pady=10)

        sixty_button= tk.Button(button_frame,
                                 text='60',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(60))
        sixty_button.grid(row=2,column=0,pady=10)

        eighty_button= tk.Button(button_frame,
                                 text='80',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(80))
        eighty_button.grid(row=3,column=0,pady=10)

        hundred_button= tk.Button(button_frame,
                                 text='100',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(100))
        hundred_button.grid(row=0,column=1,pady=10)

        twohundred_button= tk.Button(button_frame,
                                 text='200',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(200))
        twohundred_button.grid(row=1,column=1,pady=10)

        fivehundred_button= tk.Button(button_frame,
                                 text='500',
                                 width=50,
                                 height=5,
                                 relief='raised',
                                 borderwidth=5,
                                 bg='#000066',
                                 fg='white',
                                 command=lambda:withdraw(500))
        fivehundred_button.grid(row=2,column=1,pady=10)

        cash= tk.StringVar()
        other_amount=tk.Entry(button_frame,
                              textvariable=cash,
                              width=59)
        other_amount.grid(row=3,column=1,pady=10,ipady=30)

        def other_enter(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount.bind('<Return>',other_enter)

        otherLabel= tk.Label(button_frame,
                                text='Other Amount',
                                font=('Lucida Sans Unicode',15,'bold'),
                                foreground='black')
        otherLabel.grid(row=4,column=1)


class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#000066')
        self.controller = controller

        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        #space_label= tk.Label(self,height=4,bg='#000066')
        #space_label.pack()

        dep_label=tk.Label(self,
                                text='Deposit Page',
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                width=130,
                                height=2)
        dep_label.pack()

        #A label that creates the text "Please Enter Your Password"
        enter_amount_label = tk.Label(self,
                              text="Enter Deposit Amount:",
                              font=('Lucida Sans Unicode',15),
                              bg='#000066',
                              foreground='white')
        enter_amount_label.pack(pady=10)

        cash= tk.StringVar()
        deposit_entry=tk.Entry(self,
                               textvariable=cash,
                               font=('Lucida Sans Unicode',14),
                               width=22)
        deposit_entry.pack(ipady=7)

        
        def deposit_cash():
            
            global current_balance
            global def_id
            deposit_cash = int(deposit_entry.get())
            current_balance += deposit_cash
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
            mysql_conn = mysql.connect(user='youssefmoustafa', password='Lollol123456789',
                              host='localhost',
                              database='atm_database')
            cursor = mysql_conn.cursor()

            query = ("insert into deposit(depositid, userid, deposit_amount, deposit_time) values"
                     "(%s, %s, %s, %s)")

            id = def_id
            amt = deposit_cash
            depid= str(uuid.uuid1())
            # ct stores current time
            time = datetime.datetime.now()

            cursor.execute(query, (depid,id, amt, time))

            cursor.close()
            mysql_conn.commit()
            mysql_conn.close()
        enter_button = tk.Button(self,
                                 text='Enter',
                                 relief='raised',
                                 borderwidth=5,
                                 width=30,
                                 height=3,
                                 fg='white',
                                 bg='black',
                                 command=deposit_cash)
        enter_button.pack(pady=10)



class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#000066')
        self.controller = controller

        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        global current_balance
        global def_id
        controller.shared_data['Balance'].set(current_balance)

        
        balance_label= tk.Label(self,
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                anchor='e',
                                width=130,
                                height=2,
                                textvariable=controller.shared_data['Balance'])
        balance_label.pack(fill='x')

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill='both',expand=True)


        def menu():
            controller.show_frame('MenuPage')
            
        menu_button= tk.Button(button_frame,
                               text='Menu',
                               relief='raised',
                               borderwidth=5,
                               width=50,
                               height=5,
                               bg='#000066',
                               fg='white',
                               command=menu)
        menu_button.grid(row=0,column=0,pady=5,padx=465)

        def exit():
            controller.show_frame('HomeScreen')
            
        exit_button= tk.Button(button_frame,
                               text='Exit',
                               relief='raised',
                               borderwidth=5,
                               width=50,
                               height=5,
                               bg='#000066',
                               fg='white',
                               command=exit)
        exit_button.grid(row=1,column=0,pady=5)

                
        
        def activity():
            global def_id
            controller.shared_data['Balance'].set(current_balance)
            mysql_conn = mysql.connect(user='youssefmoustafa', password='Lollol123456789',
                              host='localhost',
                              database='atm_database')
            cursor = mysql_conn.cursor()

            query = ('select users.userid as userid, username, depositid, deposit_amount, deposit_time, withdrawID, withdraw_amount, withdraw_time from users left join deposit on users.userid = deposit.userid left join withdraw on users.userid = withdraw.userid where users.userid = %s limit %s')

            
        
            

            cursor.execute(query, (def_id, 100))
            result = cursor.fetchall()
            #print('bal id: ', def_id)
            print('userID: ',result[0][0])
            print('username: ',result[0][1])
            if len(result)>0:
                for (userid, username, depositid, deposit_amount, deposit_time, withdrawID, withdraw_amount, withdraw_time) in result:
                    print('depositID: ', depositid)
                    print('deposit Amount: ', deposit_amount)
                    print('deposit_time: ', deposit_time)
                    print('withdrawID: ', withdrawID)
                    print('withdraw_amount: ', withdraw_amount)
                    print('withdraw_time: ', withdraw_time)
                    break
            else:
                print('yyyy')
            cursor.close()
            mysql_conn.commit()
            mysql_conn.close()
        
        act_label= tk.Button(button_frame,
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                width=130,
                                height=2,
                                text='Check Activity',
                                command= activity)
        act_label.grid(row=2,column=0,pady=5)
        
        #space_label= tk.Label(self,height=4,bg='#000066')
        #space_label.pack()


class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#000066')
        self.controller = controller

        headingLabel = tk.Label(self,
                                text='Sunset Savings ATM',
                                font=('Lucida Sans Unicode',45,'bold'),
                                foreground='white',
                                bg='#000066')
        headingLabel.pack(pady=25)

        #space_label= tk.Label(self,height=4,bg='#000066')
        #space_label.pack()

        dep_label=tk.Label(self,
                                text='Create a New Account',
                                font=('Lucida Sans Unicode',13),
                                fg='white',
                                bg='#c83200',
                                width=130,
                                height=2)
        dep_label.pack()


        name_label = tk.Label(self,
                              text='Enter Your Full Name:',
                              font=('Lucida Sans Unicode',15),
                              fg='white',
                              bg='#000066')
        name_label.pack(pady=10)


        name= tk.StringVar()
        name_entry=tk.Entry(self,
                               textvariable=name,
                               font=('Lucida Sans Unicode',14),
                               width=22)
        name_entry.pack(ipady=7)

                              
        pin_label = tk.Label(self,
                              text='Create PIN:',
                              font=('Lucida Sans Unicode',15),
                              fg='white',
                              bg='#000066')
        pin_label.pack(pady=10) 

        pin= tk.IntVar()
        pin_entry=tk.Entry(self,
                               textvariable=pin,
                               font=('Lucida Sans Unicode',14),
                               width=22)
        pin_entry.pack(ipady=7)

        def enter():
            global current_name
            global def_id
            controller.show_frame('MenuPage')
            enter_name = name_entry.get()
            current_name += enter_name
            name.set('')
            def_id=str(uuid.uuid1())
            
            global current_pin
            enter_pin = int(pin_entry.get())
            current_pin += enter_pin
            mysql_conn = mysql.connect(user='youssefmoustafa', password='Lollol123456789',
                              host='localhost',
                              database='atm_database')
            cursor = mysql_conn.cursor()

            query = ("insert into users(userID, username, pin) values"
                     "(%s, %s, %s)")

            
            
            id= def_id    
            amt = enter_name
            pin = enter_pin

            cursor.execute(query, (id, amt, pin))

            cursor.close()
            mysql_conn.commit()
            mysql_conn.close()
            
        reg_button= tk.Button(self,
                                   relief='raised',
                                   borderwidth=5,
                                   width=30,
                                   height=3,
                                   fg='white',
                                   bg='blue',
                                   text='Create Account',
                                   command=enter)
        reg_button.pack(pady=7)


if __name__ == "__main__":
    app = ATMFrame()
    app.mainloop()
