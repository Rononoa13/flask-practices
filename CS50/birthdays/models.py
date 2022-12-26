from app import db

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Item {self.name}"