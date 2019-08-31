from flask_wtf      import FlaskForm 
from wtforms        import TextAreaField,StringField , validators as valid 



class ContactForm(FlaskForm):
	fullname = StringField("Full Name", validators=[valid.required()])
	email    = StringField("Email"    , validators=[valid.email(),valid.required()])
	message  = TextAreaField("message", validators=[valid.required()])
