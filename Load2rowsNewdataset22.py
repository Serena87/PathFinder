# Loading the dataset

# Code from Canvas:
#load pandas, tool for data analysis in Python
import pandas as pd
from langdetect import detect
# load nltk to detect stopwords
from nltk.corpus import stopwords
from nltk import word_tokenize


replace_dict = {'OM TJÄNSTEN': ' ', 'ARBETSUPPGIFTER': ' ', 'VI SÖKER DIG SOM': ' ', 
                 'INFORMATION OM FÖRETAGET': ' '} 


# read the dataset that is in the same directory and call it jobtech_dataset
#jobtech_dataset = pd.read_csv('jobtech2022columns2updated.csv')
jobtech_dataset = pd.read_csv('/Users/jon/Documents/GitHub/PathFinder/work in progress/jobtech2022columns2updated.csv')

# Specify the desired data types for the columns
data_types = {'description': str, 'occupation': str}

# Convert the columns to the desired data types
jobtech_dataset = jobtech_dataset.astype(data_types)

# #show the variables names (columns) in the dataset
print(jobtech_dataset.columns)
#show the first 3 rows (job postings) in the dataset
print(jobtech_dataset.head(3))

#jobtech_dataset.info()
dataframe = jobtech_dataset

df = pd.DataFrame(columns=dataframe.columns)

print('detecting swedish ads..')

"""
# iterate over the rows of the original dataframe
for index, row in dataframe.iterrows():
    # detect the language of the description column using the langdetect library
    if detect(row['description']) == 'sv':
        # if the language is Swedish, append the row to the new dataframe
        df = df.append(row, ignore_index=True)
        """


# iterate over each row in the DataFrame
for index, row in jobtech_dataset.iterrows():
    # check if the 'description' value is a string or can be converted to a string
    if isinstance(row['description'], str):
        # perform language detection
        if detect(row['description']) == 'sv':
            # add row to new dataset if Swedish
            df = df.append(row, ignore_index=True)
    else:
        # handle cases where 'description' is not a string
        # e.g., you can choose to skip or handle these rows differently
        print("Skipped row:", index)



# cleaning the column description
print('cleaning description column..')

df['description'] = df['description'].replace(replace_dict, regex=True)

#Remove stop words from description column
print('removing stopwords..')
stop_words = set(stopwords.words('swedish'))
df['description'] = df['description'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word.lower() not in stop_words]))



'''
print(df.columns)
#show the first 3 rows (job postings) in the dataset
print(df.head(3))
df.info()'''

# loop through each unique occupation and find the corresponding description(s)
print('finding unique occupations..')
occupations = df['occupation'].unique()
occupation_descriptions = []
for occupation in occupations:
    description = ""
    for index, row in df.iterrows():
        if row['occupation'] == occupation:
            description += row['description'] + " "
    occupation_descriptions.append(description.strip())

# create a new dataframe with the occupations and descriptions
new_df = pd.DataFrame({'occupation': occupations, 'description': occupation_descriptions})

# print the new dataframe
#print(new_df)

# save the new dataframe to a CSV file
new_df.to_csv('dataset2022UPDATED.csv', index=False)
print('new csv created. end of program.')