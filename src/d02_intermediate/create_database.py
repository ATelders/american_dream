import sqlite3
import pandas as pd

DB_NAME = 'data_salaries.db'

con = sqlite3.connect(DB_NAME)
cur = con.cursor()
cur.execute('pragma encoding=UTF8')

survey_filepath='./data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx'
survey_data = pd.read_excel(survey_filepath, engine='openpyxl', skiprows=3)

glassdoor_filepath='./data/01_raw/DataAnalyst.csv'
glassdoor_data = pd.read_csv(glassdoor_filepath)





survey_data.to_sql(
    name="survey_dataset",
    con=con,
    index=False,
    if_exists='replace',
    chunksize=500
)





con.commit

con.close

