#from flask import Flask

#app = Flask(__name__)

#@app.route("/pathfinder")
#def hello():
    #return "Hello, welcome to PathFinder"

## NLTK SET UP ##

## Natural language processing, pandas setup

#Import tokenization, download stopwords & punkt. Download not needed each run but left in for compatibility.
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import download 
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
nltk.download('punkt')


## Feed variable with NLTK stopwords
stop_words = set(stopwords.words("swedish"))


## SET UP PANDAS & READ FILE ##
import pandas as pd
# read the file called 2022.json that is in the same directory and call it jobtech_dataset
jobtech_dataset = pd.read_csv('jobtech_dataset2022.csv')
pd.set_option('max_colwidth', None) # Tell editor to not limit column width


df = jobtech_dataset[['id', 'description', 'working_hours_type', 'must_have', 'nice_to_have']]  # Picking our columns

## BASIC NLP ##

min_variabel = df.iloc[2]['description']            # Taking the second row from the data and only 'description' column
# Prints the entire description of a certain row for debug purposes
print(min_variabel)

# Tokenizes by word, each word becomes an entry in an array. Feed them into another variable. We need to fix our variable names.
variabel = word_tokenize(str(min_variabel))

#For each word in our variable, remove those that are stopwords
filtrerad_lista = []
for word in variabel:
    if word.casefold() not in stop_words:
        filtrerad_lista.append(word)

#Prints our list of remaining, non-stop words

#print(filtrerad_lista)
