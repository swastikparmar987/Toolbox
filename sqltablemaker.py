import mysql.connector as mysql


sql_password = input("Enter the password of sql : ")
mysqlcon = mysql.connect(host = 'localhost' , user = 'root' , password = sql_password , database = 'cs_project')
cursor_object = mysqlcon.cursor()

command = [''' create table sign_omg_data
(
user_id  varchar(20) not null,
password varchar(50) primary key
);''' ,'''insert into sign_omg_data value("Mayank_85679" , '22051845'); ''' ]

for i in command:
    cursor_object.execute(i)
