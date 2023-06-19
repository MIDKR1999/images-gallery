import requests
import os
from dotenv import load_dotenv
from flask import Flask, request
# Frontend --request--> API service Flask --requests-> Unsplash API 

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL='https://api.unsplash.com/photos/random'
UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY", "")
DEBUG=bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and there UNSPLASH KEY")
app = Flask(__name__)

app.config["DEBUG"]=DEBUG

@app.route("/new-image")
def new_image():
    word=request.args.get("query")
    headers={
        "Accept-Version" : "v1",
        "Authorization" : "Client-ID " + UNSPLASH_KEY
        }
    
    params ={
        "query" : word
    }
    response=requests.get(url=UNSPLASH_URL,headers=headers,params=params)

    data=response.json()
    return data

    

if __name__ == "__main__":      #if main.py is called directly using python3 main.py, then name is set as __main__ and the app get exectued 
    app.run(host="0.0.0.0", port = 5050)
