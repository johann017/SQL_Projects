import tkinter as tk
import mysql.connector

#This function effectively "clears" the original screen to
#allow the sign in/sign up page to be displayed
def forget():
    for i in range(3):
        for j in range(3):
            new_frame.pack_forget()
    sign_up.pack_forget()
    sign_in.pack_forget()

#This function creates the sign up page
def sign_up_func(event):
    
    #Variables to be used
    global name_var
    global user_var
    global password_var
    
    #Clears the screen
    forget()
    
    #This function handles the even where the submit button is pressed
    #It checks if the name, username or the password have any common
    #SQL commands. If it does, it clears the inputted values and displays
    #a message. If it doesn't, it will add the name, username and password
    #to a SQL table.
    def sign_up_submit(event):
        name = name_var.get()
        username = user_var.get()
        password = password_var.get()
        check = True
        for i in bad_input:
            if name == i or username == i or password == i:
                check = False
        if check:
            label_name4.pack_forget()
            query = "INSERT INTO Users (name,user,pass) VALUES (%s,%s,%s)"
            my_cursor.execute(query,(name,username,password))
            db.commit()
            name_var.set("")
            user_var.set("")
            password_var.set("")
        else:
            label_name4.pack()
            name_entry.delete(0,'end')
            username_entry.delete(0,'end')
            password_entry.delete(0,'end')
            
    #Draws the sign up page and the labels to be displayed based on input
    for i in range(5):
        window.columnconfigure(i,weight = 5,minsize=75)
        window.rowconfigure(i,weight = 5,minsize=50)
        for j in range(3):
            new_frame = tk.Frame(master=window, bg="Light Blue")
            new_frame.grid(row = i, column=j, padx=5, pady=5)
            
            #Name box
            if i == 0 and j == 2:
                label_name = tk.Label(master= new_frame, text="Name: ")
                label_name.pack(side="top")
                name_entry = tk.Entry(master= new_frame,textvariable = name_var, font=('calibre',10,'normal'))
                name_entry.pack()
                
            #Username box
            if i == 1 and j == 2:
                label_name2 = tk.Label(master= new_frame, text="Username: ")
                label_name2.pack(side="top")
                username_entry = tk.Entry(master= new_frame,textvariable = user_var, font=('calibre',10,'normal'))
                username_entry.pack()
                
            #Password box
            if i == 2 and j == 2:
                label_name3 = tk.Label(master= new_frame, text="Password: ")
                label_name3.pack(side="top")
                password_entry = tk.Entry(master= new_frame,textvariable = password_var, font=('calibre',10,'normal'))
                password_entry.pack()
                
            #Label in case the user inputted any common SQL commands
            if i == 3 and j == 2:
                label_name4 = tk.Label(master= new_frame, text="Bad Input. Please Retry.")
                label_name4.pack(side="top")
                label_name4.pack_forget()
                
            #Submit button
            if i == 4 and j == 2:
                submit = tk.Button(master=new_frame, width=10, height=2,text="Submit")
                submit.bind("<Button-1>", sign_up_submit)
                submit.pack()

#This function handles the event the user clicks the sign in button
def sign_in_func(event):
    
    #Clears the screen
    forget()
    
    #This function handles the even a user clicks the submit button.
    #It checks if the username and the password have any common
    #SQL commands. If it does, it clears the inputted values and displays
    #a message. If it doesn't, it will check if the username and passwords 
    #is in the table of usernames and passwords and displays a message accordingly 
    def sign_in_submit(event):
        
        #Variables to be used
        global username
        global password
        username = user_var.get()
        password = password_var.get()
        name_var.set("")
        user_var.set("")
        password_var.set("")
        check = True
        for i in bad_input:
            if username == i or password == i:
                check = False
        if check:
            if username != None and password != None and sign_in_helper(username,password) == False:
                label_name3.pack_forget()
                label_name4.pack()
            else:
                label_name4.pack_forget()
                label_name3.pack()
        else:
            label_name3.pack_forget()
            label_name4.pack()
            
    #This function handles the event a user clicks the clear button.
    #This will clear the username and password fields.
    def sign_in_clear(event):
        username_entry.delete(0,'end')
        password_entry.delete(0,'end')
        label_name3.pack_forget()
        label_name4.pack_forget()
        
    #Draws the sign in page
    for i in range(5):
        window.columnconfigure(i,weight = 5,minsize=75)
        window.rowconfigure(i,weight = 5,minsize=50)
        for j in range(3):
            new_frame = tk.Frame(master=window, bg="Light Blue")
            new_frame.grid(row = i, column=j, padx=5, pady=5)
            
            #Username box
            if i == 0 and j == 2:
                label_name = tk.Label(master= new_frame, text="Username: ")
                label_name.pack(side="top")
                username_entry = tk.Entry(master= new_frame,textvariable = user_var, font=('calibre',10,'normal'))
                username_entry.pack()
            
            #Password box
            if i == 1 and j == 2:
                label_name2 = tk.Label(master= new_frame, text="Password: ")
                label_name2.pack(side="top")
                password_entry = tk.Entry(master= new_frame,textvariable = password_var, font=('calibre',10,'normal'))
                password_entry.pack()
            
            #Messages based on if user input was correct
            if i == 3 and j == 2:
                label_name3 = tk.Label(master= new_frame, text="Successfully Logged In!!")
                label_name3.pack(side="top")
                label_name3.pack_forget()
                label_name4 = tk.Label(master= new_frame, text="Incorrect username or password")
                label_name4.pack(side="top")
                label_name4.pack_forget()
                
            #Submit and clear buttons
            if i == 4 and j == 2:
                submit = tk.Button(master=new_frame, width=10, height=2,text="Submit")
                submit.bind("<Button-1>", sign_in_submit)
                submit.pack(side = "left", padx=5, pady=5)
                clear = tk.Button(master=new_frame, width=10, height=2,text="Clear")
                clear.bind("<Button-1>", sign_in_clear)
                clear.pack(side = "left", padx=5, pady=5)

#This function does the checking if the inputted username and
#password are in the table and are correct
def sign_in_helper(u,p):
    my_cursor.execute("SELECT user,pass FROM Users")
    for x,y in my_cursor:
        if x==u and y==p:
            return True
    return False

#######################################################################################################################################

#Array or common and possibly malicious SQL commands
bad_input = ["DROP", "DELETE", "--", "UPDATE", "AND", "OR", "=", ">", "<", "FROM"]

#Connects to the database
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Newmysql_1',
    database = 'LogIn'
)
my_cursor = db.cursor(buffered=True)

#Draws the original page with the sign in and sign up button
window = tk.Tk()
window.configure(bg="Light Blue")

#Creates the variables to be used later on
name_var = tk.StringVar()
user_var = tk.StringVar()
password_var = tk.StringVar()
username = None
password = None
for i in range(3):
    window.columnconfigure(i,weight = 5,minsize=75)
    window.rowconfigure(i,weight = 5,minsize=50)
    for j in range(3):
        new_frame = tk.Frame(master=window, bg="Light Blue")
        new_frame.grid(row = i, column=j, padx=5, pady=5)
        
        #Creates the sign up and sign in button
        if i == 1 and j == 1:
            sign_up = tk.Button(master=new_frame, width=10, height=2,text="Sign Up")
            sign_up.bind("<Button-1>", sign_up_func)
            sign_up.pack(padx=5, pady=5)
            sign_in = tk.Button(master=new_frame, width=10, height=2,text="Sign In")
            sign_in.bind("<Button-1>", sign_in_func)
            sign_in.pack(padx=5, pady=5)
window.mainloop()

