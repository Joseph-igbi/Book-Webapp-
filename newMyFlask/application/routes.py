
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Users
from application.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Books
import pandas as pd





@app.route('/')

@app.route('/home')
def home():
   # data = pd.read_excel('./application/bslice1.xlsx')
   
   # data.columns=['author','desc', 'pages','title','genre', 'image']
   # for index, row  in data.iterrows():
    #    book = Books(author=row[0],book_desc= row[1], book_pages=row[2], book_title=row[3], book_genre=row[4],book_image=row[5])
     #   db.session.add(book)

   # db.session.commit()
    return render_template('home.html', title='Home Page')


   


    

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('library'))
    else:
        print(form.errors)
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/library')
def library():
    return render_template('library.html', title ='Library')

@app.route('/shelf')
@login_required
def shelf():
    return render_template('shelf.html', title='My Shelf')

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = Users(first_name=form.first_name.data,last_name= form.last_name.data,email=form.email.data, password=hash_pw)
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('register.html', title='Register', form = form)
