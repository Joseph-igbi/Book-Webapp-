
from application import db
from application.models import Books
import pandas as pd



db.drop_all()
db.create_all()

if len(Books.query.all()) < 1:
    data = pd.read_excel('.data/book_data.xlsx')   
    data.columns=['author','desc', 'pages','title','genre', 'image']
    for index, row  in data.iterrows():
        book = Books(author=row[0],book_desc= row[1], book_pages=row[2], book_title=row[3], book_genre=row[4],book_image=row[5])
        db.session.add(book)
    db.session.commit()
