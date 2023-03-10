import psycopg2

hostname='localhost'
database='postgres'
username='postgres'
password='Syam'
port_id=5433
conn=None
cur=None
# Establish a connection to the database
try:
    conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=password,
            port=port_id   
    )
    cur=conn.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script='''CREATE TABLE IF NOT EXISTS employee(
                    id int PRIMARY KEY,
                    Name  varchar(50)NOT NULL,
                    salary int,
                    designation varchar(20)
                    )'''
    cur.execute(create_script)
    insert_script='INSERT INTO employee(id,Name,salary,designation) VALUES (%s,%s,%s,%s)'
    insert_values=[(1,'AISHWARYA MURALI',32000,'java'),(2,'ANJA',22000,'jr developer'),(3,'ANTO',72000,'sr developer'),(4,'abin',52000,'software engnieer'),(5,'swali',32000,'software engnieer'),(6,'ali',15000,'XXX')]
    for d in insert_values:
        cur.execute(insert_script,d)
    #fecth datas
    cur.execute('SELECT *FROM EMPLOYEE')
    for d in cur.fetchall():
        print(d[1],d[2])
    #print(cur.fetchall)

    conn.commit()
except Exception as erorr:
    print(erorr)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
         conn.close()