from pymongo import MongoClient
def get_games():

   CONNECTION_STRING = "mongodb+srv://spb:5.aM%404MWgM4SX4S@scoredata.qtuwpvy.mongodb.net/?retryWrites=true&w=majority&appName=ScoreData"
   client = MongoClient(CONNECTION_STRING)
   return client['scores']
  
def get_players():
   CONNECTION_STRING = "mongodb+srv://spb:5.aM%404MWgM4SX4S@scoredata.qtuwpvy.mongodb.net/?retryWrites=true&w=majority&appName=ScoreData"
   client = MongoClient(CONNECTION_STRING)
   return client['players']