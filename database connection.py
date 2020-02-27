import mysql.connector as mysql
conn=mysql.connect(user="root", password="scott",
                   host="127.0.0.1")
c=conn.cursor()

c.execute("show table from ASHUTOSH_75")
print(c.fetchall())
conn.close()
