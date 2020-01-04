from flask_wtf import FlaskForm
from wtforms import BooleanField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Required,Optional,Length

class OSABaseForm(FlaskForm):
    trade_user=StringField('Trade User',[DataRequired()])
    trade_name=StringField('Trade Name',[DataRequired(),Length(min=4,message=('invalid trade name'))])
    trade_quantity=StringField('Traee Quantity',[DataRequired()])
    submit=SubmitField('Submit')




