import pymongo
import ssl

client = pymongo.MongoClient(
    "mongodb+srv://ArnavShah:arnavshah@cluster0.sgw7j.mongodb.net/thermapal?retryWrites=true&w=majority", ssl=True,
    ssl_cert_reqs=ssl.CERT_NONE)
db = client["thermapal"]
collection = db["temperature"]


def insert(mac, temperature):
    post = {"_id": mac, "temperature": temperature}
    collection.insert_one(post)

