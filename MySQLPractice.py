import mysql.connector

#Connects to the the database in MySQL
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Newmysql_1',
    database = "Test1"
)
my_cursor = db.cursor()

#Creates a new table called Testing with a name column and an age column
my_cursor.execute("CREATE TABLE Testing (name VARCHAR(50), age int)")

#Array of names to be added to the table
names = ["Brad", "James", "Ellie", "Margo", "Abe", "Rachel"]

#Creates a query without arguments to be used
query = "INSERT INTO testing (name, age) VALUES (%s,%s)"
count = 1

#Goes through the array of names to be added and inserts each name and age
#into the table
for name in names:
    my_cursor.execute(query, (name,count))
    count += 1

#Commits the changes to the database
db.commit()

#Prints all elements in the table to show elements were added
my_cursor.execute("SELECT * FROM Testing")
for x in my_cursor:
    print(x)
   
#Deletes the table so next execution of this code wont have a table
my_cursor.execute("DROP TABLE Testing")
