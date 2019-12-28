from app.models.BasePsr import BasePSR

class PropertyLoader:
    def __init__(self,name):
        self.name=name

    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name]=value

class PServiceRequest(BasePSR):

    def __init__(self,trade):
        self._id=None
        self.source=None
        self.account=None
        self.tdate=None
        self.user=None
        self.amount=None
        self.entity=None
        self.sdate=None

    @property
    def Id(self):
        return self._id

    @Id.setter
    def Id(self,val):
        self._id=val

    def calculate_deal(self,amout):
        return amout
