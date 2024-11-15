# import libraries
import sys
import pandas as pd 
import numpy as np
from sqlalchemy import create_engine 

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import re
from utils import tokenize

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report

import pickle
import warnings
warnings.filterwarnings("ignore")

def load_data(database_filepath):
    """Load the relevant data from the database in the given filepath

    Args:
        database_filepath (str): database filepath
    """
    #read data from db
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql("SELECT * FROM disaster_reponse_tbl", con = engine)

    #initially clean data concerning basic topics
    df.drop("child_alone", axis = 1, inplace=True)
    df["related"] = df["related"].map(lambda x: 1 if x==2 else x)
    df["direct_report"] = df["direct_report"].map(lambda x: 1 if x==2 else x)

    X = df["message"]
    y = df[df.columns[4:]].astype("int")

    return X, y, y.columns.tolist()

def build_model(clf = AdaBoostClassifier(algorithm = "SAMME")):
    """Build a pipeline containing CountVectorizer incl. tokenizer, TfidfTransformer, classifier

    Args:
        clf (model): Prediction model

    Returns:
        pipeline: sklearn.pipeline.Pipeline
    """

    pipeline = Pipeline([
        ("features", FeatureUnion([
            ("text_pipeline", Pipeline([
                ("vect", CountVectorizer(tokenizer=tokenize, token_pattern=None)),
                ("tfidf", TfidfTransformer())
            ]))
        ],n_jobs=-1)),
        ("clf", MultiOutputClassifier(estimator = clf,n_jobs=-1))
    ])

    parameters = {
        'clf__estimator__learning_rate':[0.5, 1.0],
        'clf__estimator__n_estimators':[10,20]
    }

    cv = GridSearchCV(estimator=pipeline, param_grid=parameters, cv=5, n_jobs = -1, verbose = 3)

    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    """Evaluate the model and print out the sklearn classification_report

    Args:
        model (variable): Prediction model to evaluate
        X_test (pandas.Series):  Messages
        Y_test (pandas.DataFrame): Categories
        category_names (list): Category names
    """
    
    y_pred_test = model.predict(X_test)
    print(classification_report(Y_test.values, y_pred_test, target_names=category_names))

def save_model(model, model_filepath):
    """Save the trained model

    Args:
        model (variable): Prediction model to evaluate
        model_filepath (str): path to save the model
    """
    
    with open(model_filepath, 'wb') as f:
        pickle.dump(model, f)

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))

        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')
    

if __name__ == '__main__':
    main()