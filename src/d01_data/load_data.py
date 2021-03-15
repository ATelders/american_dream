import pandas as pd


# Import of the first database (from brentozar)
survey_filepath='./data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx'
survey_data = pd.read_excel(survey_filepath,  engine='openpyxl', skiprows=3)

# Import of the second database (from Kaggle)
glassdoor_filepath='./data/01_raw/DataAnalyst.csv'
glassdoor_data = pd.read_csv(glassdoor_filepath)

print(survey_data.head())
print(glassdoor_data.head())

# Select rows where country is United States

survey_data = survey_data[survey_data['Country'] == 'United States']

# Select useful rows 

survey_data = survey_data[
    [
        'Survey Year',
        'SalaryUSD',
        'PostalCode',
        'EmploymentStatus',
        'JobTitle',
        'YearsWithThisTypeOfJob',
        'HowManyCompanies',
        'OtherPeopleOnYourTeam',
        'Gender',
        'OtherJobDuties'
    ]
]

survey_data.to_csv("./data/02_intermediate/survey_data.csv")