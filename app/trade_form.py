from wtforms import SelectField
from app.trade_base_form import OSABaseForm

class REGIONBForm(OSABaseForm):
    exchanges=SelectField('Exchange',choices=[('EC','EC'),('CS','CS')])

