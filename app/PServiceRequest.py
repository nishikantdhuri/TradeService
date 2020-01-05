from app.BasePsr import BasePSR
import uuid

class PropertyLoader:
    def __init__(self,name):
        self.name=name

    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name]=value

class PServiceRequest(BasePSR):

    def __init__(self,trade):
        self.id=uuid.uuid1()
        # self.trade_user=trade['trade_user']
        # self.trade_name = trade['trade_name']
        # self.trade_quantity = trade['trade_quantity']
        # self.exchange = trade['exchanges']
        self.source=trade['exchanges']
        self.account=trade['trade_name']
        self.tdate='11-11-2020'
        self.user=trade['trade_user']
        self.amount=trade['trade_quantity']
        self.entity=trade['trade_name']
        self.sdate='11-11-2020'

    # @property
    # def Id(self):
    #     return self._id
    #
    # @Id.setter
    # def Id(self,val):
    #     self._id=val
    #
    # def calculate_deal(self,amout):
    #     return amout
