import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="mahmoud",
  passwd="01140422762",
  database="conti"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT name FROM contidb WHERE ID= 1 ")
mycursor.execute("SELECT test_manager , project , software_version FROM test WHERE bench_number=1 ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT name FROM contidb WHERE ID= 1 ")
  
myresult1 = mycursor.fetchall()
for x in myresult1:
  print(x)
