from application import db
from application.models import Book
from faker import Faker

faker = Faker()

for _ in range(25):
    title = faker.word().capitalize()
    author = f'{faker.last_name()} {faker.first_name()}'
    db.session.add(Book(title=title, author=author))
db.session.commit()
