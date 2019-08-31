# Blog with flask

### Template&themes 
  - Startbootstrap <a href="https://startbootstrap.com/themes/clean-blog/" >clean-blog</a> 

### requirements lib install
  - flask
  - [flask-admin](https://github.com/AlaaProg/flask-admin) bootstrap 4 support
  - Flask-SQLAlchemy
  - Flask-Migrate
  - Flask-WTF
  - python-dotenv
  - flask-ckeditor 
  - flask_security

### Rune
   - creaet .env file insade
        ```
           FLASK_ENV=development
           FLASK_APP=manager.py
        ```
  - `$ flask db init`
  - `$ flask db migrate`
  - `$ flask db upgrade`
  - `$ flask users create admin@email.com`
  - `$ flask users activate admin@email.com`
  - `$ flask roles create admin`
  - `$ flask roles add admin@email.com admin`
  - `$ flask run -p 8000`
