
from flask import render_template, redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Users
from application.forms import RegistrationForm, LoginForm, SearchForm, CreateForm, AddShelfForm, DescShelfForm
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Books, Users, Bookshelf 
import pandas as pd
from sqlalchemy  import func, select 



@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():   
    return render_template('home.html', title='Home Page', sform=SearchForm())
   

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
    return render_template('login.html', title='Login', form=form, sform=SearchForm())


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'), sform = SearchForm())


@app.route('/library', methods =['Get', 'POST'])
def library():
    books = Books.query.order_by(func.random()).limit(6)
    books2 = Books.query.order_by(func.random()).limit(6)
    return render_template('library.html', title ='Library', Books1=books, Books2=books2, sform=SearchForm())


@app.route('/shelf', methods=['GET','POST'])
@login_required
def shelf():

    form = CreateForm()
    if form.validate_on_submit():
        addBook= Bookshelf(bookshelf_name=form.shelf_name.data, book_name='NaN', book_image='NaN', book_sid=1)
        db.session.add(addBook)
        db.session.commit()

        return redirect(url_for('create_shelf'))

       
    return render_template('shelf.html', title='My Shelf', sform = SearchForm(), form=form)


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
    return render_template('register.html', title='Register', form = form, sform=SearchForm())


@app.route('/search_results', methods=['GET', 'POST'])
def search_results():   
    sform = SearchForm()
    if sform.validate_on_submit():
        search_data = "%s"%(sform.search.data)
        books = Books.query.filter(Books.book_title.like("%"+search_data+"%")).all()
        sform = SearchForm()
        return render_template('book-search.html', title ='Your search results',sform = sform, books = books)
    return render_template('book-search.html', title ='Your search results',sform = sform)

@app.route('/create_shelf', methods=['GET', 'POST'])
@login_required
def create_shelf():
    form = DescShelfForm()
    if form.validate_on_submit():
        search_data = "%s"%(form.addbook_name.data)
        books = Books.query.filter(Books.book_title.like("%"+search_data+"%")).all()
       


        return render_template('create_shelf.html', title='Create new Shelf', sform= SearchForm(),aform=AddShelfForm(),form=form,books=books)

    return render_template('create_shelf.html', title='Create new Shelf', sform= SearchForm(), form=form)
   
