from pymongo import MongoClient


class MongoConnection(object):

    def connect(self):
        if hasattr(self,'mongo')and self.mongo is not None:
            return self.mongo
        else:
           client=MongoClient('mongodb://172.17.0.2:27017/')
           self.mongo =client["test"]
           return self.mongo


class mongoDB(object):

    def __init__(self):
        self.mongo=MongoConnection().connect()

    def getAllTrades(self):
        tradesc=(self.mongo["test"]).find()
        trades=[]
        for i in tradesc:
            trades.append(i)
        return trades


    def save_trade(self,trade):
        id=(self.mongo["test"]).insert_one(trade)
        return str(id.inserted_id)


