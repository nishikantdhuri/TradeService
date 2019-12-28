from pymongo import MongoClient
from app import app

class MongoConnection(object):

    def connect(self):
        if hasattr(self,'mongo')and self.mongo is not None:
            return self.mongo
        else:
           client=MongoClient('mongodb://localhost:27017/')
           self.mongo =client["tradem"]
           return self.mongo


class mongoDB(object):

    def __init__(self):
        self.mongo=MongoConnection().connect()

    def getAllTrades(self):
        tradesc=(self.mongo["tradem_data"]).find()
        trades=[]
        for i in tradesc:
            trades.append(i)
        return trades


    def save_trade(self,trade):
        self.mongo
        id=(self.mongo["tradem_data"]).insert_one(trade)
        pass


