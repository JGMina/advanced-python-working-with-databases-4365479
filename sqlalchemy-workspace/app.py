import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

films = [('Pulp Fiction', 'Quentin Tarantino', 1994),
         ('Back to the Future', 'Robert Zemeckis', 1985), 
         ('Moonrise Kingdom', 'Wes Anderson', 2012)]

cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', films)

connection.commit()
connection.close()