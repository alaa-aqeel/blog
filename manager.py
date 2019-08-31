import os, flask 
from flask_security import Security, SQLAlchemyUserDatastore 
from flask_migrate  import Migrate
from application    import create_app, db
from admin          import models

# load the .flaskenv
flask.cli.load_dotenv()


app            = create_app(os.getenv("FLASK_ENV","production"))
migrate        = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security       = Security(app, user_datastore)



# add model to flask shell
@app.shell_context_processor
def make_shell_context():
	modules = dict(app=app)
	modules['User']    = models.User
	modules['Role']    = models.Role
	modules['Post']    = models.Post
	modules['Contact'] = models.Contact
	return modules


if os.getenv('FLASK_ENV') == 'development':
	@app.before_first_request
	def before_first_request():
		try:
			db.session.bulk_update_mappings(models.User,[{'_password':12345678,'id':1}])
			db.session.commit()
			print("Update default admin_1 `password`='%s'"%str(12345678))
		except:
			print("!Update default admin_1 `password`='%s'"%str(12345678))