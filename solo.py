from soloSensor.SoloSensor import SoloSensor
from mongoDB.myMongo import MyMongo
import datetime
import pprint

a = SoloSensor(18)
i = a.medir()
if i :
    status = "molhado"
else:
    status = "seco"
print(datetime.datetime.now())
print(status)

mymongo = MyMongo("estufa")
data = {"data_hora":datetime.datetime.now(), "solo":status}
_id = mymongo.add("solo",data)

