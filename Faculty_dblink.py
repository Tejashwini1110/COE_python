#creating table
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE products (product_id INT PRIMARY KEY,product_name VARCHAR(100),category VARCHAR(50),price DECIMAL(10, 2),stock_quantity INT)")
mydb.commit()

#inserting values into table
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
product_id=input("Enter product id:")
product_name = input("Enter product name: ")
category = input("Enter product category: ")
price = float(input("Enter product price: "))
stock_quantity = int(input("Enter stock quantity: "))
sql = "INSERT INTO products (product_id,product_name, category, price, stock_quantity) VALUES (%s,%s, %s, %s, %s)"
values = (product_id,product_name, category, price, stock_quantity)
mycursor.execute(sql, values)
mydb.commit()

#deleting a row based on id
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
id=input("Enter product id:")
mycursor.execute("delete from products where product_id=%s",(product_id,))
mydb.commit()

#updating product name based on product id
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
name=input("Enter product name to be changed:")
id=input("Enter product id:")
mycursor.execute("update products set product_name=%s where product_id=%s",(name,id))
mydb.commit()

#display all
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
mycursor.execute("select *from products")
prod=mycursor.fetchall()
for p in prod:
    print(p)

#display all in asc order
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
mycursor.execute("select *from products order by price")
prod=mycursor.fetchall()
for p in prod:
    print(p)

 #display products whose price between 0 and 1000
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
mycursor.execute("select *from products where price between 500 and 1000")
prod=mycursor.fetchall()
for p in prod:
   print(p)

#display products based on category
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="1234", database="retail")
mycursor = mydb.cursor()
cat=input("Enter category:")
mycursor.execute("select *from products where category=%s",(cat,))
prod=mycursor.fetchall()
for p in prod:
    print(p)