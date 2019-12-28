from flask import _app_ctx_stack,current_app,_request_ctx_stack

class Validate(object):
    def __init__(self,app):
        self.app=app
        if app != None:
            self.init_app(app)

    def validate(self,trade):
        ctx=_app_ctx_stack.top
        req=_request_ctx_stack.top
        _request_ctx_stack.pop()
        if trade > 200:
            return False
        return True
        # if hasattr('id',trade) and trade.id > 200000:
        #     return False,'invalid id'
        # return True,''

    def init_app(self,app):
        app.teardown_appcontext(self.tear_down)


    def tear_down(self):
        ctx= _app_ctx_stack.top
        ctx.validate_id=0

    @property
    def configure(self):
        ctx=_app_ctx_stack.top
        if ctx != None:
            if not hasattr('validate_id',ctx):
                ctx.validate_id=1
            return ctx.validate_id





