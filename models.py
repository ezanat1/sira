from datetime import datetime
from app import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstName=db.Column(db.String(30),unique=True,nullable=False)
    middleName=db.Column(db.String(30),unique=True,nullable=False)
    lastName=db.Column(db.String(30),unique=True,nullable=False)
    userName=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String,primary_key=True)
    password=db.Column(db.String(60),nullable=False)
    post=db.relationship('BusinessClass',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.userName}','{self.email}',{'self.image_file'})"

class BusinessClass(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    projectName=db.Column(db.String(120),unique=True,nullable=False)
    projectTags=db.Column(db.String(30),unique=True,nullable=False)
    projectDescription=db.Column(db.Text,unique=True,nullable=False)
    projectProblem=db.Column(db.Text,unique=True,nullable=False)
    projectSolution=db.Column(db.Text,unique=True,nullable=False)
    data_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)