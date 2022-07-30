'''
 ########::::: ###:::: ##    ##: ##    ##: ####: ##    ##:  ######:      ########:  ########:   #######:   #######: ########:  ######:  ########:    
 ##     ##:::'## ##::: ###   ##: ##   ##: . ## : ###   ##: ##    ##::    ##     ##: ##     ##: ##     ##:       ##: ##:       ##    ##:... ##:
 ##     ##::'##   ##:: ####  ##: ##  ##:: : ## : ####  ##: ##      ::    ##     ##: ##     ##: ##     ##:       ##: ##:       ##     ::::: ##: 
 ########::'##     ##: ## ## ##: #####::: : ## : ## ## ##: ##   ####:    ########:  ########:  ##     ##:       ##: ######:   ##     ::::: ##: 
 ##     ##: #########: ##  ####: ##  ##:: : ## : ##  ####: ##    ##::    ##:        ##   ##:   ##     ##: ##    ##: ##:       ##     ::::: ##: 
 ##     ##: ##     ##: ##   ###: ##   ##: : ## : ##   ###: ##    ##::    ##:        ##    ##:  ##     ##: ##    ##: ##:       ##    ##:::: ##: 
 ########:: ##     ##: ##    ##: ##    ##:'####: ##    ##:. ######:::    ##:        ##     ##:  #######:   ######:  ########:  ######::::: ##: 
........:::..:::::..::..::::..::..::::..::....::..::::..:::......::::    .:::::::::..:::::..:::.......::::......:::........:::......::::::..::   

'''
#==========================================================================================
#                            IMPORTING MODULES BASIC MODULES
#==========================================================================================


import os
import sys
import easygui
import pyttsx3
import subprocess
from easygui import *
from mysql.connector import Error                   
from mysql.connector import errorcode


#==========================================================================================
#                             INSTALLING MODULES & PACKAGES
#==========================================================================================


#==========================================================================================

engine = pyttsx3.init()
sound = engine.getProperty('voices')

engine.setProperty('voice',sound[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

speak('WELCOME TO MY BANK MANAGEMENT SYSTEM')

#==========================================================================================

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

speak("PLEASE CLICK ON START BUTTON TO INSTALL PACKAGES FOR THIS PROGRAM IF THEY ARE NOT PRESENT IN YOUR SYSTEM")

version = "Package Installation"
options = ["  START  ","  CANCEL  "]
button = buttonbox("INSTALL PACKAGES FOR THIS PROGRAM IF THEY ARE NOT PRESENT IN YOUR SYSTEM",title=version,choices=options)

if button == options[0]:
    speak("it will take few minutes, depends on your system's performance and internet connection")

    install('mysql.connector')
    install('tabulate')
    install('pyfiglet')
    install('termcolor')
    install('stdiomask')
    install('colorama')
    install('easygui')
    install('tkinter')
    install('matplotlib')

    button = "PACKAGES INSTALLED SUCCESSFULLY"
    os.system('cls')    

else:
    os.system('cls')

#==========================================================================================
#                         IMPORTING MODULES AFTER INSTALLATION
#==========================================================================================

import time                                                               
import stdiomask                                
import string
import csv

import colorama                                 
import pyfiglet                                 
import mysql.connector as mycon                
import matplotlib.pyplot as plt

from tkinter import *
from tabulate import tabulate
from stdiomask import *

from pyfiglet import figlet_format              
from colorama import init,Back as bg            
init(strip=not sys.stdout.isatty())             
from termcolor import cprint                    

#==========================================================================================
#                                       ABOUT
#==========================================================================================

def about():
    
    a = '''

    About the Project:
    ~~~~~~~~~~~~~~~~~

    Talking about the features of this Bank Management System, the Admin can create an account by providing the required data of the customer
    along with his/her initial amount which is to be deposited.Admin can also view the statistical representation of amount per person.The admin
    can also view the customer's details, modify the details or delete the details of any customer.

    The Customer can also deposit and withdraw money just by providing the user account number and entering the amount and perform the
    transactions. This simple console-based system provides the simplest management of bank account and transactions.

    All the data's are stored in tabular form in a relational database i.e. MySQL database which is a free and open-source
    software under the terms of the GNU General Public License, and is also available under a variety of proprietary licenses. MySQL was owned
    and sponsored by the Swedish company MySQL AB, which was bought by Sun Microsystems (now Oracle Corporation).
    '''
 

           

                                        
    

    os.system('cls')

    text = "ABOUT :-"
    cprint(figlet_format(text, font="starwars"), "blue")
  
    cprint(a,'cyan')
    #cprint(b,'cyan')

    version = "About The Project"
    options = ["  YES  ","  NO  "]
    button = buttonbox("DO YOU WANT TO LISTEN ABOUT THIS PROJECT",title=version,choices=options)

    if button == options[0]:

        speak('''This project has been created by tanmay sarkary''')
        speak(a)
    else:
        pass
    
    while True:

        cprint('DO YOU WANT TO CONTINUE (Y/N) :-','green')
        speak('DO YOU WANT TO CONTINUE')
        ab_input = input('>>>  ').lower()
        
        if ab_input == "":
            cprint('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE,PLEASE TRY AGAIN','yellow')
            speak('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE, PLEASE TRY AGAIN')

        elif ab_input == 'y':
            os.system('cls')
            main()
                

        elif ab_input == 'n':
            cprint('EXITING PROGRAM')
            time.sleep(3)
            sys.exit()
    

        else:
            cprint('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE TRY AGAIN','yellow')


#==========================================================================================
#                                DATABASE CONNECTION
#==========================================================================================

#------------------------------------------------------------------------------------------
#               GETTING PASSWORD FOR AUTHENTICATION AND AUTHORISATION
#------------------------------------------------------------------------------------------

speak("CLICK ON 'YES' BUTTON IF YOUR MySQL USER-NAME IS ROOT")

version = "USER-NAME"
options = ["  YES  ","  NO  "]
button = buttonbox("CLICK ON 'YES' BUTTON IF YOUR MySQL USER-NAME IS ROOT",title=version,choices=options)

if button == options[0]:
    c = 'root'

else:
    speak("PLEASE ENTER YOUR MySQL USERNAME:-")
    c = easygui.enterbox("ENTER YOUR MY-SQL USERNAME:-")

speak('PLEASE ENTER YOUR MySQL PASSWORD')
p = passwordbox('ENTER YOUR MySQL PASSWORD :-')

#==========================================================================================

while True:

    try:
        con=mycon.connect(host = 'localhost',user = c,passwd = p)
        mycursor=con.cursor()
        break

    except mycon.Error as error:

        print("Failed to Connect with DATABASE {}".format(error))
        speak('ERROR IS FOUND, PLEASE ENTER YOUR MySQL PASSWORD AGAIN')
        p = passwordbox('ENTER YOUR MySQL PASSWORD :-')
        error=" "
        continue

    os.system('cls')

mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")

#==========================================================================================
#                                 CREATING TABLE
#==========================================================================================

mycursor.execute("""create table if not exists bank_master(
                        ID_NO bigint(15) primary key NOT NULL UNIQUE,
                        NAME VARCHAR(20) NOT NULL,
                        DOB DATE NOT NULL,
                        ADDRESS VARCHAR(35) NOT NULL,
                        PH_NO BIGINT(15) NOT NULL,
                        EMAIL VARCHAR(35),
                        ACC_TYPE VARCHAR(2) NOT NULL,
                        AMOUNT BIGINT(15) NOT NULL);""")


#==========================================================================================
#                               INSERTING DATA/VALUES
#==========================================================================================

speak('DO YOU WANT TO INSERT SOME BY-DEFAULT DATA IN YOUR MySQL DATABASE ?')
version = "DEFAULT-DATA"
options = ["  YES  ","  NO  "]
button = buttonbox("DO YOU WANT TO INSERT SOME BY-DEFAULT DATA IN YOUR MySQL DATABASE ?", title = version, choices = options)

if button == options[0]:

    value0 = '''insert into bank_master
    values(625100200,'tanmay sarkar','2002-11-20','MALDA',9775766850,'rajrishi0219@gmail.com','c',160000)'''    

    value1 = '''insert into bank_master
    values(625100201,'SAYETA BISWAS','2002-05-11','MALDA',9784563210,'sayeta@gmail.com','c',80000)'''

    value2 = '''insert into bank_master
    values(625100202,'SHAN','2003-02-19','DELHI',9563244474,'rdjshan@gmail.com','c',75000)'''    

    value3 = '''insert into bank_master
    values(625100203,'rajrishi mitra','2002-03-21','MALDA',8745691233,'tanmay026@gmail.com','c',90000)'''

    value4 = '''insert into bank_master
    values(625100204,'HIMANSHU YADAV','2002-11-20','JAMMU & KASHMIR',7884563210,'himanshu@gmail.com','c',65000)'''    

    value5 = '''insert into bank_master
    values(625100205,'RAHUL KUMAR','2001-01-10','KOLKATA',6543219787,'rahulkumar@gmail.com','c',50000)'''

    mycursor.execute(value0)
    mycursor.execute(value1)
    mycursor.execute(value2)
    mycursor.execute(value3)
    mycursor.execute(value4)
    mycursor.execute(value5)
    
    con.commit()

    easygui.msgbox('DATA ADDED SUCCESSFULLY . . . !')
    speak('DEFAULT DATA ADDED SUCCESSFULLY')
    time.sleep(2)
    os.system('cls')

else:
    os.system('cls')

#==========================================================================================
#                                        ADMIN
#==========================================================================================

def admin():

#------------------------------------------------------------------------------------------
#                     USERNAME & PASSWORD VERIFICATION USING "TKINTER"
#------------------------------------------------------------------------------------------

    window = Tk()
    window.title('BANKING LOGIN PAGE')
    window.configure(background='cyan')

    #FRAME BLUEPRINT
    
    width = 320
    height = 380
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))

    #COMMAND FUNCTIONS

    def click():

        ent_text=textentry.get()
        pass_text=pw_entry.get()
        user1 = ['tanmay','raja']

        if ent_text in user1 and pass_text == '0000':
            speak('YOU ARE A VALID USER')
            output.insert(END,'YOU ARE A VALID USER. . .\n')

        else:
            speak('YOU ARE AN INVALID USER')
            output.insert(END,'YOU ARE AN INVALID USER. . . TRY AGAIN\n')

    def fun1():

        window.destroy()
        cprint('\t\t\t\t\t\t\t LOGIN SUCCESFULL, CONTINUE\n \t\t\t\t\t\t\t\tPRESS ENTER','green')
        os.system('cls')

        cprint('*'*167,'cyan')
        print()

        cprint('\t\t\t\t\t\t\t\t\t WELCOME TO BANK MANAGEMENT SYSTEM','magenta')
        speak('WELCOME TO BANK MANAGEMENT SYSTEM')
        print()
        cprint('*'*167,'cyan')
        print()
        admin_menu()

    #LABEL FOR USERNAME
    
    lbl_username = Label(window,text='USERNAME:',bg='cyan',fg='black',font='algerian 15')
    lbl_username.grid(row=2,column=0,sticky=W)
    textentry = Entry(window,width=20,bg='deep sky blue',fg='black')
    textentry.grid(row=2,column=1)

    #LABEL FOR PASSWORD

    lbl_password = Label(window,pady=20,text='PASSWORD:',bg='cyan',fg='black',font='algerian 15')
    lbl_password.grid(row=3,column=0,sticky=W)
    pw_entry = Entry(window,show='*',width=20,bg='tomato',fg='black')
    pw_entry.grid(pady=20,row=3,column=1)

    #OUTPUT BOX TO PRINT VALID OR INVALID

    output = Text(window,width=40,height=4,wrap=WORD,bg = 'black',fg='white')
    output.grid(pady=25,row=5,columnspan=2)

    #SUBMIT BUTTON

    btn_submit = Button(window,text='SUBMIT',width=30,command=click,bg='yellow')
    btn_submit.grid(pady=25,row=4,columnspan=2)

    #LOGIN BUTTON
    
    btn_login = Button(window,text='LOGIN',width=30,command=fun1,bg='green2')
    btn_login.grid(pady=25,row=6,columnspan=2)
    
#------------------------------------------------------------------------------------------

    window.mainloop()

def admin_menu():
    
    text = "ADMIN :-"
    cprint(figlet_format(text, font="starwars"), "cyan")
    speak('ADMIN MENU')
    
    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')
    speak(time.asctime())
       
    cprint('''1.ABOUT CUSTOMER
2.ACTIONS
3.STATISTICAL REPRESENTATION
4.DATA BACKUP''','blue')
    
    cprint('5.RETURN TO MAIN MENU','green')
    cprint('6.EXIT\n','red')
    cprint('ENTER YOUR CHOICE :','yellow')
    act = input('>>>  ')

    if act == '1':

        os.system('cls')
        cprint('*'*167,'blue')    
        text = "DATA :-"
        cprint(figlet_format(text, font="starwars"), "cyan")
        cprint('*'*167,'blue')

        aview()
        
    if act == '2':
        actions()

    if act == '5':
        os.system('cls')
        main()

    if act == '3':
        os.system('cls')
        graph()

    if act == '4':
        backup()
        
    if act == '6':
        time.sleep(3)
        sys.exit()

def aview():

    speak('PLEASE ENTER THE PIN')
    v_password = passwordbox('PLEASE ENTER PIN :-')
       
    pin = ['0000']

    if v_password in pin:

        mycursor.execute('select * from bank_master')
        result = mycursor.fetchall()
        print(tabulate(result, headers = ['id_no','name','dob','address','ph_no','email','acc_type','amount'], tablefmt=('grid')))
        
    else:
        speak('You Are Not An Authorized User')
        print('You Are Not An Authorized User')



def actions():

    os.system('cls')
    cprint('*'*167,'magenta')

    text = "ACTIONS"

    cprint(figlet_format(text, font="starwars"), "cyan")
    cprint('*'*167,'magenta')

    cprint('\t\tWhat You Want To Do...','yellow')
    speak('What You Want To Do')

    b='''\n\t\t\t\t1.INSERT CUSTOMER DETAILS
            \t\t\t2.UPDATE CUSTOMER DETAILS
            \t\t\t3.DELETE CUSTOMER DETAILS
            \t\t\t4.RETURN TO MAIN MENU'''
    cprint(b,'blue')
    speak(b)

    cprint('''\t\t\t\t5.EXIT''','red')

    print()
    cprint('ENTER YOUR CHOICE :','yellow')
    speak('ENTER YOUR CHOICE')

    ainput = input('>>>  ')

    if ainput == '1':
        insert()

    if ainput == '2':
        update()

    if ainput == '3':
        delete()

    if ainput == '4':
        os.system('cls')
        main()

    if ainput == '5':
        time.sleep(3)
        sys.exit()

def insert():

    speak('Enter customer details')
    msg = "Enter Costumer's personal information"
    title = "ENTER CUSTOMER DETAILS"
    fieldNames = ["NAME", "DOB (YYYY-MM-DD)", "ADDRESS","PHONE NO.","E-MAIL ID","ACCOUNT TYPE(C/S)","AMOUNT (IN ₹)" ]
    Values = multenterbox(msg, title, fieldNames)

    if Values is None:
        sys.exit(0)

    # MAKE SURE THAT NONE OF THE FIELDS WERE LEFT BLANK

    while 1:

        errmsg = ""
        for i, name in enumerate(fieldNames):

            if Values[i].strip() == "":
              errmsg += "{} Is A Required Field.\n\n".format(name)

        if errmsg == "":
            break                   
        Values = multenterbox(errmsg, title, fieldNames, Values)

        if Values is None:
            break
    try:
        x = Values
        b = tuple(x)
        insert_list = [b]
        
        name = x[0]
        dob = x[1]
        address=x[2]
        ph_no = x[3]
        email = x[4]
        acc_type = x[5]
        amount = x[6]
        
        count=625100200

        q = "select id_no from bank_master"
        mycursor.execute(q)
        m=mycursor.fetchall()

        for i in m:
            count+=1

        insert_values = 'insert into bank_master() VALUES(%s, %s, %s,%s, %s, %s, %s, %s)'
        row = [(count,name,dob,address,ph_no,email,acc_type,amount)]
        mycursor.executemany(insert_values, row)
        con.commit()

        msg = "DATA SUCCESSFULLY UPLOADED \nHELLO {} YOUR ID-NUMBER IS {} ".format(name,count)
        speak(msg)
        
        msgbox(msg)

        print(tabulate(insert_list,headers=['id_no','name','dob','address','ph_no','email','acc_type','amount'], tablefmt=('grid')))

    except:

        if x == None:
            cprint("No data given","red")
    
    speak('DO YOU WANT TO INSERT MORE DETAILS')
    d=input('DO YOU WANT TO INSERT MORE DETAILS (Y/N) :').lower()

    if d == 'y':
        insert()    

def delete():

    d_no = int(input('IDENTITY CARD NUMBER WHICH YOU WANT TO DELETE :'))
    del_command = 'DELETE FROM bank_master WHERE ID_NO = %s'
    delt = (d_no ,)
    mycursor.execute(del_command, delt)
    con.commit()

    speak('DATA DELETED SUCCESSFULLY')
    print('DATA DELETED SUCCESSFULLY')

def update():

    i_input = int(input('ENTER THE IDENTITY CARD NUMBER :'))

    cprint(''' WHAT YOU WANT TO UPDATE
        \n\t1.NAME
        2.ADDRESS
        3.PHONE_NO
        4.EMAIL ''','green')
    cprint('''\t5.RETURN TO PREVIOUS MENU
        6.RETURN TO MAIN MENU\n''','green')

    cprint('ENTER YOUR CHOICE :','yellow')
    u_input = input('>>>  ')

    if u_input == '1':

        up_name = input('NAME :').upper()
        up_command = 'UPDATE bank_master SET NAME= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('NAME UPDATED SUCCESSFULLY')

    if u_input == '2':

        up_name = input('ADDRESS :').upper()
        up_command ='UPDATE bank_master SET ADDRESS= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('ADDRESS UPDATED SUCCESSFULLY')
        

    if u_input == '3':

        up_name = int(input('PHONE_NO :'))
        up_command='UPDATE bank_master SET PH_NO= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('PHONE NO. UPDATED SUCCESSFULLY')

    if u_input == '4':

        up_name = input('EMAIL :')
        up_command = 'UPDATE bank_master SET EMAIL= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('EMAIL UPDATED SUCCESSFULLY')

    if u_input == '5':
        os.system('cls')
        actions()        

    if u_input == '6':
        os.system('cls')
        admin_menu()

#------------------------------------------------------------------------------------------
#                                        GRAPH
#------------------------------------------------------------------------------------------

def graph():

    cprint('*'*167,'blue')
    print()

    text="GRAPH :-"
    cprint(figlet_format(text, font="slant"), "cyan")
    
    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')
    cprint('*'*167,'blue')

    s = 'select name from bank_master'
    mycursor.execute(s)
    data = mycursor.fetchall()
    l = []

    for i in data:
        l.append(i[0])
        
    am = 'select amount from bank_master'    
    mycursor.execute(am)
    amount = mycursor.fetchall()
    m = []

    for j in amount:
        m.append(j[0])

    speak('enter your choice for analysing')

    cprint('HOW DO YOU WANT TO ANALYSE ?','yellow')
    cprint('''\n1.BAR GRAPH
2.LINE GRAPH''','green')
    print()

    cprint('ENTER YOUR CHOICE','yellow')
    gr_input=input('>>>  ')

    if gr_input == '1':

        plt.bar(l,m,)
        plt.xticks(fontsize = 6,rotation = 30)
        plt.xlabel('NAMES ---->')
        plt.ylabel('AMOUNT ---->')

        plt.grid(b = True, which = 'major', color = '#666666', linestyle = '-')
        plt.title('CUSTOMER vs AMOUNT graph')

    if gr_input == '2':

        plt.plot(l,m,'c',marker = '*',markersize = 6,markeredgecolor = 'r')
        plt.xticks(fontsize = 6,rotation = 30)
        plt.xlabel('NAMES ---->')
        plt.ylabel('AMOUNT ---->')

        plt.grid(b = True, which = 'major', color = '#666666', linestyle = '-')
        plt.title('CUSTOMER vs AMOUNT graph')

    plt.show()
        
#==========================================================================================
#                                    CUSTOMER
#==========================================================================================

c_accno = 0

def customer():

    mycursor.execute('select * from bank_master')
    a = mycursor.fetchall()

    global c_accno
    title = "CUSTOMER ACCOUNT"
    fieldNames = ["ENTER YOUR NAME", "ENTER ID NO" ]

    msg = "Enter The Required Informations"
    values = multenterbox(msg, title, fieldNames)
    x = values

    for i in a:

        if str(i[0]) == x[1] and i[1].lower() == x[0].lower():

            c_accno = x[1]
            speak('You Are Valid Customer')
            easygui.msgbox('You Are Valid Customer. . . !')

            time.sleep(1)            
            os.system('cls')
            
            customer_menu()
    
def customer_menu():

    cprint('*'*167,'blue')
    print()

    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')

    print()
    cprint('*'*167,'blue')

    speak('welcome')
    speak('you have successfully logged into your account')
    speak('now you can perform the following operations')

    cprint('''WHAT DO YOU WANT TO DO. . .
                
                1.VIEW AMOUNT
                2.TRANSACTION
                3.RETURN TO MAIN MENU
                4.EXIT''','green')
    print()

    speak('enter your choice')
    cprint('ENTER YOUR CHOICE :','yellow')

    c_input = input('>>>  ')

    if c_input == '1':

        mycursor.execute("select name,amount from bank_master where ID_NO='"+c_accno+"'")
        result = mycursor.fetchall()
        speak('{} ,you have rupees {} in your account'.format(result[0][0],result[0][1]))
        easygui.msgbox('\t\t\tACCOUNT NO :-   {}\n\t\t\tNAME :-\t\t{}\n\t\t\tAMOUNT :-\t\t₹{}'.format(c_accno,result[0][0],result[0][1]),'YOUR AMOUNT','¤¤ DONE ¤¤')
        
    if c_input == '2':
        transaction()

    if c_input == '3':
        os.system('cls')
        main()

    if c_input == '4':
        time.sleep(2)
        sys.exit()
    
#------------------------------------------------------------------------------------------
#                                   TRANSACTION
#------------------------------------------------------------------------------------------
    
def transaction():

    version= 'TRANSACTIONS'
    options = ["  DEPOSIT MONEY  ","  WITHDRAW MONEY  "]
    speak('what to you want to perform')
    button = buttonbox("\t\t\t\tWHAT YOU WANT TO DO :-",title = version,choices = options)
        
    if button == options[0]:

        dp = int(input("Enter Amount To Be Deposited:"))
        mycursor.execute("update bank_master set AMOUNT=AMOUNT+'"+str(dp)+"' where ID_NO='"+c_accno+"'")
        con.commit()
        
        mycursor.execute("select AMOUNT from bank_master where ID_NO='"+c_accno+"'")
        amount = mycursor.fetchall()

        speak('MONEY HAS BEEN DEPOSITED SUCCESSFULLY')
        easygui.msgbox('MONEY HAS BEEN DEPOSITED SUCCESSFULLY ! ! !\nYOU HAVE ₹ {} IN YOUR ACCOUNT'.format(amount[0][0]))
            
    if button == options[1]:

        wd = int(input("Enter amount to be withdrawn:"))
        mycursor.execute("update bank_master set AMOUNT=AMOUNT-'"+str(wd)+"' where ID_NO='"+c_accno+"'")

        mycursor.execute("select AMOUNT from bank_master where ID_NO='"+c_accno+"'")
        amount = mycursor.fetchall()

        speak('MONEY HAS BEEN WITHDRAWN SUCCESSFULLY')
        easygui.msgbox('MONEY HAS BEEN WITHDRAWL SUCCESSFULLY ! ! !\nYOU HAVE ₹ {} IN YOUR ACCOUNT'.format(amount[0][0]))

#------------------------------------------------------------------------------------------
#                                   DATA BACKUP
#------------------------------------------------------------------------------------------

def backup():

    f = open('backup.csv','w+')
    mycursor.execute('select * from bank_master')
    
    fetch_file = mycursor.fetchall()
    w = csv.writer(f)

    for row in fetch_file:

        w.writerow([str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7])])

    speak('DATA BACKED-UP SUCCESSFULLY')
    easygui.msgbox('DATA BACKED-UP SUCCESSFULLY. . . !')

#==========================================================================================
#                                       MAIN
#==========================================================================================

def admin_main():

    speak('PLEASE ENTER USER-NAME AND PASSWORD')
    admin()    

    while (input('DO YOU WANT TO CONTINUE THE PROGRAM  (Y/N) :').lower()) == 'y':

        os.system('cls')
        cprint('*'*167,'cyan')
        print()

        cprint('\t\t\t\t\t\t\t\tWelcome To BANK SYSTEM','green')
        print()
        cprint('*'*167,'cyan')

        print()
        admin_menu()

    else:
        print('EXITING ADMIN')
        
#------------------------------------------------------------------------------------------

def customer_main():

    text = "CUSTOMER"
    cprint(figlet_format(text, font="starwars"), "cyan")

    customer()   

    while input('DO YOU WANT TO CONTINUE THE PROGRAM (Y/N) :').lower() == 'y':

        os.system('cls')
        customer_menu()

    else:
        print('EXITING CUSTOMER')

#==========================================================================================

def main():

    text = "WELCOME"    
    cprint(figlet_format(text, font="starwars"), "cyan")
    speak('welcome')
    time.sleep(2)
    os.system('cls')
    
    text = "BANKING"
    cprint(figlet_format(text, font="banner3-D"), "cyan")
    
    
    cprint('*'*167,'blue')
    
    print()
    print()
    
    cprint('\t\t\t\t\t\t\t WELCOME TO OUR BANK MANAGEMENT SYSTEM','green', attrs=['bold'])

    cprint('''\t\t\t\t\t\t\t\t\t\t\t\t\t\t CREATED BY :- Tanmay sarkar''',
            'red', attrs=['blink'])

    cprint('*'*167,'blue')

    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'magenta')

    print('\t\tWHAT YOU WANT TO VIEW\n')
    cprint('\t\t\t\t1.ADMIN','yellow')
    cprint('\t\t\t\t2.CUSTOMER','green')
    cprint('\t\t\t\t3.ABOUT','cyan')
    cprint('\t\t\t\t4.EXIT','red')
    print()
    
    cprint('ENTER YOUR CHOICE :','yellow')
    a=input('>>>  ')

    if a == '1':
        admin_main()
    
    elif a == '2':
        speak('please enter the name and id number')
        customer_main()

    elif a == '3':
        about()

    elif a == '4':

        print('THANK YOU. . . . .\nEXITING PROGRAM . . . .')
        time.sleep(3)
        sys.exit()

    else:
        print('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICES')

main()
