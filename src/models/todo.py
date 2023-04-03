from database.database import db

class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    label=db.Column(db.String, nullable=False)
    done=db.Column(db.)