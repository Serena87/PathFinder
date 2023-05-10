# HEJ Front-end!!
# Ropa på get_words för en lista på 50 ord skapad av en människa
# Ropa på extract_common_words för en lista av 50 ord skapat av en algoritm :D
# Ropa på get_occupation2 och skicka in upp till 5 ord och få tillbaka en lista på 5 yrken
# 3-5 ord fungerar bäst. Om ni skickar färre än 5, skicka med tomma strängar för resterande ord t.ex 
# Get_occupation('hjälpsam', 'noggrann', 'ledning', '', '')
# Ni får snabbt tillbaka en lista på 5 occupations som passar
# Varma hälsningar



import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Skickar ord att fylla bubblorna med till frontend
lista2 = ['Organiserad', 'Självgående', 'Samarbetande', 'Analytisk', 'Resultatinriktad', 'Uthållig', 'Kreativ', 'Kommunikativ', 'Flexibel', 'Kundorienterad', 'Teamplayer', 'Kundservice', 'Försäljning', 'Marknadsföring', 'Projektledning', 'Strategisk', 'Lösningsorienterad', 'Ansvarsfull', 'Driven', 'Tidsplanering', 'Affärsutveckling', 'Budgetansvarig', 'Ledarskap', 'Utveckling', 'Utbildning', 'Forskning', 'Hållbarhet', 'Produktutveckling', 'Kvalitetssäkring', 'Teknik', 'Administration', 'Ekonomi', 'Kvalitet', 'Resor', 'IT', 'Design', 'Hälso- och sjukvård', 'Juridik', 'Logistik', 'Inköp', 'Projektstyrning', 'Human resources', 'Rekrytering', 'Affärssystem', 'Affärsmannaskap', 'Operativt arbete', 'Skatt', 'Redovisning', 'Konflikthantering', 'Entreprenörskap']
lista3 = ['Kompetent', 'Pålitlig', 'Ansvarsfull', 'Effektiv', 'Flexibel', 'Engagerad', 'Initiativrik', 'Kreativ', 'Organiserad', 'Kommunikativ', 'Samarbetande', 'Problemlösare', 'Självgående', 'Analytisk', 'Flexibel', 'Ambitiös', 'Resultatorienterad', 'Innovativ', 'Strukturerad', 'Tidsmedveten', 'Utåtriktad', 'Målinriktad', 'Lösningsfokuserad', 'Lyhörd', 'Anpassningsbar', 'Pålitlig', 'Uthållig', 'Uppfinningsrik', 'Kundorienterad', 'Teamorienterad', 'Empatisk', 'Beslutsam', 'Självsäker', 'Proaktiv', 'Kvalitetsmedveten', 'Diplomatisk', 'Initiativtagande', 'Driven', 'Flexibel', 'Analytisk', 'Resultatorienterad', 'Innovativ', 'Kreativ', 'Kommunikativ', 'Effektiv', 'Ansvarstagande', 'Pålitlig', 'Samarbetsvillig', 'Serviceinriktad', 'Lösningsorienterad']

def get_words():
    return(lista3)

## Takes x amount of words, returns 5 suitable occupations. Used by frontend. 


def get_occupation2(word1, word2, word3, word4, word5):
    # Load occupation data
    print('Reading dataset...')
    df = pd.read_csv('dataset2022.csv')
    print('dataset read!')

    # Preprocess occupation descriptions. Puts words into vectors for each  
    tfidf = TfidfVectorizer()
    description_vectors = tfidf.fit_transform(df['description'].fillna(''))
    print('preprocessed occupation descriptions! Vectors cretead')

    # Create input vector by transforming a string containing three words (word1, word2, and word3) 
    # using the same TfidfVectorizer instance. The resulting vector is stored in a variable called "input_vector".
    input_vector = tfidf.transform([' '.join([word1, word2, word3, word4, word5])])
    print('Input vector created')

    # Compute cosine similarity (similarity between two vectors) between input vector and occupation description vectors
    similarity_scores = cosine_similarity(input_vector, description_vectors)

    print('Similarity between input vector, description vector compared')
    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores, axis=1)[:, -5:].squeeze()[::-1]
    return df.iloc[top_occupations]['occupation'].tolist()


print(get_occupation2('säkerhet', 'människor', 'social', 'utåtriktad', 'vakt'))

## AI word extract COMMON WORDS 2

# fungerar verkligen inte bra än

#HÄR KOMMER MIN KOD SE NEDAN

# it will take the input words, predict the job occupations, 
# filter the jobs dataset based on the predicted occupations, 
# and return the top 5 matching job occupations.


import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the job dataset
jobs = pd.read_csv('dataset2022.csv')

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Convert the job descriptions into a matrix of numerical features
X = vectorizer.fit_transform(jobs['description'])

# Create a Multinomial Naive Bayes classifier object
clf = MultinomialNB()

# Train the classifier using the numerical features and the job occupations
clf.fit(X, jobs['occupation'])

def classify_job(word1, word2, word3):
    # Convert the input words into a numerical feature matrix
    input_words = [word1, word2, word3]
    input_features = vectorizer.transform(input_words)

    # Predict the job occupation based on the input features
    predicted_occupations = clf.predict(input_features)

    # Filter the jobs dataset based on the predicted occupations
    matches = jobs[jobs['occupation'].isin(predicted_occupations)]

    # Return the top 5 matching job occupations
    top_matches = matches['occupation'].value_counts().head(5).index.tolist()

    return top_matches

matching_jobs = classify_job('säkerhet', 'människor', 'social')
print(matching_jobs)