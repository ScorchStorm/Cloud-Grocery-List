"grocery-list-b15ef"
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# access database
print('accessing database')
cred = credentials.Certificate("C:/Users/Matthew/OneDrive/Documents/BYU-I Winter Semester 2025 Files/Applied Programming/grocery-list-b15ef-firebase-adminsdk-fbsvc-531453ba67.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# add data
print('adding data')
pizza = db.collection("grocery-list-collection").document("pizza")
pizza.set({"name": "Party Pizza", "aisle": 3, "company": "Tonito's", "price": 1.97,})
beef_jerky = db.collection("grocery-list-collection").document("beef_jerky")
beef_jerky.set({"name": "Real Beef Jerky", "aisle": 23, "company": "Robertson's", "price": 29.99,})
burritos = db.collection("grocery-list-collection").document("burritos")
burritos.set({"name": "Beef and Bean Green Chili Burritos", "aisle": 3, "company": "El Monterey", "price": 4.98,})
milk = db.collection("grocery-list-collection").document("milk")
milk.set({"name": "Half Gallon Reduced Fat 2% Milk", "aisle": 28, "company": "Great Value", "price": 1.92,})

# read data
print('reading data')
grocery_ref = db.collection("grocery-list-collection")
docs = grocery_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# delete data
print('deleting data')
pizza.delete()
beef_jerky.delete()
burritos.delete()
milk.delete()

# read data again
print('reading data again')
grocery_ref = db.collection("grocery-list-collection")
docs = grocery_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")