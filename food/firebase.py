import pyrebase

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
    print(key, value, list[value])
print(list)
