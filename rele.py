from reles.myRele import MyRele
from mongoDB.myMongo import MyMongo
import datetime
import pprint
import time

now = datetime.datetime.now()
print(now)
seishora = now.replace(hour=6,minute=0,second=0,microsecond=0)
print(seishora)
vinteduashora = now.replace(hour=22,minute=0,second=0,microsecond=0)
print(vinteduashora)
c = MyRele(17)
if  (now > seishora) and ( now < vinteduashora ) :
    c.on()
    print("on")
    status = True
else:
    c.off()
    print("off")
    status = False
mymongo = MyMongo("estufa")
data = {"data_hora":datetime.datetime.now(),"luz": status}
id = mymongo.add("luz",data)
#time.sleep(10)
#c.off()
