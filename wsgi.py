from flask import Flask
import subprocess

application = Flask(__name__)

@application.route("/")


def exe_cmd(c):
	p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	(o, e) = p.communicate()
	p_s = p.wait()
	return o, e, p_s

def pull_data():
	cmd="curl -k https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-17-5082.html"
	(output,err,p_status)=exe_cmd(cmd)
	if p_status == 0:
		#print output
		flag = 0
		buf = output.split("\n")
		
		for line in buf:
			if not (line.find('<results') == -1):
				flag = 1
			if (flag == 1 ) & (not (line.find('data=') == -1)):
				flag = 0
				# found the result data block
				dline= line.split("}")

				l_d = []
				for dlin in dline:
					# dl hs one row of the result
					dli = dlin.split("{")
					if ( len(dli) > 1):
						dl = dli[1].replace("&quot;","")
						#print dl
						# 
						elem = dl.split(",")
						
						d = {}
						for ele in elem:
							el=ele.split(":")
							d[el[0]]=el[1]
						l_d.append(d)
	return l_d


#############################################

print list_dic

def hello():
    list_dic=pull_data()
    return str(list_dic)

if __name__ == "__main__":
    application.run()