# Question 1,2,3,4

import sqlite3
try:
    con=sqlite3.connect('students.db')
    query='create table stud(name varchar(15),marks int(3))'
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    for i in range(0,10):
        name=input("name: ")
        marks=input("marks: ")
        lst=[(name, marks)]
        query = 'insert into stud(name,marks) values(?,?)'
        con.executemany(query, lst)
    con.commit()
    q='select * from stud where marks>80'
    data=cursor.execute(q)
    for row in data:
        print('name: {}, marks: {}'.format(row[0],row[1]))
finally:
    print('database created successfully')
    con.close()


