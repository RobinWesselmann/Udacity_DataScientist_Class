import json
import plotly
import pandas as pd

from flask import Flask
from flask import render_template, request, jsonify
import joblib
import sys
from prepare_figures import prepare_figures

sys.path.append("../models")

from sqlalchemy import create_engine


app = Flask(__name__, template_folder='./template')

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql("SELECT * FROM disaster_reponse_tbl", con = engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    #prepare figures
    figs = prepare_figures(df)

    # encode plotly graphs in JSON
    ids = [f"figures-{i}" for i, _ in enumerate(figs)]

    print(ids)

    graphJSON = json.dumps(figs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template('visualizations.html', ids=ids, figuresJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


@app.route('/text_classification_app')
def classifier_app():
    
    # render web page with plotly graphs
    return render_template('classifier_app.html') 


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()