# HEJ Front-end!!
# Ropa på get_words för en lista på 50 ord skapad av en människa
# Ropa på extract_common_words för en lista av 50 ord skapat av en algoritm :D
# Ropa på get_occupation och get_occupation2 och skicka in 3 ord och få tillbaka en lista på 5 yrken
# Varma hälsningar



import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
#Skickar ord att fylla bubblorna med till frontend
lista = ['Noggran', 'Kreativ', 'Djur', 'Körkort', 'Positiv', 'Människor', 'Mat', 'Hållbarhet', 'Vårdande', 'Social', 'Försäljning']
lista2 = ['Organiserad', 'Självgående', 'Samarbetande', 'Analytisk', 'Resultatinriktad', 'Uthållig', 'Kreativ', 'Kommunikativ', 'Flexibel', 'Kundorienterad', 'Teamplayer', 'Kundservice', 'Försäljning', 'Marknadsföring', 'Projektledning', 'Strategisk', 'Lösningsorienterad', 'Ansvarsfull', 'Driven', 'Tidsplanering', 'Affärsutveckling', 'Budgetansvarig', 'Ledarskap', 'Utveckling', 'Utbildning', 'Forskning', 'Hållbarhet', 'Produktutveckling', 'Kvalitetssäkring', 'Teknik', 'Administration', 'Ekonomi', 'Kvalitet', 'Resor', 'IT', 'Design', 'Hälso- och sjukvård', 'Juridik', 'Logistik', 'Inköp', 'Projektstyrning', 'Human resources', 'Rekrytering', 'Affärssystem', 'Affärsmannaskap', 'Operativt arbete', 'Skatt', 'Redovisning', 'Konflikthantering', 'Entreprenörskap']

def get_words():
    return(lista2)


##Takes three words and returns 5 matching occupations

def get_occupation(word1, word2, word3):

    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # load your dataset into a Pandas DataFrame
    df = pd.read_csv('clean_occup.csv')

    # create a TfidfVectorizer object to convert the text descriptions into a numerical matrix
    tfidf = TfidfVectorizer()

    # fit the TfidfVectorizer object to the text descriptions of the occupations
    tfidf_matrix = tfidf.fit_transform(df['description'])

    # create a list of the input words
    input_words = [word1, word2, word3]

    # convert the input words into a numerical matrix using the TfidfVectorizer object
    input_matrix = tfidf.transform(input_words)

    # calculate the cosine similarity between the input matrix and the tfidf matrix for all occupations
    cosine_similarities = cosine_similarity(input_matrix, tfidf_matrix)

    # get the top 5 occupations with the highest similarity scores
    top_indexes = cosine_similarities.argsort()[0][-5:][::-1]

    # create a list of the top 5 occupations with the highest similarity scores
    top_occupations = []
    for index in top_indexes:
        top_occupations.append(df.iloc[index]['occupation'])

    # print the top 5 occupations with the highest similarity scores
    #print("The input words match with the following occupations:")
    #print(top_occupations)
    return top_occupations




import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_occupation2(word1, word2, word3):
    # Load occupation data
    df = pd.read_csv('clean_occup.csv')

    # Preprocess occupation descriptions. Puts words into vectors for each  
    tfidf = TfidfVectorizer()
    description_vectors = tfidf.fit_transform(df['description'].fillna(''))

    # Create input vector by transforming a string containing three words (word1, word2, and word3) 
    # using the same TfidfVectorizer instance. The resulting vector is stored in a variable called "input_vector".
    input_vector = tfidf.transform([' '.join([word1, word2, word3])])

    # Compute cosine similarity (similarity between two vectors) between input vector and occupation description vectors
    similarity_scores = cosine_similarity(input_vector, description_vectors)

    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores, axis=1)[:, -5:].squeeze()[::-1]
    return df.iloc[top_occupations]['occupation'].tolist()

print(get_occupation('säkerhet', 'social', 'människor'))
print(get_occupation2('säkerhet', 'social', 'människor'))


## Experiment

import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import random

def extract_common_words():
    # load the dataset
    df = pd.read_csv('clean_occup.csv')

    # tokenize the descriptions
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    df['tokens'] = df['description'].apply(lambda x: tokenizer.tokenize(x.lower()))

    # remove stop words
    stop_words = stopwords.words('swedish')
    df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

    # count the word frequency
    word_counts = Counter([word for words in df['tokens'] for word in words])

    # extract 50 random but common words
    common_words = [word[0] for word in word_counts.most_common()]
    random.shuffle(common_words)
    common_words = common_words[:50]

    return common_words


