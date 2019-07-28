import mysql.connector

myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print(myconn)

mycursor = myconn.cursor()

mycursor.execute("CREATE DATABASE mysql_test")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.close()
myconn.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mysql_test"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

mycursor.execute("ALTER TABLE users ADD COLUMN dob VARCHAR")

sql = "INSERT INTO users (name, age,dob) VALUES (%s, %i, %s)"
val = ("Nagaraju",23, "01-06-1996")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("1 record inserted, ID:", mycursor.lastrowid)

val1 = [
  ('Peter',24, '01-06-1995'),
  ('Amy',25, '01-06-1994')
  ]
mycursor.executemany(sql, val1)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchone()
print(myresult)

sql = "UPDATE users SET age = %i WHERE name = %s "
val = (24,'Peter' )
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

sql = "DELETE FROM users WHERE name = 'Amy'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
