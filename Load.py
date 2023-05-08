# Loading the dataset

# Code from Canvas:
#load pandas, tool for data analysis in Python
import pandas as pd
from langdetect import detect
# load nltk to detect stopwords
import nltk.corpus


replace_dict = {'OM TJÄNSTEN': ' ', 'ARBETSUPPGIFTER': ' ', 'VI SÖKER DIG SOM': ' ', 
                 'INFORMATION OM FÖRETAGET': ' ', "'" : '', 'text_formatted' : '',
                 'company_information' : '', 'needs' : '', 'requirements' : '', 
                 'conditions' : '', 'None' : '', '!': ' ', ':' : '', ',' : ''} 



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

df = pd.DataFrame(columns=dataframe.columns)

# iterate over the rows of the original dataframe
for index, row in dataframe.iterrows():
    # detect the language of the description column using the langdetect library
    if detect(row['description']) == 'sv':
        # if the language is Swedish, append the row to the new dataframe
        df = df.append(row, ignore_index=True)



# Välj kolumnen som du vill ändra och använd str-metoden slice för att ta bort de första 10 tecknen
df['description'] = df['description'].str.slice(start=10)
df['description'] = df['description'].str.replace('\\', 'KOWABUNGA')
df['description'] = df['description'].str.replace('KOWABUNGAn', ' ')
df['description'] = df['description'].replace(replace_dict, regex=True)

#Remove stop words from description column
stop_words = set(stopwords.words('swedish'))
df['description'] = df['description'].apply(lambda x: ' '.join([word for word in nltk.word_tokenize(x) if word.lower() not in stop_words]))


# Clean Occupation column
df['occupation'] = df['occupation'].str.slice(start=40)
df['occupation'] = df['occupation'].str.split("'", 2).str[1]

# Clean Occupation_field column
df['occupation_field'] = df['occupation_field'].str.slice(start=40)
df['occupation_field'] = df['occupation_field'].str.split("'", 2).str[1]

df['timestamp'] = df['timestamp'].str.slice(stop=-13)

print(df.columns)
#show the first 3 rows (job postings) in the dataset
print(df.head(3))
df.info()

# save the new dataframe to a CSV file
df.to_csv('datasetet.csv', index=False)