from flask import Flask, url_for, render_template
from flask_pymongo import PyMongo
import json

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
        #print(i)
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

@app.route("/getAll")
def getAll():
    online_users = mongo.db.users.find()
    for i in online_users:
        x.append(i)
        print(i)








if __name__ == "__main__":
    app.run(debug=True)
    # app.run()


#source <desired-path>/bin/activate