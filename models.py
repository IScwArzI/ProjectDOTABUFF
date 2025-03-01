from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    win_rate = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Hero {self.name}>'
