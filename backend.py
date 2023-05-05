import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
#Skickar ord att fylla bubblorna med till frontend
lista = ['Noggran', 'Kreativ', 'Djur', 'Körkort', 'Positiv', 'Människor', 'Mat', 'Hållbarhet', 'Vårdande', 'Social', 'Försäljning']

def get_words():
    return(lista)





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


## Extract common words (WIP)
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

def extract_common_words():
    # Download stopwords just in case not done before
    nltk.download('stopwords')
    
    # Load dataset
    df = pd.read_csv('clean_occup.csv')
    
    # Select a random sample of occupations
    sample_df = df.sample(n=100)
    
    # Get Swedish stopwords
    swedish_stopwords = stopwords.words('swedish')
    
    # Create a count vectorizer object
    vectorizer = CountVectorizer(stop_words=swedish_stopwords)
    
    # Fit and transform the count vectorizer on the occupation descriptions
    count_matrix = vectorizer.fit_transform(sample_df['description'])
    
    # Get the total count for each word in the count matrix
    word_count = np.sum(count_matrix, axis=0)
    
    # Convert the word count matrix to a list of tuples (word, count)
    word_count_list = [(word, word_count[0, i]) for word, i in vectorizer.vocabulary_.items()]
    
    # Sort the list of tuples by count in descending order
    sorted_word_count_list = sorted(word_count_list, key=lambda x: x[1], reverse=True)
    
    # Get the top 50 words
    top_words = [word[0] for word in sorted_word_count_list[:50]]
    
    return top_words

print(extract_common_words())