import mysql.connector

def sign_in():
    u = input("Username: ")
    p = input("Password: ")
    my_cursor.execute("SELECT user,pass FROM Users")
    for x,y in my_cursor:
        if x==u and y==p:
            print("Successfully Logged In!!")
            return True
    print("Incorrect username or password")
    return False

def sign_up():
    query = "INSERT INTO Users (name,user,pass) VALUES (%s,%s,%s)"
    n = input("Name: ")
    u = input("Username: ")
    p = input("Password: ")
    my_cursor.execute(query,(n,u,p))
    db.commit()

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Newmysql_1',
    database = "LogIn"
)
my_cursor = db.cursor(buffered=True)
#my_cursor.execute("CREATE TABLE Users(ID int NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), user VARCHAR(50), pass VARCHAR(50), time TIMESTAMP NOT NULL DEFAULT NOW())")
option = input("Sign in or Sign Up: ")
while not((option == "Sign in") or (option == "Sign Up")):
    option = input("Sign in or Sign Up: ")
valid = False
if option == "Sign Up":
    sign_up()
if option == "Sign in":
    for i in range(3):
        if not valid:
            valid = sign_in()
my_cursor.execute("SELECT * FROM Users")
for x in my_cursor:
    print(x)
#my_cursor.execute("DROP TABLE Users")