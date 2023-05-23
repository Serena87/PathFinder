# HEJ Front-end!!
# Ropa på get_random_words för en lista på 50 ord skapad av en människa
# Ropa på get_egenskaper() för en lista på 50 egenskaper
# Ropa på get_arbetsuppgifter() för en lista på 50 arbetsuppgifter
# Ropa på get_occupation2 och skicka in upp till 5 ord och få tillbaka en lista på 5 yrken
# 3-5 ord fungerar bäst. Om ni skickar färre än 5, skicka med tomma strängar för resterande ord t.ex 
# Get_occupation('hjälpsam', 'noggrann', 'ledning', '', '')
# Ni får snabbt tillbaka en lista på 5 occupations som passar
# Varma hälsningar


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import openai

# Skickar ord att fylla bubblorna med till frontend.
# Hämtar från fil

def get_egenskaper():
    with open(('ord_egenskaper.txt'), 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    
    if 16 >= len(words):
        return words
    
    random_words = random.sample(words, 16)

    return random_words

# Gets 15 arbetsuppgifter

def get_arbetsuppgifter():
    with open(('ord_arbetsuppgifter.txt'), 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    
    if 15 >= len(words):
        return words
    
    random_words = random.sample(words, 15)

    return random_words

## Takes x amount of words, returns 5 suitable occupations using cosine similarity. Used by frontend. 

##Pre process creating vector space
    # Load occupation data
print('Reading dataset...')
df = pd.read_csv('dataset2022.csv')
print('dataset read!')

    # Preprocess occupation descriptions. Puts words into vectors for each  
print('Processing occupation descriptions...')
tfidf = TfidfVectorizer()
description_vectors = tfidf.fit_transform(df['description'].fillna(''))

def get_occupation2(word1, word2, word3, word4, word5):


    # Create input vector by transforming a string containing three words (word1, word2, and word3) 
    # using the same TfidfVectorizer instance. The resulting vector is stored in a variable called "input_vector".
    print('Creating input vector...')

    input_vector = tfidf.transform([' '.join([word1, word2, word3, word4, word5])])
    print('Input vector created')

    # Compute cosine similarity (similarity between two vectors) between input vector and occupation description vectors
    print('Matching...')
    similarity_scores = cosine_similarity(input_vector, description_vectors)


    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores, axis=1)[:, -5:].squeeze()[::-1]
    return df.iloc[top_occupations]['occupation'].tolist()

# Function that takes chosen job and searchs ChatGPT for info and then returns a decription
def get_description(yrke):
    print('matching job..')
    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.2, # How ridgid or creative the answer chould be, 0.0 ridgid, 2.0 super creative
    max_tokens = 1500, 
    # promts for the chatbot
    messages = [
        {"role": "system", "content": "beskriv yrket och ge en realistisk framtidsprognos yrket, 3 bra saker med yrket i 1,2,3-form och vilken utbildning som behövs"},
        {"role": "user", "content": yrke}])
    return(completion.choices[0].message.content)


#print(get_occupation2('säkerhet', 'människor', 'social', 'utåtriktad', 'vakt'))


