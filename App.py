import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT)''')

famousMovies = [('Taxi Driver', 'Martin Scorsese', 1976), ('Taxi Driver 2', 'Martin Scorsese', 1977), ('Taxi Driver 3', 'Martin Scorsese', 1978)]
# cursor.executemany('INSERT INTO Movies VALUES(?,?,?)', famousMovies)

release_year = (1976,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

# print(cursor.fetchone())
print(cursor.fetchall())

connection.commit()
connection.close()

