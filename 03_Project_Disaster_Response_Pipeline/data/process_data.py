import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """Load the messages and categories under the given filepath,
    concatenate messages and categories and output the result.

    Args:
        messages_filepath (str): filepath for the message dataset (csv)
        categories_filepath (str): filepath for the category dataset (csv)
    """
    df_msg = pd.read_csv(messages_filepath)
    df_cat = pd.read_csv(categories_filepath)
    df_ = pd.concat([df_msg, df_cat.drop("id", axis = 1)], axis = 1)
    return df_

def clean_data(df):
    """Splits the categories column into separate, clearly named columns
      converts values to binary, and drops duplicates.

    Args:
        df (pd.DataFrame): messages and categories data
    """
    
    #expand the categories column 
    df_categories = df["categories"].str.split(";", expand = True)
    col_names = [col.split("-")[0] for col in df_categories.iloc[0]]
    df_categories.columns = col_names

    for col in df_categories:
        df_categories[col] = df_categories[col].str.split("-").str[1]

    #transform to binary 
    df_categories = df_categories.astype("int")
    
    #drop categories column from df
    df = df.drop("categories", axis = 1)

    #combine expanded df_categories & msg data (df)
    df_expanded = pd.concat([df, df_categories], axis = 1)

    #drop related = 2 and duplicates
    df_clean= df_expanded.drop_duplicates()
    df_clean = df_clean.drop(df_clean[df_clean["related"] == 2].index, axis = 0)

    return df_clean


def save_data(df, database_filename):
    """Saves the given dataframe in the table 'disaster_response_tbl' in the Database 
    under the provided filepath / filename or creates (if not existant) a new database with this table under the 
    given filepath

    Args:
        df (pandas.DataFrame): dataframe containing the cleaned data
        database_filename (str): filepath of the database
    """
    engine = create_engine(f'sqlite:///{database_filename}') #'sqlite:///InsertDatabaseName.db'
    df.to_sql('disaster_reponse_tbl', engine, index=False, if_exists = "replace")  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()