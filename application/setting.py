import os 

class Config(object):

	# flask 
	APP_NAME         = os.getenv("APP_NAME"       , "Blog")
	SECRET_KEY       = os.getenv("SECRET_KEY"     , os.urandom(24))
	DEBUG            = os.getenv("FLASK_DEBUG"    , True)
	STATIC_FOLDER    = os.getenv("STATIC_FOLDER"  , './../public/static/')
	TEMPLATE_FOLDER  = os.getenv("TEMPLATE_FOLDER", './../public/templates/')
	UPLOAD_FOLDER    = os.getenv('UPLOAD_FOLDER'  , 'public/static/img/')
	TEMPLATES_AUTO_RELOAD = True 


	PRE_PAGE_POSTS    = 8

	# flask-wtf
	WTF_CSRF_ENABLED    = os.getenv("CSRF_ENABLED",True)
	WTF_CSRF_SECRET_KEY = str(SECRET_KEY)

	# flask-admin
	ADMIN_TEMPLATE_MODE = os.getenv('ADMIN_TEMPLATE_MODE', 'bootstrap4') 

	CKEDITOR_PKG_TYPE    = 'full'
	CKEDITOR_LANGUAGE    = 'en'
	CKEDITOR_HEIGHT      = 400
	CKEDITOR_ENABLE_CODESNIPPET = True
	CKEDITOR_FILE_UPLOADER      =  'upload'

	SECURITY_PASSWORD_SALT = str(SECRET_KEY)
	SECURITY_LOGIN_URL     = '/login'
	SECURITY_LOGOUT_URL    = '/logout'

class Development(Config):
	
	DEBUG = True 

	WTF_CSRF_ENABLED               = os.getenv("CSRF_ENABLED",False)
	CKEDITOR_SERVE_LOCAL           = True 

	SQLALCHEMY_DATABASE_URI        = os.getenv('DATABASE_URL', "sqlite:///"+os.path.join(os.getcwd(),'development.db.sqlite3'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
	
	DEBUG            = False 

	SQLALCHEMY_DATABASE_URI        = os.getenv('DATABASE_URL',  "sqlite:///"+os.path.join(os.getcwd(),'production.db.sqlite3') )
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
	
	DEBUG   = True 
	TESTING = True

	SQLALCHEMY_DATABASE_URI        = os.getenv('DATABASE_URL',  "sqlite:///"+os.path.join(os.getcwd(),'testing.db.sqlite3'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	PRESERVE_CONTEXT_ON_EXCEPTION  = False
	

config = {
	"development" : Development,
	"production" : Production,
	"testing":Testing
}