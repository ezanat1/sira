from flask import Flask, render_template,request
from main import app
from main.forms import BusinessForm,Login,Registration
from main.models import User,BusinessClass


# class Registration(FlaskForm)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form=Login()
    return render_template('login.html',title='Login')

@app.route('/register')
def register():
    form=Registration()
    return render_template('register.html',title='Register')

@app.route('/dash')
def dashboard():
    return render_template('dashboard.html',title='Dashboard')

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
        return render_template('dashboard.html',newList=newList,title='Create Campaign')
    return render_template('projects.html')