from flask import Blueprint,render_template,request
from app.utils import trade_util
from app.regionB.forms.regionb_form import REGIONBForm
regionB_bp = Blueprint('regionB_bp',__name__,url_prefix='/regionb')
from app import app
from app.utils.trade_util import TradeUtil
logger=app.config['logger']
trade_util=TradeUtil()
# from blinker import Namespace
# sig=Namespace()
# custom_signal=sig.signal('custom_signal')

# def log_template_renders(sender,template,context,**app):
#     sender.logger.debug(template.name)

# @custom_signal.connect
# def process_received(app,**args):
#     a=args.get('id')
#     pass

#template_rendered.connect(log_template_renders,app)

# @mliosa_bp.before_request
# def check_access():
#     if not trade_util.check_entitlement():
#         render_template('error.html')

@app.route('/')
def healthcheck():
    return 'runing'

@regionB_bp.route('/trade',methods=['POST','GET'])
def put_trade():
    form_data=REGIONBForm()
    if form_data.validate_on_submit():
        return 'True'
    return render_template('regionb_put_trade.html',form=form_data)

@regionB_bp.route('/error')
def no_access():
    return render_template('error.html')

@regionB_bp.app_template_filter()
def formattext(str1):
    return str(str1) + "formatted!!"

@regionB_bp.route('/getregionb',methods=['GET'])
def getmli():
    #custom_signal.send(current_app._get_current_object(),id=123)
    logger.info('fetching trades..')
    trades=trade_util.get_all_trades
    return render_template('regionb.html',data=trades)


# @mliosa_bp.route('/stream_data_slow')
# def stream_data():
#     def generate():
#         # create and return your data in small parts here
#         for i in range(10000):
#             yield str(i)
#
#     return Response(stream_with_context(generate()))
#
# @mliosa_bp.route('/stream_data_1')
# def stream_data_1():
#     def generate():
#         # create and return your data in small parts here
#         a=[]
#         for i in range(10000):
#             a.append(str(i))
#         return a
#
#     return Response(stream_with_context(generate()))

# @mliosa_bp.route('/Inventory',methods=('GET','POST'))
# def get_trade():
#     form=OSAForm()
#     if form.validate_on_submit():
#         return "Done"
#     else:
#         return render_template('inventory.html',form=form)


@regionB_bp.route('/get/<id>')
def getId(id):
    print(request.view_args)
    return str(id)
