from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    str1 = "Hello World from HG!"
    return str1

if __name__ == "__main__":
    application.run()
