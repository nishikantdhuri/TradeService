from flask import Flask
import logging
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
app=Flask(__name__)
app.debug=True
cs=CSRFProtect()
cs.init_app(app)
lm=LoginManager()
lm.init_app(app)
#logging.basicConfig(filename=__name__,format='%(process)d-%(levelname)s-%(message)s',level=logging.DEBUG)
logger=logging.getLogger(__name__)
app.config['logger']=logger


app.config["MONGO_URI"] = "mongodb://localhost:27017/plexus"
logging.basicConfig(filename='log.log',level=logging.DEBUG)
app.config.from_object('config')
from app.trade_controller import trade_bp
app.register_blueprint(trade_bp)
from app.mongodb import mongoDB

toolbar=DebugToolbarExtension(app)
toolbar.init_app(app)

# @app.before_first_request
# def beforefirstre():
#     app.logger.info('begin')
#
# @app.after_request
# def afterrequest(resp):
#     app.logger.info(resp)
#     return resp
#
# def badrequest(e):
#     return 'badrequest'
#
# app.register_error_handler(404,badrequest)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def index():
#     return render_template('base/template/index.html')

