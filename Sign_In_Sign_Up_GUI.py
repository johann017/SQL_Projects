import tkinter as tk
import mysql.connector

def forget():
    for i in range(3):
        for j in range(3):
            new_frame.pack_forget()
    sign_up.pack_forget()
    sign_in.pack_forget()

def sign_up_func(event):
    global name_var
    global user_var
    global password_var
    forget()
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
    for i in range(5):
        window.columnconfigure(i,weight = 5,minsize=75)
        window.rowconfigure(i,weight = 5,minsize=50)
        for j in range(3):
            new_frame = tk.Frame(master=window, bg="Light Blue")
            new_frame.grid(row = i, column=j, padx=5, pady=5)
            if i == 0 and j == 2:
                label_name = tk.Label(master= new_frame, text="Name: ")
                label_name.pack(side="top")
                name_entry = tk.Entry(master= new_frame,textvariable = name_var, font=('calibre',10,'normal'))
                name_entry.pack()
            if i == 1 and j == 2:
                label_name2 = tk.Label(master= new_frame, text="Username: ")
                label_name2.pack(side="top")
                username_entry = tk.Entry(master= new_frame,textvariable = user_var, font=('calibre',10,'normal'))
                username_entry.pack()
            if i == 2 and j == 2:
                label_name3 = tk.Label(master= new_frame, text="Password: ")
                label_name3.pack(side="top")
                password_entry = tk.Entry(master= new_frame,textvariable = password_var, font=('calibre',10,'normal'))
                password_entry.pack()
            if i == 3 and j == 2:
                label_name4 = tk.Label(master= new_frame, text="Bad Input. Please Retry.")
                label_name4.pack(side="top")
                label_name4.pack_forget()
            if i == 4 and j == 2:
                submit = tk.Button(master=new_frame, width=10, height=2,text="Submit")
                submit.bind("<Button-1>", sign_up_submit)
                submit.pack()

def sign_in_func(event):
    forget()
    def sign_in_submit(event):
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
    def sign_in_clear(event):
        username_entry.delete(0,'end')
        password_entry.delete(0,'end')
        label_name3.pack_forget()
        label_name4.pack_forget()
    for i in range(5):
        window.columnconfigure(i,weight = 5,minsize=75)
        window.rowconfigure(i,weight = 5,minsize=50)
        for j in range(3):
            new_frame = tk.Frame(master=window, bg="Light Blue")
            new_frame.grid(row = i, column=j, padx=5, pady=5)
            if i == 0 and j == 2:
                label_name = tk.Label(master= new_frame, text="Username: ")
                label_name.pack(side="top")
                username_entry = tk.Entry(master= new_frame,textvariable = user_var, font=('calibre',10,'normal'))
                username_entry.pack()
            if i == 1 and j == 2:
                label_name2 = tk.Label(master= new_frame, text="Password: ")
                label_name2.pack(side="top")
                password_entry = tk.Entry(master= new_frame,textvariable = password_var, font=('calibre',10,'normal'))
                password_entry.pack()
            if i == 3 and j == 2:
                label_name3 = tk.Label(master= new_frame, text="Successfully Logged In!!")
                label_name3.pack(side="top")
                label_name3.pack_forget()
                label_name4 = tk.Label(master= new_frame, text="Incorrect username or password")
                label_name4.pack(side="top")
                label_name4.pack_forget()
            if i == 4 and j == 2:
                submit = tk.Button(master=new_frame, width=10, height=2,text="Submit")
                submit.bind("<Button-1>", sign_in_submit)
                submit.pack(side = "left", padx=5, pady=5)
                clear = tk.Button(master=new_frame, width=10, height=2,text="Clear")
                clear.bind("<Button-1>", sign_in_clear)
                clear.pack(side = "left", padx=5, pady=5)

def sign_in_helper(u,p):
    my_cursor.execute("SELECT user,pass FROM Users")
    for x,y in my_cursor:
        if x==u and y==p:
            return True
    return False

bad_input = ["DROP", "DELETE", "--", "UPDATE", "AND", "OR", "=", ">", "<", "FROM"]
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Newmysql_1',
    database = 'LogIn'
)
my_cursor = db.cursor(buffered=True)
window = tk.Tk()
window.configure(bg="Light Blue")
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
        if i == 1 and j == 1:
            sign_up = tk.Button(master=new_frame, width=10, height=2,text="Sign Up")
            sign_up.bind("<Button-1>", sign_up_func)
            sign_up.pack(padx=5, pady=5)
            sign_in = tk.Button(master=new_frame, width=10, height=2,text="Sign In")
            sign_in.bind("<Button-1>", sign_in_func)
            sign_in.pack(padx=5, pady=5)
window.mainloop()

