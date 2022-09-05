import sqlite3
from faker import Faker


connection = sqlite3.connect('books_db.sqlite')

with open('schema.sql', 'r') as f:
    connection.executescript(f.read())

cursor = connection.cursor()
faker = Faker()

for _ in range(25):
    title = faker.word().capitalize()
    author = f'{faker.last_name()} {faker.first_name()}'
    cursor.execute('INSERT INTO books(title, author) VALUES (?, ?)', (title, author))


connection.commit()
connection.close()
