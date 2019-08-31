from flask       import render_template
from blog        import views



def blog_init(app,admin):

	admin.init_app(app,index_view=views.AdminIndex(url='/'),endpoint='home')
	admin.add_view(views.About(url='/about',name='About'))	
	admin.add_view(views.ContactMe(url='/contactme',name='Contact Me'))	


	##  admin url 
	admin.add_view(views.Login(url='/login',name='login',menu_class_name='no'))
	admin.add_view(views.PostView(url='/post/<postid>',name='PostView',menu_class_name='no'))
	


	## app url 
	app.add_url_rule("/upload",view_func=views.upload,methods={'POST'})	


	@app.errorhandler(404)
	def page_not_found_error(error):
		return render_template('errors_page/404.html'), 404