from ultrasonic import Ultrasonic
import mongoDB.myMongo 
import datetime
import pprint

a = Ultrasonic(23,24)
distancia = a.medir()
print(distancia)
mymongo = MyMongo("estufa")
data = {"data_hora":datetime.datetime.now(),"distancia": distancia}
_id = mymongo.add("ultrasonic",data)
print(_id)
add = mymongo.get_item("ultrasonic",{"_id":_id})
pprint.pprint(add)
