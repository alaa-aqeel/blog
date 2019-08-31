import os 
from flask  import redirect,url_for,request
from jinja2 import Markup
from flask_security import current_user 
from flask_ckeditor import CKEditorField
from flask_admin    import form
from flask_admin.contrib.sqla import ModelView 
from application    import admin, db



class CustomModelVIew(ModelView):

	# can_export        = False
	can_view_details  = True
	can_set_page_size = True

	list_template    = 'admin/list.html'
	edit_template    = 'admin/edit.html'
	create_template    = 'admin/create.html'
	details_template    = 'admin/details.html'



	def inaccessible_callback(self,name,**kw):
		return redirect("/")
		
	def is_accessible(self): 
		return current_user.has_role('admin')

class UserModelView(CustomModelVIew): 
	column_searchable_list = ('fullname',)

	column_exclude_list   = ['posts']
	form_excluded_columns = ['posts','create_at']

class PostsModelView(CustomModelVIew):

	column_searchable_list = ('title',)

	load_ckeditor  = True 

	form_overrides = {
		'post'  : CKEditorField
	}

	details_template = 'admin/posts_details.html'

	column_exclude_list   = ['post','header_img']
	form_excluded_columns = ['create_at','user']

	def _list_thumbnail(view, context, model, name):
		if not model.header_img:
			return ''

		return Markup('<img src="%s">' % url_for('static',
			filename="img/headers/"+form.thumbgen_filename(model.header_img)))

	column_formatters = {
		'header_img': _list_thumbnail
	}

	def prefix_name_image(obj, file_data):
		parts = os.path.splitext(file_data.filename)
		return 'headers-%s%s' % parts

	form_extra_fields = {
		'header_img': form.ImageUploadField('Image',
				base_path='public/static/img/headers/',
				thumbnail_size=(100, 100, True),
				namegen=prefix_name_image,
				url_relative_path='img/headers/'
			)
	}

	def on_model_change(self,form, model, is_created):
		if is_created :
			current_user.posts.append(model)
			db.session.commit()


class ContactModelView(CustomModelVIew):
	can_create        = False 
	column_searchable_list = ('fullname',)

	column_exclude_list   = ['message']
	form_excluded_columns = ['create_at']
		



