import sqlite3
import pandas as pd
dbase=sqlite3.connect('our_data.db') 
print("database openeed")
dbase.execute('''CREATE TABLE IF NOT EXISTS book_store(
              ID INT PRIMARY KEY NOT NULL,
              NAME TEXT NOT NULL,
              DIVISION TEXT NOT NULL,
              STARS INT NOT NULL)''')
print("table created")
table_query="SELECT * FROM book_store"


def insert_record(ID , NAME, DIVISION, STARS):
    dbase.execute('''INSERT INTO book_store(ID,NAME,DIVISION,STARS)
                VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))
    dbase.commit()



# insert_record(  00, 'bob', 'hardware', 4)


print("database closed")
def read_data():
    data=dbase.execute('''SELECT ID, NAME, DIVISION, STARS FROM book_store ''')
    for record in data:
        print ("ID :"+str(record[0]))
        print ("NAME :"+str(record[1]))
        print ("VISION :"+str(record[2]))
        print ("STARS :"+str(record[3]))
        print("\n \n")


def update_data():
    dbase.execute('''UPDATE book_store SET DIVISION="software" WHERE ID="6"''')
    dbase.commit()
def delete_data():
    dbase.execute('''DELETE from book_store WHERE ID="6"''')
    dbase.commit()
delete_data()
update_data()
read_data()
data=pd.read_sql(table_query,dbase)
data.to_csv("table.csv",index=False)
dbase.close()