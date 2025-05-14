
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://johnwillymarandu:marandu1990@pymongo1.vp4e8ev.mongodb.net/?retryWrites=true&w=majority&appName=Pymongo1"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.farm

farmcollection = db['Users']
#farmcollection2 = db['products']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)