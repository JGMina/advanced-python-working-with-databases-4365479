import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(User_ID TEXT, FName TEXT, LName TEXT, Email TEXT)''')

# famousMovies = [
#     ('X0001', 'Sahloul', 'Taxi', 'sahloul@gmail.com'),
#     ('X0002', 'Zaal', 'Martin', 'zaal@gmail.com'),
#     ('X0003', 'Martin', 'Scorsese', 'ms@msn.com'),
#     ('X0004', 'Matt', 'Salah', 'matt@msn.com'),
#     ('X0005', 'Maten', 'Scott', 'maten@msn.com')
#     ]
# cursor.executemany('INSERT INTO Users VALUES(?,?,?,?)', famousMovies)

cursor.execute("SELECT Email FROM Users")
results = cursor.fetchall()
for email in results:
  print(str(email).replace(",", ""))

connection.commit()
connection.close()

