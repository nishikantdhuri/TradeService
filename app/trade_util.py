#from injector import inject
from app.PServiceRequest import PServiceRequest
from app.mongodb import mongoDB

class LazyLoadData:

    def __init__(self,function):
        self.function=function
        self.name=function.__name__

    def __get__(self, obj, owner):
        obj.__dict__[self.name]=self.function(obj)
        return obj.__dict__[self.name]

mongo=mongoDB()

class TradeUtil(object):

    __trade = None

    def __init__(self):
        if TradeUtil.__trade != None:
            raise ('singleton class')
        else:
            TradeUtil.__trade = self

    @staticmethod
    def getinstance():
        if TradeUtil.__trade == None:
            TradeUtil.__trade = TradeUtil()
        return TradeUtil.__trade

    #@LazyLoadData
    def get_all_trades(self):
        trades=mongo.getAllTrades()
        return trades

    def save_trade(self,trade):
        mongo.save_trade(trade)

    def process_trade(self,trade):
        psr=PServiceRequest(trade)
        return self.save_trade(vars(psr))

    def check_entitlement(self):
        return True

    def save_trade(self,trade):
        try:
            id=mongo.save_trade(trade)
        except Exception as ex:
            return '0'
        return id

