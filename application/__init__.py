from flask            import Flask 
from flask_admin      import Admin 
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor   import CKEditor

db       =  SQLAlchemy()
ckeditor = CKEditor()
admin    = Admin(url='/',
    base_template='layout/base.html'
)


def create_app(env):

    app = Flask(__name__)

    # Config 
    from .setting import config
    app.config.from_object(config[env])

    app.static_folder   =  app.config["STATIC_FOLDER"]
    app.template_folder =  app.config["TEMPLATE_FOLDER"]

    admin.name = app.config['APP_NAME']
    admin.template_mode = app.config['ADMIN_TEMPLATE_MODE']

    db.init_app(app)
    ckeditor.init_app(app)

    from blog import blog_init,views
    blog_init(app,admin)

    from admin import admin_init
    admin_init(admin)

    #
    admin.add_view(views.Logout(url='/logout',name='Log Out',category="Admin"))

    return app 