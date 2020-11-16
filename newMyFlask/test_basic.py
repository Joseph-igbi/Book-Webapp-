import os
import unittest
 
from application import app, db
 
 
 
 
class BasicTests(unittest.TestCase):
 
    #### setup and teardown ####
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI']="sqlite://"
        app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
#### helper methods ####
 
 
    def register(self, email, password, confirm):
        new_user= Users(first_name ='Joseph', last_name= 'Igbi', email='joseph.igbi@joseph.com', password='password')
        db.session.add(user)
        db.session.commit()
 
    def login(self, email, password):
        return self.app.post('/login',
                 data=dict(email=email, password=password),
                 follow_redirects=True)
 
    def logout(self):
        return self.app.get('/logout', follow_redirects=True
    ) 


#### tests ####

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        response = self.app.get('register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_Library_page(self):
        response = self.app.get('library', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        self.register()
        self.app.get('/login', follow_redirects=True)
        return self.assertEqual(response.status_cod, 200)







if __name__ == "__main__":
    unittest.main()
