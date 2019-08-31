from flask_security        import UserMixin, RoleMixin , utils
from sqlalchemy.ext.hybrid import hybrid_property
from application           import db 


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model,RoleMixin):
    __tablenaem__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text())
    def __str__(self): return str(self.name)

class User(db.Model,UserMixin):
	__tablenaem__ = 'user'

	id        = db.Column(db.Integer()  ,primary_key=True)
	email     = db.Column(db.String(255), unique=True)
	fullname  = db.Column(db.String(255) )
	_password  = db.Column('password',db.String(255) )
	active    = db.Column(db.Boolean()    ,default=False)
	create_at = db.Column(db.DateTime(),default=db.func.now())

	posts     = db.relationship('Post', backref='user', lazy='dynamic')	
	roles     = db.relationship('Role' , secondary=roles_users,
	                        backref=db.backref('user', lazy='dynamic'))
	

	def __str__(self): return str(self.fullname)

	@hybrid_property
	def password(self): 
		return self._password

	@password.setter
	def password(self, new_pass):
		if new_pass != self._password:
			new_password_hash = utils.hash_password(new_pass)
			self._password = new_password_hash

class Post(db.Model):
	__tablenaem__ = 'post'

	id         = db.Column(db.Integer()  ,primary_key=True)
	header_img = db.Column(db.String(255))
	title      = db.Column(db.String(255), unique=True)
	subtitle   = db.Column(db.Text())
	post       = db.Column(db.Text())

	create_at = db.Column(db.DateTime(), default=db.func.now())
	user_id   = db.Column(db.Integer() , db.ForeignKey('user.id'))

	def __str__(self):return str(self.title)


class Contact(db.Model):
	__tablenaem__ = 'contact'
	
	id       = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(255))
	email    = db.Column(db.String(255))
	message  = db.Column(db.Text())	

	create_at = db.Column(db.DateTime(), default=db.func.now())