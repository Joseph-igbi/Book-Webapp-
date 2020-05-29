from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime



class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(300), nullable=False)
    book_desc = db.Column(db.String(1000), nullable=False, unique=True)
    book_pages = db.Column(db.String(10), nullable=False)
    book_title= db.Column(db.String(300), nullable=False, unique=True)
    book_genre=db.Column(db.String(300), nullable=False)
    book_image=db.Column(db.String(200), nullable=False) 
    def __repr__(self):
        return''.join(['book: ', self.book_title, '\r\n','Pages:', self.book_pages, '\r\n', 'Author: ', self.author, '\r\n', 'Genre: ',self.book_genre,'\r\n','Image: ', self.book_image,'\r\n', 'Description', self.book_desc])


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password= db.Column(db.String(500), nullable=False)
    lib_rel = db.relationship('Library', backref='librarian', lazy=True)
    booksh_rel= db.relationship('Bookshelf', backref='user_book', lazy=True) 
   
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

class Library(db.Model, UserMixin):
    library_id=db.Column(db.Integer, primary_key=True)
    library_name=db.Column(db.String(200), nullable= False)
    date_created= db.Column(db.DateTime, nullable=False, default =datetime.utcnow)
    libuser_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #booksh_rel = db.relationship('Bookshelf', backref = 'book_placed', lazy=True)

class Bookshelf(db.Model, UserMixin):
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default =datetime.utcnow)
    book_name= db.Column(db.String(400), nullable= False)
    book_image= db.Column(db.String(400), nullable= False)
    book_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    library_id =  db.Column(db.Integer, nullable=False)
    #library_id =  db.Column(db.Integer, db.ForeignKey('library.library_id'), nullable=False)
    #def __repr__(self):
      #  return ''.join(['bookselfID: ', self.bookshelf_id, '\r\n', 'shelf_name: ', self.bookshelf_name])    
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))


