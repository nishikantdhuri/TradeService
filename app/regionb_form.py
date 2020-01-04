from wtforms import SelectField
from app.region_form import OSABaseForm

class REGIONBForm(OSABaseForm):
    exchanges=SelectField('Exchange',choices=[('EC','EC'),('CS','CS')])

