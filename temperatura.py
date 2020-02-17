from DHT11.MyDHT11 import MyDHT11
from mongoDB.myMongo import MyMongo
import datetime
import pprint

a = MyDHT11(4)
b = a.get_dados()
temperatura = b.temperatura
humidade = b.humidade

print(temperatura,humidade)
mymongo = MyMongo("estufa")
data = {"data_hora":datetime.datetime.now(),"temperatura": temperatura, "humidade":humidade}
_id = mymongo.add("DHT",data)
print(_id)
add = mymongo.get_item("DHT",{"_id":_id})
pprint.pprint(add)
