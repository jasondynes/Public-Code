import sqlite3
db = sqlite3.connect("movies.db")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
