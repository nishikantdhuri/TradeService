from flask import g
from app import app
from app.extn.flask_validate import Validate
if __name__ == '__main__':
    #_ext = Validate(app)
    #app.config['extn']=_ext
    #_ext.configure()
    app.run(port=82)