import mysql.connector
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Newmysql_1',
    database = "Test1"
)
my_cursor = db.cursor()
my_cursor.execute("CREATE TABLE Testing (name VARCHAR(50), age int)")
names = ["Brad", "James", "Ellie", "Margo", "Abe", "Rachel"]
query = "INSERT INTO testing (name, age) VALUES (%s,%s)"
count = 1
for name in names:
    my_cursor.execute(query, (name,count))
    count += 1
db.commit()
my_cursor.execute("SELECT * FROM Testing")
for x in my_cursor:
    print(x)
my_cursor.execute("DROP TABLE Testing")