from flask import Flask
import subprocess

application = Flask(__name__)

@application.route("/")



def pull_data():
    output = subprocess.check_output(['curl','-H','Authorization: Bearer 8UoEBUYYqpfizZp-AnJtCFsCtAxSIUO9_xwFfF9A1as','https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-17-5082.html'])
		#print output
    return output


#############################################


def hello():
    o=pull_data()
    return o

if __name__ == "__main__":
    application.run()
