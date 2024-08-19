from modules.app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Contact(id={self.id}, phone='{self.phone}', name='{self.name}')>"

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "name": self.name
        }


with app.app_context():
    db.create_all()
