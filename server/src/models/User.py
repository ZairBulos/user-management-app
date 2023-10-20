from src.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastName': self.last_name,
            'age': self.age
        }

    @classmethod
    def create(cls, name, last_name, age):
        user = User(name=name, last_name=last_name, age=age)
        return user.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except Exception as e:
            raise e

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            raise e
