#firstly, you need to install the library of the python sql connector. 
import mysql.connector
#here you put all the info like ip address and name of the database 
#it is important to make sure that the DB user has a full access so you can use it to retrieve the data. 
#in host part , here i have used the local ip but in case of the newtwork add the Ip Address of Raspberry from the router. 
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="mahmoud",
  passwd="password",
  database="conti"
)

mycursor = mydb.cursor()

#here you can write my sql queries and specifiy the data which you want. 
#in my case was a testing data for Vehicles. 
mycursor.execute("SELECT test_manager , project , software_version FROM test WHERE bench_number=1 ")
#here you fetch the data which you specified. 
myresult = mycursor.fetchall()
#here you need a loop to output all the letters or the data letters fro the sql tables. 
for x in myresult:
  print(x)
#another query to another DB accessable with the same User. 
mycursor.execute("SELECT name FROM contidb WHERE ID= 1 ")
#here to fetch specified data and output all data via a for loop.   
myresult1 = mycursor.fetchall()
#for loop to retrieve the data. 
for x in myresult1:
  print(x)
#for GUI you can use a Tkinter Lib in python to have an interface. 
