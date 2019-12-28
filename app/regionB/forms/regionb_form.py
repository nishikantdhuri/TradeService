from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,SelectField,DecimalField
from wtforms.validators import DataRequired,Length
from app.forms.region_form import OSABaseForm

class REGIONBForm(OSABaseForm):
    exchanges=SelectField('Exchange',choices=[('EC','EC'),('CS','CS')])

