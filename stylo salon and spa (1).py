import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database stylo")

#table 1 : employe

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor
mycursor.execute("create table employee(employee_id int(8),name varchar(50),phone_no. int (12) ,salary int(10),address varchar(100))")

# table 2 : client profile

import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table client_profile(name varchar(50),phone_no. int(12),treatment varchar (50),amount int(10)")

#table 3 : packages 

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor
mycursor.execute("create table packages(s.no int(10),package _name varchar(50),amount int(10)")

#table 4 : appointments

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor
mycursor.execute("create table appointments(name varchar(50),phone_no. int(12), scheduled_date varchar(50),time int(10) ")

# table 5 : products for sale

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor
mycursor.execute("create table products_for_sale(product_name varchar(50),quantity int(10),amount int(50),expiry_date varchar(10)) ")

a='b'
while(a=='b'):
 print('1.employee')
 print('2.client profile')
 print('3.packages')
 print('4.appointments')
 print('5.product for sale')
 print('6.exit')

 sel=int(input('enter the number:'))
 if sel==1:
     def emp():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.modify')
      print('5.delete')
      print('6.main menu')
      c=int(input("enter any number"))
      if c==1:
          addemp()
      if c==2:
          upemp()
      if c==3:
          disemp()
      if c==4:
          modemp()
      if c==5:
          delemp()
      else :
          print('returning to main menu')
          break   
     def addemp():
        import mysql.connector
        try:
          mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
          mycursor=mydb.cursor()
          id=int(input('enter employee_id'))
          name=input('enter employee name')
          no=int(input('enter phone no.'))
          salary=int(input('enter salary'))
          address=input('enter address')
          mycursor.execute("""insert into employee(employee_id,name,phone_no.,salary,address)values(%s,%s,%s,%s,%s)""",(id,name,no,salary,address))
          mydb.commit()
          print("record inserted")
        except:     
           print("unable to add record,plz try again")
     def upemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         u=input("enter sql command to update")
         mycursor.execute(u)
         mydb.commit()
         print("record updated")
        except: 
         print("unable to update record,plz try again")
     def disemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         d=input ("enter sql command for displaying record")
         mycursor.execute(d)
         results=cursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
         print("unable to display, plz try again")
     def modemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         m=input("enter sql command")
         mycursor.execute(m)
         mydb.commit()
         print("record modified")
        except:
            print ("unable to modify,plz try again")
     def delemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         e=input("enter sql command")
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
     emp()
 if sel==2:
     def cp():
       print('1.add')
       print('2.update')
       print('3.display')
       print('4.modify')
       print('5.delete')
       print('6.main menu')
       f=int(input("enter any number"))
       if f==1:
           addcp()
       if f==2:
           upcp()
       if f==3:
           discp()
       if f==4:
           modcp()
       if f==5:
           delcp()
       else:
           print('returning to the main menu')
           break
     def addcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input("enter name of client")
         no=int(input("enter phone number of client"))
         treatmentnt=input("enter treatment of client")
         amount=int(input("enter amount of treatment"))
         mycursor.execute("""insert into client_profile(name,phone_no.,treatment,amount)values(%s,%s,%s,%s)""",(name,no,treatment,amount))
         mydb.commit()
         print("record inserted")
        except:
            print("unable to add record,plz try again")
     def upcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         u=input("enter sql command for update")
         mycursor.execute(u)
         mydb.commit()
         print("record updated")
        except:
            print("unable to update record,plz try again")
     def discp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         d=input("enter sql command for display")
         mycursor.execute(d)
         results=cursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
            print("unable to display,plz try again")
     def modcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         m=input("enter sql command")
         mycursor.execute(m)
         mydb.commit()
         print("record updated")
        except:
            print("unable to modify,plz try again")
     def delcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb,cursor()
         e=input("enter sql command")
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
     cp()
 if sel==3:
     def pak():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.modify')
      print('5.delete')
      print('6.main menu')
      g=int(input("enter number"))
      if g==1:
          addpak()  
      if g==2:
          uppak()
      if g==3:
          dispak()
      if g==4:
          modpak()
      if g==5:
          delpak()
      else:
          print('returning to main menu')
          break  
     def addpak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         no=int(input('enter s.no'))
         name=input('enter package name')
         amount=int(input('enter amount'))
         mycursor.execute("""insert into packages(s.no,package_name,amount)values(%s,%s,%s)"""(no,name,amount))
         mydb.commit()
         print('record inserted')
        except:
            print('unable to insert record,plz try again')
     def uppak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         u=input("enter sql command for update")
         mycursor.execute(u)
         print('record updated')
         mydb.commit()
        except:
            print('unable to update error,plz try again')
     def dispak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         d=input('enter sql command to display')
         mycursor.execute(d)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
         mydb.commit()
        except:
            print('unable tyo display,plz try again')
     def modpak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         m=input('enter sql command to modify')
         mycursor.execute(m) 
         print('record modified')
         mydb.commit()
        except:
            print('unable to modify,plz try again')
     def delpak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         e=input('enter sql command for delete')
         mycursor.execute(e)
         print('record deleted')
         mydb.commit()
        except:
            print('unable to delete,plz try again')
     pak()
 if sel==4:
     def app():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.modify')
      print('5.delete')
      print('6.main menu')
      h=int(input('enter number'))
      if h==1:
          addapp()
      if h==2:
          upapp()
      if h==3:
          disapp()
      if h==4:
          modapp()
      if h==5:
          delapp()
      else:
          print('returning to the main menu')
          break
     def addapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input('enter name of client')
         no=int(input('enter phone no.'))
         date=input('enter scheduled date')
         time=int(input('enter time'))
         mycursor.execute("""insert into appointments(name,phone_no.,scheduled_date,time)values(%s,%s,%s,%s)""",(name,no,date,time))
         print('record inserted')
         mydb.commit()
        except:
            print('unable to insert record,plz try again')
     def upapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         u=input('enter sql command to display')
         mycursor.execute(u)
         print('record updated')
         mydb.commit()
        except:
            print('unable to update,plz try again')
     def disapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         d=input('enter sql command to display')
         mycursor.execute(d)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
        except:
            print('unable to display,plz try again')
     def modapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         m=input('enter sql command to modify')
         mycursor.execute(m)
         print('record modified')
         mydb.commit()
        except:
            print('unable to modify,plz try again')
     def delapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         e=input('enter sql command to delete')
         mycursor.execute(e)
         mydb.commit()
         print('record deleted')
        except:
            print('unable to delete,plz try again')
     app()
 if sel==5:
     def prod():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.modify')
      print('5.delete')
      print('6.main menu')
      i=int(input('enter number'))
      if i==1:
          addprod()
      if i==2:
          upprod()
      if i==3:
          disprod()
      if i==4: 
          modprod()
      if i==5:
          delprod()
      else:
          print('returning to the main menu')
          break
     def addprod():     
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input('enter product name')
         quantity=int(input('enter quantity'))
         amount=int(input('enter amount'))
         date=input('enter expiry date')
         mycursor.execute("""insert into product_for_sale(product_name,quantity,amount,expiry_date)values(%s,%s,%s,%s)""",(name,quantity,amount,date))
         mydb.commit()
         print('record inserted')
        except:
            print('unable to record,plz try again')
     def upprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         u=inpur('enter sql command for update')
         mycursor.execute(u)
         mydb.commit()
         print('record updated')
        except:
            print('unable to update record,plz try again')
     def disprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         d=input('enter sql command for display')
         mycursor.execute(d)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
        except:
            print('unable to display,plz try again')
     def modprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         m=input('enter sql command to modify')
         mycursor.execute(m)
         print('record modified')
        except:
            print('unable to modify,plz try again')
     def delprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mcursor=mydb.cursor()
         e=input('enter sql command to delete')
         mycursor.execute(e)
         print('record deleted')
        except:
            print('unable to delete recod,plz try again')
     prod()
 if sel==6:
     exit()