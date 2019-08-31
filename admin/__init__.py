from flask_admin.contrib import fileadmin
from application import db 
from admin       import views
from admin       import models 



def admin_init(admin):

	admin.add_view(views.UserModelView(models.User, db.session, name="User",category="Admin"))
	admin.add_view(views.PostsModelView(models.Post, db.session, name="Post",category="Admin"))
	admin.add_view(views.ContactModelView(models.Contact, db.session, name="Contact",category="Admin"))
