from flask import Flask, render_template,request,flash,redirect,url_for
from main import app,db,bcrypt,mail
from main.forms import BusinessForm,Login,Registration,resetForm,resetPassword
from main.models import User,BusinessClass
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
# class Registration(FlaskForm)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Unsuccessfull Log-in','danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
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
@login_required
def dashboard():
    return render_template('dashboard.html',title='Dashboard')

@app.route('/addProject',methods=['GET','POST'])
@login_required
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    logout_user()
    return render_template('account.html',title='Account')


def sendEmail(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request',sender='noreply@demo.com',recipients=[user.email])
    msg.body=f'''
    To Reset your password please visit the following link:
    { url_for('reset_token',token=token,_external=True) }
    If you didn't make this request then simply ignore this email.
    '''
    mail.send(msg)

@app.route('/reset_password',methods=['GET','POST'])
def reset_Password_Request():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form=resetForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        sendEmail(user)
        flash('Email Has been sent with instructions','info')
        return redirect(url_for('login'))
    return render_template('resetRequest.html',title='Reset Password',form=form)

@app.route('/set_password/<token>',methods=['GET','POST'])
def set_Password_Request():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user=User.verify(url_for('dashboard'))
    if user is None:
        flash('That is an invalid or expired token','warining')
        return redirect(url_for('set_Password_Request'))
    form=resetPassword()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash('Your Password has been updated!','success')
        return redirect(url_for('login'))
    return render_template('reset_token.html',title='Reset Password',form=form)
