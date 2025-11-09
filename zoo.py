#ZOO MANAGEMENT SOFTWARE @cbsepython.in
#CREATING ZOO MANAGEMENT SOFTWARE 
print("""
                       =======================================
                        WELCOME TO ZOO MANAGEMENT SOFTWARE
                       =======================================
                        """)


#Creating database connectivity
import mysql.connector as mycon
username=input("Enter Usernname:")
passcode=input("Enter Password:")
data=mycon.connect(host="localhost",user="{}".format(username),passwd="{}".format(passcode))
mycursor=data.cursor()
if (data.is_connected()):
    print("Connection Established.")

#CREATING ZOO DATABASE
mycursor=data.cursor()
#mycursor.execute("CREATE DATABASE Zoo")
data.close()


#CREATING TABLE

import mysql.connector as mycon
data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
mycursor=data.cursor()
#mycursor.execute("CREATE TABLE Zoo_info(Name char(30),Age int(3) NOT NULL,Gender char(20) NOT NULL,Category varchar(20) NOT NULL,Number int(5) NOT NULL)" )
data.close()


#here in this function the 'additon' of records of 'Animals' takes place 
def addition_of_records_of_animals():
     import mysql.connector as mycon
     data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
     mycursor=data.cursor()
     ch=int(input("Number of Records :"))
     A=1
     while A<=ch:
          n=input("Enter Name:")
          a=int(input("Enter Age:"))
          g=input("Enter Gender:")
          c=input("Enter Category:")
          no=int(input("Enter Number:"))
          mycursor.execute("INSERT INTO Zoo_info VALUES('{}',{},'{}','{}',{})".format(n,a,g,c,no))
          data.commit()
          print("Inserted")
          A+=1
     data.close()

#here in this function the 'updation' of records of 'Animals' takes place 
def updating_through_name():
     import mysql.connector as mycon
     data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
     mycursor=data.cursor()
     ch=int(input("Enter Number of Records you want to change:"))
     A=1
     while A<=ch:
          n=input("Enter Name:")
          a=int(input("Enter Age:"))
          no=int(input("Enter Number:"))
          mycursor.execute("UPDATE Zoo_info SET Age={},Number={} WHERE Name='{}'".format(a,no,n))
          data.commit()
          print("Updated")
          A+=1
          data.close()

#here in this function the records of 'Animals' are 'displayed' takes place 
def Displaying_record_of_animals():
     import mysql.connector as mycon
     data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
     mycursor=data.cursor()
     mycursor.execute("SELECT * FROM Zoo_info")
     x=mycursor.fetchall()
     for i in x:
          print(i)
     print("Displayed")
     data.close()

#here in this function the 'Deletion' of records of 'Animals' takes place
def deleting_records_of_animals():
     import mysql.connector as mycon
     data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
     mycursor=data.cursor()
     ch=int(input("Enter Number of Animal Records You want to DELETE:"))
     A=1
     while A<=ch:
          USER=input("Enter Name of Animal:")
          mycursor.execute("DELETE FROM Zoo_info WHERE Name='{}'".format(USER))
          data.commit()
          print("Deleted")
          A+=1
     data.close()

#here in this function the 'searching' of records of 'Animals' takes place
def searching_any_particular_record():
     import mysql.connector
     from mysql.connector import Error

     try:
          connection = mysql.connector.connect(host='localhost',
                                         database='Zoo',
                                         user='root',
                                         password='root')
          if connection.is_connected():
               db_info = connection.get_server_info()
               print(f"Connected to Mysql server version: {db_info}")
               cursor = connection.cursor()
               n=input('Enter Animal Name : ')
               select_query = f"select * from Zoo_info where name = '{n}';"
               cursor.execute(select_query)

               record = cursor.fetchall()
               for item in record:
                    print(item)

     except Error as e:
          print("Error While connecting to mysql is: ", e)

     finally:
          if connection.is_connected():
               cursor.close()
               connection.close()
               print("Mysql connection is closed ")

           
#here in this function the exiting of zoo management software takes place
def exiting_the_program():
     import mysql.connector as mycon
     data=mycon.connect(host="localhost",user="root",passwd="root",database="Zoo")
     mycursor=data.cursor()
     data.close()
     exit()
     print("Exited")
     
ch='y'
while ch=='y':
     print("Press 1 to Add records of Animal")
     print("Press 2 to Update records of Animal")
     print("Press 3 to Display records of Animal")
     print("Press 4 to Delete records of Animal")
     print("Press 5 to Search record of Animal")
     print("Press 6 to Exit")
     userchoice=int(input('Enter Desired Choice from Menu:'))
     if userchoice==1:
          addition_of_records_of_animals()
     elif userchoice==2:
           updating_through_name()
     elif userchoice==3:
          Displaying_record_of_animals()
     elif userchoice==4:
                   deleting_records_of_animals()
     elif userchoice==5:
          searching_any_particular_record()
     elif  userchoice==6:
          exiting_the_program()
     else:
          print('Wrong Choice!')
     ch=input('Press y to continue using Zoo Management Software:')    

       
          
          
          
     
     
     
     

     



