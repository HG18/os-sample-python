from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    str="Hello World from HG!"
    return str

if __name__ == "__main__":
    application.run()
