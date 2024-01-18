import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="project",charset="utf8")
mycursor=mydb.cursor()

def stuInsert():
    L=[]
    rollno=int(input("Enter the roll number : "))
    L.append(rollno)
    name=input("Enter the Name: ")
    L.append(name)
    dob=input("Enter the date of birth of student(dd-mm-yyyy):")
    L.append(dob)
    address=input("Enter the address:")
    L.append(address)
    marks=int(input("Enter the marks:"))
    L.append(marks)				
    stud=(L)
    sql="insert into stud (rollno,name,dob,address,marks) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    print("Student details inserted")

def stuview():
    mycursor.execute("select * from stud")
    myrus=mycursor.fetchall()
    print("Rollno\t\tName\t\tDate of Birth\t\tAddress\t\tMarks")
    for x in myrus:
        for i in x:
            print(i,end='\t\t')
        print()

def removeStu():
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from stud where rollno=%s"
    mycursor.execute(sql,rl)
    print('Record deleted!!!')
    mydb.commit()

def stusearch():
    print("Select the search criteria : ")
    print("1. Roll")
    print("2. Name")
    print("3. DOB")
    print("4. Address")
    print("5. Marks")
    print("6. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll no : "))
        rl=(s,)
        sql="select * from stud where rollno=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from stud where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=input("Enter DOB : ")
        rl=(s,)
        sql="select * from stud where dob=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter Address : ")
        rl=(s,)
        sql="select * from stud where address=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        s=int(input("Enter Marks : "))
        rl=(s,)
        sql="select * from stud where marks=%s"
        mycursor.execute(sql,rl)
    elif ch==6:
        sql="select * from stud"
        mycursor.execute(sql)
        
    res=mycursor.fetchall()
    print("The Students details are as follows : ")

    print("Roll no\t\tName\t\tDate of Birth\t\tAddress\t\tMarks")
    for x in res:
        for i in x:
            print(i,end='\t\t')
        print()

def MenuSet():
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Students")
    print("Enter 3 : To Search Student")
    print("Enter 4 : To Remove Student")

    userInput = int(input("Please Select An Above Option: "))
    if(userInput == 1):
        stuInsert()
    elif(userInput == 2):
        stuview()
    elif(userInput == 3):
        stusearch()
    elif(userInput == 4):
        removeStu()
    else:
        print('Invalid input !!!')

MenuSet()

def runAgain():
    runAgn = input("\nWant To Run Again? Y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            os.system('cls')
        else:
            os.system('clear')    
        MenuSet()
        runAgn = input("\nwant To Run Again? y/n: ")
    else:
        if runAgn.lower()=='n':
            print("Thank you")
        else:
            print("Invalid input")
runAgain()
