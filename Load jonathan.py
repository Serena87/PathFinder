# Loading the dataset

# Code from Canvas:
#load pandas, tool for data analysis in Python
import pandas as pd
from langdetect import detect

# read the file called 2022.json that is in the same directory and call it jobtech_dataset
jobtech_dataset = pd.read_csv('jobtech_dataset2022.csv')
# #show the variables names (columns) in the dataset
print(jobtech_dataset.columns)
#show the first 3 rows (job postings) in the dataset
print(jobtech_dataset.head(3))

jobtech_dataset.info()

# crop dataset to only wanted columns
dataframe = jobtech_dataset[['id', 'description', 'occupation', 'occupation_field', 'timestamp']] 

dataframe.info()

dfsvenska = pd.DataFrame(columns=dataframe.columns)

# iterate over the rows of the original dataframe
for index, row in dataframe.iterrows():
    # detect the language of the description column using the langdetect library
    if detect(row['description']) == 'sv':
        # if the language is Swedish, append the row to the new dataframe
        dfsvenska = dfsvenska.append(row, ignore_index=True)


print(dfsvenska.columns)
#show the first 3 rows (job postings) in the dataset
print(dfsvenska.head(3))
dfsvenska.info()