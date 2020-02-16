

from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime

class Books(db.Model):
    b_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(300), nullable=False)
    book_desc = db.Column(db.String(1000), nullable=False, unique=True)
    book_pages = db.Column(db.String(10), nullable=False)
    book_title= db.Column(db.String(300), nullable=False, unique=True)
    book_genre=db.Column(db.String(300), nullable=False)
    book_image=db.Column(db.String(200), nullable=False)
   

    def __repr__(self):
        return''.join(['book: ', self.book_title, '', self.book_pages, '\r\n', 'Author: ', self.author, '\r\n', self.book_genre])



class Users(db.Model, UserMixin):
    u_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password= db.Column(db.String(500), nullable=False)
   
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
    
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
