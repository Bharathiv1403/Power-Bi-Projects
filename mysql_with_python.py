from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Bhar2002',database='python_db')

# if con:
#     print("connected")

# else:
#     print("error")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users (name, age, city) values (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data insert success")

def update(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s, age=%s, city=%s where id=%s"
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("Data update success")

def select():
    res=con.cursor()
    sql="SELECT ID, NAME, AGE, CITY from users"
    res.execute(sql)
    result=res.fetchall()
    # result=res.fetchone()
    # result=res.fetchmany(2)
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("Data Delete success")

while True:
    print('1. Insert Data')
    print('2. Update Data')
    print('3. Select Data')
    print('4. Delete Data')
    print('5. Exit')

    u_choice=int(input("Enter Your Choice : "))

    if u_choice==1:
        name=input("Enter the Name : ")
        age=input("Enter the Age : ")
        city=input("Enter your City : ")
        insert (name,age,city)

    elif u_choice==2:
        id=input('Enter the ID :')
        name=input('Enter the Name :')
        age=input("Enter the Age : ")
        city=input('Enter your City :')
        update (name,age,city,id)

    elif u_choice==3:
        select()

    elif u_choice==4:
        id=input("Enter the ID Delete :")
        delete(id)

    elif u_choice==5:
        quit()

    else:
        print("Select correct choice, Plase try again")