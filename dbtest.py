import sqlite3
conn=sqlite3.connect('pms.db')
cur=conn.cursor()
cur.execute("create table employee_details(eid int,ename varchar(20),dptid int,designation varchar(20),email varchar(20),contact int,address varchar(20))")
cur.execute("create table attendance(dptid int,dptname varchar(20),eid int,ename varchar(20),date datetime,timein datetime,timeout datetime)")
cur.execute("create table sallary_details(eid int,dptid int,account_number int,pan int,base_sallary int )")

conn.commit()
conn.close()
