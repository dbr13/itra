import psycopg2
import sys

from psycopg2._psycopg import cursor

conn = None
try:
    conn = psycopg2.connect(database='pytest', user='tester', password='dober', host='localhost')
except:
    print('I\'m unable to connect to db')


cursor = conn.cursor()

#SQL query create table
#query = '''CREATE TABLE customers(id SERIAL PRIMARY KEY, name VARCHAR, age INTEGER);'''
#cursor.execute(query)


# SQL query insert data

namedict =({'name':'Dam', 'age': 37},
           {'name':'Dober', 'age': 35})

#query = '''INSERT into customers (name, age) values(%(name)s, %(age)i)''', namedict
#cursor.executemany('''INSERT into customers (name, age) values(%(name)s, %(age)s)''', namedict)

#conn.commit()

query = '''Select * from customers'''
cursor.execute(query)
#rows = cursor.fetchone()
print('\n rows:\n')
res = []
D = {}
for row in cursor:
    res.append(row)
    D[row[1]]= row[2]

cursor.close()
conn.close()

print(res)
print(D)

