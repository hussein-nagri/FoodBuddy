import pymongo
from datetime import datetime
client = pymongo.MongoClient("mongodb+srv://root:root@stillgood-chx3k.gcp.mongodb.net/test?retryWrites=true&w=majority")

def loadFridge():

    db = client.fridge

    allFoods = []
    for food in db.foodItems.find():
        food['id'] = food.pop('_id')
        print(food)

        allFoods.append(food)
    # allFoods = db.foodItems.find()
    return allFoods
# loadFridge()


# print ( client.list_database_names() )


