from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')

def get_games():
   client = MongoClient(CONNECTION_STRING)
   return client['scores']
  
def get_players():
   client = MongoClient(CONNECTION_STRING)
   return client['players']