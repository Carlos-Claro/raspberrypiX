from myMongo import MyMongo
import pprint
import datetime

mymongo = MyMongo("estufa")
d = datetime.datetime(2018,3,19,19,00)
for post in mymongo.get_itens("ultrasonic",{"data_hora":{"$gte":d},"distancia":{"$gte":0}}):
    pprint.pprint(post)
