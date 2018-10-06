from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")

@app.route("/settings")
def settings():
    return render_template('settings.html', title="Settings")

@app.route("/register")
def registration():
    return render_template('register.html', title="Register")


    
if __name__ == "__main__":
    app.run(debug=True)
    # app.run()














#source <desired-path>/bin/activate