import sqlite3
import sqlalchemy

connection = sqlite3.connect('Users.db')

cursor = connection.cursor()

cursor.execute('''Create Table if NOT EXISTS USERS(User_ID INT, First_Name TEXT, Last_Name TEXT, Email_Address TEXT)''')

Add_Users = [(1, 'Jack', 'Sparrow', 'jack@gmail.com'),
             (2, 'Harry', 'Styles', 'styles.harry@hotmail.com'),
             (3, 'Jamie', 'Ooi', 'jamie@gmail.com'),
             (4, 'Peter', 'Parker', 'peter@hotmail.com'),
             (5, 'Kevin', 'Owens',  'Owens.kevin@social.com')]

cursor.executemany('INSERT INTO USERS VALUES (?,?,?,?)', Add_Users)

cursor.execute('Select Email_Address FROM USERS')
print(cursor.fetchall())

connection.commit()
connection.close()

engine = sqlalchemy.create_engine('sqlite:///Users.db', echo=True)

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("USERS" , metadata,
                               sqlalchemy.Column("Email_Address", sqlalchemy.Text))

with engine.connect() as Conn:
  for i in Conn.execute(sqlalchemy.select(users_table)):
    print(i)
