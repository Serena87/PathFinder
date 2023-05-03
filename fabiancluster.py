from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the dataset
df = pd.read_csv('dfsvenska.csv', encoding='utf-8')

# Preprocess the data
df = df[['description', 'occupation']]
df = df.dropna() # Remove any rows with missing data
df = df.reset_index(drop=True) # Reset the index

# Convert the job descriptions to a numerical representation
vectorizer = TfidfVectorizer(stop_words='swedish')
job_descriptions = vectorizer.fit_transform(df['description'])

# Train the k-means clustering model
k = 5 # number of clusters
kmeans = KMeans(n_clusters=k, random_state=42).fit(job_descriptions)

# Get the cluster labels for each job title
labels = kmeans.labels_

# Add the cluster labels to the original dataset
df['cluster'] = labels

# Print the occupations in each cluster
for i in range(k):
    print(f'Cluster {i}:')
    print(df[df['cluster'] == i]['occupation'].unique())
