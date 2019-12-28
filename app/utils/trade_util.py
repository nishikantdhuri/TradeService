#from injector import inject
from app.models.PServiceRequest import PServiceRequest
from app.repository.mongodb import mongoDB

class LazyLoadData:

    def __init__(self,function):
        self.function=function
        self.name=function.__name__

    def __get__(self, obj, owner):
        obj.__dict__[self.name]=self.function(obj)
        return obj.__dict__[self.name]

mongo=mongoDB()

class TradeUtil:

    @LazyLoadData
    def get_all_trades(self):
        trades=mongo.getAllTrades()
        return trades

    def save_trade(self,trade):
        mongo.save_trade(trade)

    def process_trade(self,msg):
        psr=PServiceRequest(msg)
        self.save_trade(vars(psr))

    def check_entitlement(self):
        return True

