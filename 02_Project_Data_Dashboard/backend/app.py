from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='../frontend')

@app.route("/")
@app.route("/index")
def home():

    return render_template("index.html")

@app.route("/Descriptive_Analysis")
def decriptive_analysis():
    return render_template("Descriptive_Analysis.html")

@app.route("/About")
def about():
    return render_template("About.html")



if __name__ == "__main__":
    app.run(debug=True)