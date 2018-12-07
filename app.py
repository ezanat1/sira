from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from models import User,BusinessClass
app = Flask(__name__)
app.config['SECRET_KEY']='ekmys@123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///biz.db'
db=SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addProject',methods=['GET','POST'])
def addProject():
    newList=[]
    if request.method =='POST':
        projectName=request.form['projectName']
        print(projectName)
        projectTags=request.form['projectTags']
        projectDescription=request.form['projectDescription']
        projectMembers=request.form['projectMembers']
        projectProblem=request.form['projectProblem']
        projectSolution=request.form['projectSolution']
        newList.append(projectName)
        print(newList)
        return render_template('dashboard.html',newList=newList)
    return render_template('projects.html')



    def __repr__(self):
        return f"BusinessClass('{self.projectName}','{self.data_posted}')"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
