
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


print(get_occupation('kund', 'vård', 'hjälp'))