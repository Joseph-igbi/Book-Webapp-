from flask import render_template, redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Users
from application.forms import RegistrationForm, LoginForm, SearchForm, CreateForm,DescShelfForm, SelectBookshelf, DeleteBookshelf
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Books, Users, Library, Bookshelf 
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
    return redirect(url_for('login'))

@app.route('/library', methods =['Get', 'POST'])
def library():
    books = Books.query.order_by(func.random()).limit(6)
    books2 = Books.query.order_by(func.random()).limit(6)
    books3 = Books.query.order_by(func.random()).limit(6)
    books4 = Books.query.order_by(func.random()).limit(6)

    return render_template('library.html', title ='Library', Books1=books, Books2=books2,Books3=books3, Books4=books4,sform=SearchForm())


@app.route('/shelf', methods=['GET','POST'])
@login_required
def shelf():
   
    form = CreateForm()
    if form.validate_on_submit():
        create_sh= Library(library_name=form.shelf_name.data, librarian=current_user)
        db.session.add(create_sh)
        db.session.commit()

        return redirect(url_for('shelf'))
    
    string_user = str(current_user)
    num_user = string_user.strip('UserID: ')
    created_shelves = Library.query.filter_by(libuser_id =num_user)

    d_form =DeleteBookshelf()
    d_form.bookshelves.choices= [(shelf.library_id, shelf.library_id) for shelf in Library.query.filter_by(libuser_id=num_user)]

    dd_form= SelectBookshelf()
    dd_form.bookshelves.choices= [(shelf.library_id, shelf.library_id) for shelf in Library.query.filter_by(libuser_id=num_user)]
   
    
    if d_form.validate_on_submit:
        drop_down=d_form.bookshelves.data
    if dd_form.validate_on_submit:
        return render_template('shelf.html', title='My Shelf', sform = SearchForm(), form=form, cs=created_shelves,dd_form=dd_form, d_form=d_form, shelfid=dd_form.bookshelves.data)     

    return render_template('shelf.html', title='My Shelf', sform = SearchForm(), form=form, cs=created_shelves,dd_form=dd_form, d_form=d_form, shelfid=shelfid) 
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

@app.route('/edit_shelf/<shelfid>', methods=['GET', 'POST'])
@login_required
def edit_shelf(shelfid):
    shelfid=str(shelfid)
    form = DescShelfForm() 
    bookshelf = Bookshelf.query.filter_by(library_id = shelfid).all()
    shelfinfo = Library.query.filter_by(library_id=shelfid).first()
    shelf_name= shelfinfo.library_name
    search_data = "%s"%(form.addbook_name.data)
    books = Books.query.filter(Books.book_title.like("%"+search_data+"%")).all()
    if form.validate_on_submit():
        return render_template('create_shelf.html', title=shelf_name, sform= SearchForm(), form=form, books=books, sid=shelfid, shelfinfo=shelfinfo, bookshelf=bookshelf)

  

    
    return render_template('create_shelf.html', title='Create new Shelf', sform= SearchForm(), form=form, books=books, sid=shelfid, bookshelf=bookshelf, shelfinfo=shelfinfo)
    

@app.route('/shelf/delete', methods=['GET','POST'])
@login_required
def shelf_delete():
     d=DeleteBookshelf()
     ds=d.bookshelves.data
     delbooks = Bookshelf.query.filter_by(library_id=ds).all()
     for books in delbooks:  
         db.session.delete(books)
     delshelf = Library.query.filter_by(library_id=ds).first()
     db.session.delete(delshelf)
     db.session.commit()
     return redirect(url_for('shelf'))

@app.route('/shelf/middleman', methods=['GET','POST'])
@login_required
def middleman():
    shelfid = SelectBookshelf()
    shelfid = shelfid.bookshelves.data
    shelfid=str(shelfid)
    
    return redirect('/edit_shelf/%s'%(shelfid))

@app.route('/edit_shelf/<sid>/remove', methods=['GET','POST'])
@login_required
def remove(sid):
    bookshelf = Bookshelf.query.filter_by(library_id =sid).all()
    for books in bookshelf:
        print('BOOOOOOOOOKS', books.bookshelf_id)
    shelfinfo = Library.query.filter_by(library_id = sid).first()
    shelf_name= shelfinfo.library_name

    return render_template('remove_book.html', title=shelf_name, sform= SearchForm(), sid=sid, books=bookshelf, shelfinfo=shelfinfo)

@app.route('/add/<sid>/shelf/<book_id>/', methods=['GET','POST'])
@login_required
def add(sid, book_id):
    book_id =str(book_id)
    print('shelf id at add: ', sid)
    book = Books.query.filter_by(book_id= book_id).first()

    addbook = Bookshelf(book_name=book.book_title, book_image= book.book_image, user_book=current_user, library_id= sid)
    db.session.add(addbook)
    db.session.commit()
    
    return redirect('/edit_shelf/%s'%(sid))


@app.route('/delete/<sid>/shelf/<book_id>', methods=['GET','POST'])
@login_required
def book_delete(sid, book_id):
    book_id =str(book_id)
    print('shelf id at add: ', sid)
    book = Bookshelf.query.filter_by(bookshelf_id=book_id, library_id=sid).first()
    db.session.delete(book)
    db.session.commit()
    
    return redirect('/edit_shelf/%s'%(sid))


