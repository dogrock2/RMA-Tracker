from flask import Flask, url_for, render_template, request
from flask_pymongo import PyMongo
import json
import bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    online_users = mongo.db.rma_records.find()
    x = []
    for i in online_users:
        x.append(i)
    return render_template('home.html', title="Home", setActive1='active', results=x)

@app.route("/settings")
def settings():
    return render_template('settings.html', title="Settings", setActive2='active')

@app.route("/register")
def registration():
    return render_template('register.html', title="Register", setActive3='active')

@app.route("/modify")
def modify():
    return render_template('modify.html', title="Register", setActive4='active')

@app.route("/verifyLogin", methods=['POST'])
def verifyLogin():
    credInput = request.get_json()
    pwd = credInput["inputPwd"]
    result = mongo.db.users.find_one({"userName":credInput["inputUser"]})
    if result == None:
        return("User not found")
    else:
        hashed = result["regInputPassword"]
        if bcrypt.hashpw(pwd, hashed) == hashed:
            print("Matches")
            return "success"
        else:
            return("Password does not match")
        

@app.route("/addRegistration", methods=['POST'])
def addRegistration():
    valInput = request.get_json()      
    dupOK = verifyDuplicates(valInput["userName"], valInput["inputEmail"])    
    if dupOK == 0:
        inputPwd = valInput["regInputPassword"]
        valInput["regInputPassword"] = encode_pwd(inputPwd)
        mongo.db.users.insert_one(valInput)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    elif dupOK == 1:
        return "Username Duplicate"
    else:
        return "Email Duplicate"
        

def verifyDuplicates(usr, email):
    stat = 0   
    for x in mongo.db.users.find({"userName":usr}):
        stat = 1
        return stat
    for y in mongo.db.users.find({"inputEmail":email}):
        stat = 2
        return stat
    return stat 

def encode_pwd(inputPwd):  
    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(inputPwd, salt)
    return hashed





if __name__ == "__main__":
    app.run(debug=True)
    # app.run()


#source <desired-path>/bin/activate



#return json.dumps({'success':False}), 400, {'ContentType':'application/json'}