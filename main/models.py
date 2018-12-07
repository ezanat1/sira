from datetime import datetime
from main import db,login_manager

'''
Two tables for application
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstName=db.Column(db.String(30),unique=False,nullable=False)
    middleName=db.Column(db.String(30),unique=False,nullable=False)
    lastName=db.Column(db.String(30),unique=False,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    # image_file=db.Column(db.String,primary_key=True)
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('BusinessClass',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.firstName}','{self.email}')"

class BusinessClass(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    projectName=db.Column(db.String(120),unique=True,nullable=False)
    projectTags=db.Column(db.String(30),unique=True,nullable=False)
    projectDescription=db.Column(db.Text,unique=True,nullable=False)
    projectProblem=db.Column(db.Text,unique=True,nullable=False)
    projectSolution=db.Column(db.Text,unique=True,nullable=False)
    data_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"BusinessClass('{self.projectName}','{self.data_posted}')"