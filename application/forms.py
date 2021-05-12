from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CryptoForm(FlaskForm):
   name = StringField('Name of cryptocurrency', validators=[DataRequired()])
   acronym = StringField('Acronym of crypto', validators=[DataRequired()])
   description = StringField('Descryption of crypto', validators=[DataRequired()])
   valueusd = IntegerField('Value of crypto USD', validators=[DataRequired()]) 
   submit = SubmitField('Add cryptocurrency')

class ArticlesForm(FlaskForm):
   title = StringField('Title of article', validators=[DataRequired()])
   author = StringField('Author of article', validators=[DataRequired()])
   topic = StringField('Topic of article', validators=[DataRequired()])
   link = StringField('Link to article', validators=[DataRequired()]) 
   submit = SubmitField('Add article')