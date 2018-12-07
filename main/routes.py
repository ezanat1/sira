from flask import Flask, render_template,request,flash,redirect,url_for
from main import app,db,bcrypt
from main.forms import BusinessForm,Login,Registration
from main.models import User,BusinessClass
from flask_login import login_user

# class Registration(FlaskForm)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Unsuccessfull Log-in','danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form=Registration()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(firstName=form.firstName.data,middleName=form.middleName.data,lastName=form.lastName.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created','success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form,title='Register')

@app.route('/dash',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html',title='Dashboard')

@app.route('/addProject',methods=['GET','POST'])
def addProject():
    newList=[]
    form=BusinessForm()
    if request.method =='POST':
        # projectName=request.form['projectName']
        # print(projectName)
        # projectTags=request.form['projectTags']
        # projectDescription=request.form['projectDescription']
        # projectMembers=request.form['projectMembers']
        # projectProblem=request.form['projectProblem']
        # projectSolution=request.form['projectSolution']
        # newList.append(projectName)
        print(newList)
        return render_template('dashboard.html',newList=newList,title='Create Campaign',form=form)
    return render_template('projects.html')