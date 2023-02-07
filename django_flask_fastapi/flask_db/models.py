from app import db


class Book(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text())
    price = db.Column(db.Integer)
    date_add = db.Column(db.TIMESTAMP(), default=db.func.now())
    status = db.Column(db.Boolean())

    def __str__(self):
        return str(f"Book title: {self.title}. Price: {self.price}")

