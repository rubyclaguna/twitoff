import os
import basilica
from dotenv import load_dotenv



load_dotenv()

basilica_api_key = os.getenv("basilica_api_key",default="OOPS")


def basilica_connection():
    connection = basilica.Connection(basilica_api_key)
    print(connection)
    return connection

if __name__ =="__main__":

    sentences = [
    "This is a sentence.", 
    "This is a similar sentence.", 
    "I don't think this sentence is very similar at all....",
]

connection = basilica_connection() 
