from flask import Flask
from flask import render_template
import pandas as pd
import plotly.graph_objects as go
import plotly
import json
from data_wrangling import prepare_figures

app = Flask(__name__, template_folder='../frontend')

@app.route("/")
@app.route("/index")
def home():

    figures = prepare_figures()

    ids = [f"figures-{i}" for i, _ in enumerate(figures)]

    figures_JSON = json.dumps(figures, cls = plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", ids=ids, figuresJSON=figures_JSON)



if __name__ == "__main__":
    app.run(debug=True)