from flask import g
from app import app
if __name__ == '__main__':
    #_ext = Validate(app)
    #app.config['extn']=_ext
    #_ext.configure()
    app.run(port=82)