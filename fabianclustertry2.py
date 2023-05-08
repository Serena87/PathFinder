import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('dfsvenska.csv', encoding='utf-8')

# Preprocess the data
df = df[['description', 'occupation']]
df = df.dropna() # Remove any rows with missing data
df = df.reset_index(drop=True) # Reset the index

# Define a custom stop words list for Swedish
swedish_stop_words = [
    'och', 'i', 'att', 'en', 'som', 'för', 'med', 'till', 'på', 'är',
    'av', 'om', 'den', 'de', 'vi', 'du', 'han', 'hon', 'det', 'så',
    'kan', 'men', 'hur', 'när', 'där', 'var', 'sig', 'ett', 'från',
    'ha', 'har', 'inte', 'eller', 'man', 'vid', 'blir', 'blev', 'gör',
    'gjort', 'gjorde', 'göra', 'ska', 'skall', 'samma', 'sådan', 'sådant',
    'sådana', 'din', 'ditt', 'mina', 'mitt', 'enligt', 'både', 'även',
    'första', 'genom', 'mellan', 'någon', 'något', 'några', 'sista',
    'under', 'utan', 'över', 'förra', 'fram', 'hela', 'närvarande',
    'sista', 'samma', 'samma', 'samma'
]

# Convert the job descriptions to a numerical representation
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words=swedish_stop_words)
job_descriptions = vectorizer.fit_transform(df['description'])

# Cluster the job descriptions using K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=42).fit(job_descriptions)
df['class'] = kmeans.labels_

# Calculate the frequency of each occupation in each class
occupation_frequency = df.groupby(['class', 'occupation']).size().reset_index(name='count')

# Plot the bar chart
sns.set_style('whitegrid')
g = sns.catplot(x='class', y='count', hue='occupation', data=occupation_frequency, kind='bar', height=8.27, aspect=11.7/8.27)
g.set_xlabels('Class')
g.set_ylabels('Frequency')
plt.show()
