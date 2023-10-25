from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')

# Create a database called 'vue-chatbot'
db = client['vue-chatbot']