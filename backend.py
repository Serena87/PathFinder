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
#Skickar ord att fylla bubblorna med till frontend
lista = ['Noggran', 'Kreativ', 'Djur', 'Körkort', 'Positiv', 'Människor', 'Mat', 'Hållbarhet', 'Vårdande', 'Social', 'Försäljning']
lista2 = ['Organiserad', 'Självgående', 'Samarbetande', 'Analytisk', 'Resultatinriktad', 'Uthållig', 'Kreativ', 'Kommunikativ', 'Flexibel', 'Kundorienterad', 'Teamplayer', 'Kundservice', 'Försäljning', 'Marknadsföring', 'Projektledning', 'Strategisk', 'Lösningsorienterad', 'Ansvarsfull', 'Driven', 'Tidsplanering', 'Affärsutveckling', 'Budgetansvarig', 'Ledarskap', 'Utveckling', 'Utbildning', 'Forskning', 'Hållbarhet', 'Produktutveckling', 'Kvalitetssäkring', 'Teknik', 'Administration', 'Ekonomi', 'Kvalitet', 'Resor', 'IT', 'Design', 'Hälso- och sjukvård', 'Juridik', 'Logistik', 'Inköp', 'Projektstyrning', 'Human resources', 'Rekrytering', 'Affärssystem', 'Affärsmannaskap', 'Operativt arbete', 'Skatt', 'Redovisning', 'Konflikthantering', 'Entreprenörskap']

def get_words():
    return(lista2)

## Takes x amount of words, returns 5 suitable occupations. Used by frontend. 

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_occupation2(word1, word2, word3, word4, word5):
    # Load occupation data
    print('Reading dataset...')
    df = pd.read_csv('clean_occup.csv')
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

print(get_occupation2('ledarskap', 'utveckling', 'utbildning', 'forskning', ''))





## Ny extract_common_words
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import nltk
from nltk.corpus import stopwords
import random

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_common_words(dataset_file):
    # Load the dataset
    df = pd.read_csv(dataset_file)

    # Tokenize the descriptions
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    df['tokens'] = df['description'].apply(lambda x: tokenizer.tokenize(x.lower()))

    # Remove stop words
    stop_words = stopwords.words('swedish')
    df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

    # Join tokenized words into a single string
    df['tokens'] = df['tokens'].apply(lambda x: ' '.join(x))

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer on the tokenized descriptions
    X = vectorizer.fit_transform(df['tokens'])

    # Get the feature names (words) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()

    # Convert feature_names to a list
    feature_names = list(feature_names)

    # Extract 50 random but common words
    common_words = random.sample(feature_names, 50)

    return common_words

# Usage
def fetch_common_words(): 
    common_words = extract_common_words('clean_occup.csv')
    print(common_words)
    return common_words

fetch_common_words()


## AI word extract COMMON WORDS 2

import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import random

def extract_common_words(dataset_file, num_common_words=50):
    # Load the dataset
    try:
        df = pd.read_csv(dataset_file)
    except FileNotFoundError:
        raise FileNotFoundError("Dataset file not found.")

    # Tokenize the descriptions
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    df['tokens'] = df['description'].apply(lambda x: tokenizer.tokenize(x.lower()))

    # Remove stop words
    stop_words = stopwords.words('swedish') + ['custom', 'stop', 'words']  # Add any additional stop words here
    df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

    # Join tokenized words into a single string
    df['tokens'] = df['tokens'].apply(lambda x: ' '.join(x))

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer on the tokenized descriptions
    X = vectorizer.fit_transform(df['tokens'])

    # Get the feature names (words) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()

    # Convert feature_names to a list
    feature_names = list(feature_names)

    # Extract top N most common words based on TF-IDF scores
    word_scores = zip(feature_names, X.sum(axis=0).tolist()[0])
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
    common_words = [word for word, _ in sorted_words[:num_common_words]]

    return common_words


print('---------')
print('---------')
print('---------')
print('---------')

# Example usage
common_words = extract_common_words("clean_occup.csv", num_common_words=50)
print(common_words)
