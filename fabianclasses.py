import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv('dfsvenska.csv')

# Define Swedish stop words
swedish_stopwords = stopwords.words('swedish')

# Convert descriptions to numerical features using CountVectorizer
vectorizer_desc = CountVectorizer(stop_words=swedish_stopwords)
X_desc = vectorizer_desc.fit_transform(df['description'])

# Count frequency of each occupation based on description
desc_counts = pd.Series(df['occupation'][X_desc.sum(axis=1).nonzero()[0]].values).value_counts()

# Convert occupation_field to numerical features using CountVectorizer
vectorizer_field = CountVectorizer(stop_words=swedish_stopwords)
X_field = vectorizer_field.fit_transform(df['occupation_field'])

# Count frequency of each occupation based on occupation_field
field_counts = pd.Series(df['occupation'][X_field.sum(axis=1).nonzero()[0]].values).value_counts()

# Count frequency of each occupation based on occupation
occ_counts = df['occupation'].value_counts()

# Combine counts from all three sources
total_counts = desc_counts.add(field_counts, fill_value=0).add(occ_counts, fill_value=0)

# Print most frequent occupations
print(total_counts.sort_values(ascending=False))

