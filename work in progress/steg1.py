# STEG 1

# Loading the dataset

#load pandas, tool for data analysis in Python
import pandas as pd
import langdetect


# read the dataset that is in the same directory and call it jobtech_dataset
jobtech_dataset = pd.read_csv('jobtech2022columns2updated.csv')

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

for index, row in dataframe.iterrows():
    description = row['description']
    if description.strip():  # Skip if the description is empty or contains only whitespace
        try:
            lang = langdetect.detect(description)
            if lang == 'sv':
                # Add the Swedish text to the data frame
                df = df.append(row)
        except langdetect.lang_detect_exception.LangDetectException:
            # Handle the case when language detection fails
            pass



# save the new dataframe to a CSV file
df.to_csv('dataset2022UPDATEDsv2.csv', index=False)
print('new csv created. end of program.')