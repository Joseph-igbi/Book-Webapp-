
from application import db
from application.models import Books



db.drop_all()
db.create_all()
