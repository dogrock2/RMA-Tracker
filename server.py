from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('navbar.html', title="Home")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
