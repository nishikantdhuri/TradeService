from flask import Blueprint,render_template

resionA_bp = Blueprint('resionA_bp',__name__,url_prefix='/regiona')

@resionA_bp.app_template_filter()
def formatter(text):
    return text.upper()

@resionA_bp.route('/')
def index():
    title='region-A'
    return render_template('regiona.html',data=title)