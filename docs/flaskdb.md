# Python with database[MYSQL]. 

We have seen how to write flask applications that can serve basic requests. The next thing that we need to learn is how to save states in application. Till now we have only seen stateless applications. 

We will have a look at how we can connect to mysql using python mysql connectors.

<pre>

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
</pre>

This will print the connection that is created. 

Let try and create a table and insert some values in it. 

<pre>
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="testapp"
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
</pre>

The above code will create table customers in testapp database. 

Lets insert values in this database.

<pre>
import mysql.connector
  
mydb = mysql.connector.connect(
  host="localhost",
  user="chowmean",
  passwd="chowmean",
  database="testapp"
)

print(mydb)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
</pre>

This will insert a row in table. 

Lets see how we can see the entry that is created right now. 

<pre>
import mysql.connector
  
mydb = mysql.connector.connect(
  host="localhost",
  user="chowmean",
  passwd="chowmean",
  database="testapp"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
</pre>

This will print the data that is extracted from mysql.