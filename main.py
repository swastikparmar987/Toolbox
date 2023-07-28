from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import * # importing everything from filedialog
import mysql.connector as mysql
import random
import webbrowser

bg_colour = '#242424'
txt_cover = '#2e95fd'

sql_password = input("Enter sql password : ")

def register():
    username_value = username.get()
    password_value = password.get()

    if username_value == "Enter User Name":
        messagebox.showerror("Error", "Username cannot be empty!")
        return
    if password_value == "Enter password":
        messagebox.showerror("Error", "Password cannot be empty!")
        return

    try:
        my_connection = mysql.connect(
            host="localhost",
            user="root",
            password=sql_password,
            database="cs_project"
        )
        cur = my_connection.cursor()

        check_query = "SELECT * FROM sign_in_data WHERE user_id = '{}'".format(username_value)
        cur.execute(check_query)
        if cur.fetchone():
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            cur.close()
            my_connection.close()
            return

        insert_query = "INSERT INTO sign_in_data VALUES ('{}', '{}')".format(username_value, password_value)
        cur.execute(insert_query)
        my_connection.commit()
        messagebox.showinfo("Success", "Registration successful!")
        cur.close()
        my_connection.close()
        menu()

    except Exception as e:
        print(e)
        messagebox.showerror("ERROR", "An error occurred while registering.")



def login():
    bg_colour = '#242424'
    txt_cover = '#2e95fd'


    mysqlcon = mysql.connect(host = 'localhost' , user = 'root' , password = sql_password , database = 'cs_project')
    cursor_object = mysqlcon.cursor()

    def Checking_userInputs():
        username_value = user_name.get()
        Password_value = password.get()
        sql_query = 'select * from sign_in_data'
        cursor_object.execute(sql_query)
        User_login_Data_from_sql = cursor_object.fetchall()
        for userid_fromsql,passkey_fromsql in User_login_Data_from_sql:
            if (username_value,Password_value) == (userid_fromsql,passkey_fromsql):
                messagebox.showinfo("Success" , "Successfully logged in")
                menu()
                return None
        else:
              
            messagebox.showerror("Invalid Input" , "Invalid Input")
        
    root =Tk()
    root.title("login")
    root.geometry('925x500+300+200')
    root.configure(bg = bg_colour)
    root.resizable(False, False)

    #left_frame

    left_frame = Frame(root, width = 350, height = 470, bg = bg_colour)
    left_frame.place(x = 10, y = 10)
    Border_frame = Frame(root, width = 1, height = 320, bg = 'white')
    Border_frame.place(x = 370 , y = 30 )
    welcome_back = Label(left_frame , text = "Welcome Back" , bg = bg_colour , fg = txt_cover , font = ("Bebas Neue" , 35 , 'bold'))
    welcome_back.place(x = 50, y = 100)
    Startyourjourneytoday = Label(left_frame , text = "Best Toolbox ever 😅" , bg = bg_colour , fg = '#fff' , font = ("Microsoft YaHei UI light" , 15 ))
    Startyourjourneytoday.place(x = 70 , y = 160)
    #left_frame_ends

    #right_frame
    
    Right_frame = Frame(root, width = 500, height = 450, bg = bg_colour)
    Right_frame.place(x = 380, y = 10)
    login = Label(Right_frame , text = "Login" , bg = bg_colour , fg = txt_cover , font = ("Bebas Neue" , 38 ))
    login.place(x = 200 , y = 20 )

    #taking the enteries from the user
    #taking user name from the user
    
    user_name = Entry(Right_frame , width = 19 , border = 0 , fg = 'white' , bg = bg_colour , font = ("Microsoft YaHei UI light" , 12))
    user_name.place(x = 130 , y = 150)
    user_name.insert(0 , 'Enter User Name')
    frame_to_underline = Frame(Right_frame , width = 280 , height = 2, bg = 'white')
    frame_to_underline.place(x = 120 , y = 180)

    #taking the password
    password = Entry(Right_frame , width = 19 , border = 0 , fg = 'white' , bg = bg_colour , font = ("Microsoft YaHei UI light" , 12))
    password.place(x = 130 , y = 230)
    password.insert(0 , 'Enter password')
    frame_to_underline = Frame(Right_frame , width = 280 , height = 2, bg = 'white')
    frame_to_underline.place(x = 120 , y = 255)

    # login button

    login = Button(Right_frame , text = 'Login' , border = 0 ,  bg = txt_cover , fg = 'white' , activebackground = 'white' , padx = 100 , pady = 7 , font = ("Bhanschrift SemiBold" , 14 , 'bold') , command  = Checking_userInputs)
    login.place(x = 120 , y = 300)
    root.mainloop()


def menu():
    r1 = Tk()
    r1.geometry("900x540")
    r1['bg'] = '#242424' # for the window background
    r1.title("APPS")   
    l1 = Label(r1 , text = "Tools" , font = ("Bebas Neue" , 70 , "bold") , fg = "white" , bg = '#242424')
    l1.pack()
    button = { 
        'fg' : "black" ,  
        'activeforeground' : "black", 
        "activebackground" : "teal",
        "width"  : 20 , 
        "height" : 3 , 
        "bd"  : 5 , 
        "font" : ("Microsoft YaHei UI light" , 15 , "bold") , 
        "borderwidth" : 10 ,
        }
    b1 = Button(r1 ,text = "Notepad" , **button , command = Notepad)  # **button -  means using configurations from button dictionary
    b1.place(x = 500 , y = 150)
    b2 = Button(r1 ,text = "calc"  , **button , command = calc )
    b2.place(x = 200 , y = 150)
    b3  = Button(r1 , text = "Password Generator" , **button , command = password_generator_app )
    b3.place(x =200 , y = 290 )
    b4 = Button(r1 ,text = "Website searcher" , **button , command = website_Search_app )
    b4.place(x = 500 , y =290 )
    r1.mainloop()


    
#---------------------------------------------------------------------------------------------------------------------------------------------'

# CALCULATOR


def calc():
    root = Tk()
    root.title("Calculator")
    root['bg'] = '#EAF2F8' # color is Arial Blue
    number_entry = Entry(root , width = 20 ,  borderwidth= 10   ,font = ("Microsoft YaHei UI light",20 , "bold"),  relief=SUNKEN ) 
    number_entry.grid(row = 0 , column=0 , columnspan=3 , pady = 10)
    def inputt(n):                             # n = any button clicked from 1 to 10 or + , x , - , /
        current_number = number_entry.get()   #gets the current number from entry field (currently it is empty)
        number_entry.delete(0,END)            # clears entry field (it is empty for now)
        number_entry.insert(0 , str(current_number) + str(n))  # and then it inserts the current number and n 
                                                               # for now it ("" + 4 -> 4 will be displayed on entry field)
    def clear():
        number_entry.delete(0,END)
        
    def equal():                         
        expression = str(number_entry.get())  
        try:
            result = eval(expression)    # evaluating expression
            number_entry.delete(0, END)   # clears the expression
            number_entry.insert(0, result) # displays cleared expression
        except:
            number_entry.delete(0, END) 
            number_entry.insert(END, "Error" )  # if there is any error it will display "error" in entry field
            
        
        
        
    btn1 = Button(root , text = "1" ,  padx = 40 , pady = 20 , border=10  , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command = lambda : inputt(1)) #E8E8E8 is Plantinum
    
    btn2 = Button(root , text = "2" ,  padx = 40 , pady = 20 , border=10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command = lambda : inputt(2))
    btn3 = Button(root , text = "3" ,  padx = 40 , pady = 20 , border=10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(3))
    btn4 = Button(root , text = "4" ,  padx = 40 , pady = 20 , border=10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(4))
    btn5 = Button(root , text = "5" ,  padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(5))
    btn6 = Button(root , text = "6" ,  padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(6))
    btn7 = Button(root , text = "7" ,  padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command=lambda : inputt(7))
    btn8 = Button(root , text = "8" ,  padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda: inputt(8))
    btn9 = Button(root , text = "9" ,  padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(9))
    btn0 = Button(root , text = "0" , padx = 40 , pady = 20 , border = 10 , bg = "#E8E8E8",font = ("lucida" , 20 , "bold"),command= lambda : inputt(0))
    btn_add = Button(root , text = "+" , padx = 40 , pady = 20 , border=10 , bg="#2e95fd", fg = "white" ,  font = ("lucida" , 20 , "bold"), command=lambda:inputt('+'))
    btn_mult = Button(root , text = "x" , padx = 40 , pady = 20 , border=10 ,bg="#2e95fd", fg = "white"  ,font = ("lucida" , 20 , "bold"),command=lambda:inputt('*'))
    btn_sub = Button(root , text = "-" , padx = 40 , pady = 20 , border=10 ,bg="#2e95fd", fg = "white", font = ("lucida" , 20 , "bold"),command=lambda:inputt('-'))
    btn_div = Button(root , text = "/" , padx = 40 , pady = 20 , border=10 , bg="#2e95fd", fg = "white", font = ("lucida" , 20 , "bold"),command=lambda:inputt('/'))
    btn_clear = Button(root , text = "C" , padx = 40 , pady = 20 , border=10 ,bg="#2e95fd", fg = "white" ,font = ("lucida" , 20 , "bold"), command=clear)
    btn_equal = Button(root , text = "=" , padx = 180 , pady = 20 , border=10 , bg="#2e95fd", fg = "white" ,font = ("lucida" , 20 , "bold"),command=equal)
    btn1.grid(row=3 , column=0)
    btn2.grid(row=3 , column=1)
    btn3.grid(row=3 , column=2)
    btn4.grid(row=2 , column=0)
    btn5.grid(row=2 , column=1)
    btn6.grid(row=2 , column=2)
    btn7.grid(row=1 , column=0)
    btn8.grid(row =1, column=1)
    btn9.grid(row=1, column=2)
    btn0.grid(row= 4, column=1)
    btn_add.grid(row = 4 , column=0 )
    btn_sub.grid(row = 5 , column = 0)
    btn_mult.grid(row = 5 , column=1)
    btn_div.grid(row=5 , column=2)
    btn_clear.grid(row = 4 , column = 2)
    btn_equal.grid(row =6  ,columnspan= 4 )
    root.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------'
# NOTEPAD (Not with all functionalities)

def Notepad():
    def open_file():
        # asks the user to open files in reading mode for now user can open two file types .txt and .html
        file =askopenfile(mode = 'r' , filetypes=[('Text files' , ".txt") , ("HTML files" ,'.HTML' )]) 
        if file is not None:
            content = file.read()
            text.delete(1.0, END)  # Clear the existing text
        text.insert(END, content) # and will insert the new text
        file.close()
    def save_as():
        # asks the user to save file by default file will save as text file but user will get the option to save in 2 formats
        file = filedialog.asksaveasfile(defaultextension= ".txt" , filetype = [("text files" , ".txt"),
                                            ("HTML file" , ".html") ])
        filetext =str(text.get(1.0 , END)) 
        file.write(filetext)
        file.close()
        
    def red():
        text.config(bg = "red" , fg = "white")
    def violet():
        text.config(bg = "violet" ,fg = "black")
    def dark():
        text.config(bg = "black" , fg = "white")
    def light():
        text.config(bg = "cyan" ,fg= "black" )
    
    def hellp():
        window = Tk()
        window.title("Help")
        window.geometry("300x200")
        label = Label(window , text = 'This is a notepad\nis created by swastik , mayank and raghav\nyou can only open text file (.txt) and html files(.html)')
        label.pack()    
    root = Tk()
    root.geometry("900x900")
    root.title("Notepad")

    text = Text(root , font = ("Microsoft YaHei UI light" , 20 , "bold") , bg = "white" , fg = "black")
    text.pack()
    # Menu Bar or navigation bar
    navbar = Menu(root)
    file_m = Menu(navbar , tearoff = 0) # if tearoff is not 0 then it will show a line seprating two different commands in the cascade
    navbar.add_cascade(label = "File" , menu=file_m)
    file_m.add_command(label="Open" , command = open_file )
    file_m.add_command(label = "Save as" , command = save_as)
    file_m.add_separator()
    file_m.add_command(label = "QUIT" , command = quit)

    color= Menu(navbar , tearoff = 0 )
    navbar.add_cascade(label = "Background Color" , menu = color)
    color.add_command(label = "red" , command = red)
    color.add_command(label = "Dark" , command = dark)
    color.add_command(label = "cyan" , command= light)
    color.add_command(label = "Pink" , command = violet)

    helpp = Menu(navbar , tearoff = 0)
    navbar.add_cascade(label = "Help" , menu = helpp)
    helpp.add_command(label = "Help" , command = helpp)


    root.config(menu=navbar)
    root.mainloop()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Password Generator (Generates passwords from 91 characters including lowercase letters, uppercase letters ,digits  and special characters)


    
def password_generator_app():
        l = ['red' , 'green' , 'blue' , 'black' , 'brown']
        k = random.choice(l)  
        
        def generate_password(length):
            lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
            uppercase_letters = lowercase_letters.upper()
            digits = "0123456789"
            special_characters = "!@#$%^&*()_+~`|}{[]:;?><,./-="

            characters = lowercase_letters + uppercase_letters + digits + special_characters
            global password
            password = ''

            for i in range(length):
                a = random.randint(0, len(characters)-1)
                password += characters[a]

            return password

        def generate_password_gui():
            if length_entry.get() == "":
                messagebox.showerror("Error", "Please provide length")
                return
            length = int(length_entry.get())
            password = generate_password(length)
            password_label.config(text="Generated Password: " + password)
            #color will change after every run
            password_label.config(fg = k)
        def password_copy():
            root.clipboard_clear()
            root.clipboard_append(password)
            root.update()

        root = Tk() 
        root.title("Password Generator")
        root.geometry("600x600")

        length = Label(root, text="Password Length", fg="black", font=("comicsans", 18, 'bold'))
        length.place(x=10, y=90)
        length_entry = Entry(root, width=20, font=("Microsoft YaHei UI light", 20), bg="#6600ff", fg="white", bd=0, cursor="arrow")
        length_entry.place(x=250, y=90)

        gen_password = Button(root, text="Generate Password", bg="yellow", fg="black", command=generate_password_gui, width="30", height="3",
                            font=("Helvetica", 12, "bold"), bd=0, borderwidth=10)
        gen_password.place(x=130, y=150)

        copy_password = Button(root, text="Copy to Clipboard", bg="blue", fg="white", command=password_copy, width="30", height="3",
                            font=("Helvetica", 12, "bold"), bd=0, borderwidth=10)
        copy_password.place(x=130, y=400)

        password_label = Label(root, text="Generated Password:", font=("Microsoft YaHei UI light", 14, "bold"))
        password_label.place(x=10, y=350)

        root.mainloop()



            
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Website searcher
# User gives URL to search on browser (used browser : Google Chrome)

def website_Search_app():
    def search():
        url_to_search = url.get()
        webbrowser.register('chrome', None , webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open('https://www.google.com/search?q='+url_to_search)
        messagebox.showinfo("You searched" , url.get())


    root =Tk()
    root.title("Search here")
    root.geometry('925x500+300+200')
    root.configure(bg = '#fff')
    root.resizable(False, False)

    centre_frame = Frame(root, width = 550, height = 470, bg = 'white')
    centre_frame.place(x = 190, y = 10)
    welcome_back = Label(centre_frame , text = "Welcome Back" , bg = 'white' , fg = '#1a58ff' , font = ("Microsoft YaHei UI light" , 45 , 'bold'))
    welcome_back.place(x = 70 , y = 50)
    url = Entry(centre_frame , width = 25 , justify = CENTER ,  border = 0 , fg = 'black' , bg = 'white'  , font = ("Microsoft YaHei UI light" , 15))
    url.place(x = 145 , y = 180)
    url.insert(0 , 'Seach now!!')
    frame_to_underline = Frame(centre_frame , width = 280 , height = 2, bg = 'black')
    frame_to_underline.place(x = 145 , y = 210)

    searchbtn = Button(centre_frame , text = 'Search' , border = 0 ,  bg = '#1a58ff' , fg = 'white' , activebackground = 'white' , padx = 100 , pady = 7 , font = ("Bhanschrift SemiBold" , 14 , 'bold') , command = search )
    searchbtn.place(x = 140 , y = 300)
    
root =Tk()
root.title("login")
root.geometry('925x500+300+200')
root.configure(bg = bg_colour)
root.resizable(False, False)
centre_frame = Frame(root, width = 1100, height = 470, bg = bg_colour)
centre_frame.place(x = 10, y = 10)
welcome_back = Label(centre_frame , text = "Sign In" , bg = bg_colour , fg = txt_cover , font = ("Bebas Neue" , 48 , 'bold'))
welcome_back.place(x = 385, y = 10)
#taking user name from the user
username = Entry(centre_frame , width = 19 , border = 0 , fg = 'white' , bg = bg_colour , font = ("Microsoft YaHei UI light" , 12))
username.place(x = 365 , y = 150)
username.insert(0 , 'Enter User Name')
frame_to_underline = Frame(centre_frame , width = 280 , height = 2, bg = 'white')
frame_to_underline.place(x = 325 , y = 180)
    #taking the password
password = Entry(centre_frame , width = 19 , border = 0 , fg = 'white' , bg = bg_colour , font = ("Microsoft YaHei UI light" , 12))
password.place(x = 365 , y = 230)
password.insert(0 , 'Enter password')
frame_to_underline = Frame(centre_frame , width = 280 , height = 2, bg = 'white')
frame_to_underline.place(x = 325 , y = 255)
    # Sign_in button

Sign_in_btn = Button(centre_frame , text = 'Sign In' , border = 0 ,  bg = txt_cover , fg = 'white' , activebackground = 'white' , padx = 100 , pady = 7 , font = ("Bhanschrift SemiBold" , 14 , 'bold')  , command = register )
Sign_in_btn.place(x = 330 , y = 300)
        #login

For_login = Label(centre_frame , text = "Already have an Account?" , bg = bg_colour , fg = "white" , font = ("Bebas Neue" , 16))
For_login.place(x = 300, y = 380)
        #login_btn
login = Button(centre_frame , text = 'Login' , border = 0 ,  bg = bg_colour , fg = txt_cover , activebackground = 'white' , padx = 0 , pady = 0 , font = ("Bhanschrift SemiBold" , 14 , 'bold') , command = login)
login.place(x = 560 , y = 380)





root.mainloop()
