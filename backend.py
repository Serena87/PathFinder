import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
#Skickar ord att fylla bubblorna med till frontend
lista = ['Noggran', 'Kreativ', 'Djur', 'Körkort', 'Positiv', 'Människor', 'Mat', 'Hållbarhet', 'Vårdande', 'Social', 'Försäljning']

def get_words():
    return(lista)





##Tar in 3 ord och skickar tillbaka fem yrken


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


print(get_occupation('utåtriktad', 'körkort', 'människor'))

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_occupation2(word1, word2, word3):
    # Load occupation data
    df = pd.read_csv('clean_occup.csv')

    # Preprocess occupation descriptions
    tfidf = TfidfVectorizer(stop_words='english')
    description_vectors = tfidf.fit_transform(df['description'].fillna(''))

    # Create input vector
    input_vector = tfidf.transform([' '.join([word1, word2, word3])])

    # Compute cosine similarity between input vector and occupation description vectors
    similarity_scores = cosine_similarity(input_vector, description_vectors)

    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores, axis=1)[:, -5:].squeeze()[::-1]
    return df.iloc[top_occupations]['occupation'].tolist()

print(get_occupation2('utåtriktad', 'körkort', 'människor'))

import pandas as pd
import numpy as np
import gensim.downloader as api
from gensim.models import Word2Vec
from gensim.similarities import SoftCosineSimilarity
from sklearn.preprocessing import normalize

def get_occupation3(word1, word2, word3):
    # Load occupation data
    df = pd.read_csv('clean_occup.csv')

    # Preprocess occupation descriptions
    model = api.load('glove-wiki-gigaword-300')
    w2v = dict(zip(model.wv.index2word, model.wv.vectors))
    doc_vectors = [np.mean([w2v[w] for w in doc.split() if w in w2v], axis=0) for doc in df['description'].fillna('')]
    norm_vectors = normalize(doc_vectors)

    # Create input vector
    input_vector = np.mean([w2v[w] for w in [word1, word2, word3] if w in w2v], axis=0).reshape(1, -1)
    norm_input = normalize(input_vector)

    # Compute Soft Cosine Similarity between input vector and occupation description vectors
    similarity_matrix = SoftCosineSimilarity(norm_vectors)
    similarity_scores = similarity_matrix[norm_input][0]

    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores)[-5:][::-1]
    return df.iloc[top_occupations]['occupation'].tolist()


print(get_occupation3('utåtriktad', 'körkort', 'människor'))