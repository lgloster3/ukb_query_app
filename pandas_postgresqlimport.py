import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

df = pd.read_csv('C:\\Users\\Logan\\Desktop\\GTMasters\\Spring2022\\ML_tutorials\\Data_Dictionary_Showcase.csv')
df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces


engine = create_engine('postgresql://postgres:Beta@localhost:5432/ukb_query_app')


df.to_sql("data_dictionary_showcase",
          engine,
          if_exists="append",  # Options are ‘fail’, ‘replace’, ‘append’, default ‘fail’
          index = False, # Do not output the index of the dataframe
          dtype = {'col1': sqlalchemy.types.NUMERIC,
                   'col2': sqlalchemy.types.String}) # Datatypes should be SQLAlchemy type

