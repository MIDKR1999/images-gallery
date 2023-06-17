from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":      #if main.py is called directly using python3 main.py, then name is set as __main__ and the app get exectued 
    app.run(host="0.0.0.0", port = 5050)
