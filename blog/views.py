import os 
from flask            import request , redirect , flash, url_for,current_app, render_template
from flask_security   import login_user , logout_user  ,forms  , current_user 
from flask_admin      import expose ,form , BaseView, AdminIndexView
from flask_ckeditor   import upload_fail, upload_success
from sqlalchemy.event import listens_for
from admin.models     import db,Contact,Post
from blog.forms       import ContactForm


@listens_for(Post, 'after_delete')
def del_image(mapper, connection, target):
	if target.header_img:
		try:
			os.remove(os.path.join(current_app.config['UPLOAD_FOLDER']+'headers/', target.header_img))
		except OSError: pass
		try:
			os.remove(os.path.join(current_app.config['UPLOAD_FOLDER']+'headers/',
				form.thumbgen_filename(target.header_img)))
		except OSError: pass

def upload():
	if not current_user.has_role('admin') : 
		return upload_fail(message='Admin only!')
	f = request.files.get('upload')
	extension = f.filename.split('.')[1].lower()
	if extension not in ['jpg', 'gif', 'png', 'jpeg']:
		return upload_fail(message='Image only!')
	f.save(os.path.join(current_app.config['UPLOAD_FOLDER']+'posts/', f.filename))
	return upload_success(url="/static/img/posts/%s"%f.filename)


class AdminIndex(AdminIndexView):
	def __init__(self,*k,**kw):
		super(AdminIndex, self).__init__(*k,**kw)

	@expose()
	@expose("/<page>")
	@expose("/home/")
	@expose("/home/<int:page>")
	def home(self,page=1):
		poats = Post.query.order_by(Post.create_at.desc()).paginate(
						page=page,
						per_page=current_app.config['PRE_PAGE_POSTS'],
						error_out=False
					)
		return self.render("index.html",posts=poats)

class Login(BaseView):
	def inaccessible_callback(self,name,**kw):
		return redirect("/")
		
	def is_accessible(self): 
		return not current_user.is_authenticated

	@expose('/',methods=['POST','GET'])
	def login(self):
		form = forms.LoginForm(request.form)
		if form.validate_on_submit():
			login_user(form.user, remember=form.remember.data)
			return redirect("/")
		return self.render("login.html",login_user_form=form)

class Logout(BaseView):
	def inaccessible_callback(self,name,**kw):
		return redirect("/")
		
	def is_accessible(self): 
		return current_user.is_authenticated

	@expose()
	def index(self):
		logout_user()
		return redirect('/')

class About(BaseView):
	@expose()
	def about(self):
		return self.render("about.html")

class ContactMe(BaseView):

	@expose('/',methods={'GET'})
	def index(self):
		return self.render("contact.html")

	@expose("/send",methods={'POST'})
	def message(self):
		form = ContactForm()
		if form.validate_on_submit():
			contact = Contact(
					fullname=form.fullname.data,
					email= form.email.data,
					message= form.message.data,
				)

			db.session.add(contact)
			db.session.commit()
			flash("Successfuly Send ")

			return redirect(url_for('contactme.index'))

		flash(str(form.errors),'error')
		return redirect(url_for('contactme.index'))


class PostView(BaseView):
	@expose()
	def index(self,postid):
		post = Post.query.filter_by(id=postid).first()
		if not post : return redirect('/')
		return self.render('post.html',post=post)
