import pyrebase
from .models import Food


def updateSQL():
  config = {
    "apiKey": "AIzaSyDKQKHxU3YQQXwFsWFTdycplvnMuUnN4yc",
    "authDomain": "foodbuddy-1a5de.firebaseapp.com",
    "databaseURL": "https://foodbuddy-1a5de.firebaseio.com",
    "projectId": "foodbuddy-1a5de",
    "storageBucket": "foodbuddy-1a5de.appspot.com",
    "messagingSenderId": "337190624102",
    "appId": "1:337190624102:web:bd0a1a49c92cad5a1b46a7",
    "measurementId": "G-RYYWLY1VBY"
  }
  
  firebase = pyrebase.initialize_app(config)
  
  db = firebase.database()
  list = db.get().val()
  
  for key, value in enumerate(list):
    foodObject = Food(food_name=list[value]["item"],
                      food_amount=list[value]["amount"],
                      date=list[value]["date"])
    print(foodObject.date)
    foodObject.food_amount = foodObject.food_amount.split(" ", 1)[0]
    date = foodObject.date.split("/")
    foodObject.date = f"{date[2]}-{date[0]}-{date[1]}"
  
    fod = Food.objects.filter(food_name=foodObject.food_name, food_amount=foodObject.food_amount, date=foodObject.date)
    if (len(fod) == 0):
      FoodItem = Food(food_name=foodObject.food_name, food_amount=foodObject.food_amount, date=foodObject.date)
      FoodItem.save()
  
  print(list)
  
  allFoods = Food.objects.all()
  return allFoods
