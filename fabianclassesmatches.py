import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the job dataset
jobs = pd.read_csv('clean_occup.csv')

# Define the clean_text function
def clean_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation marks
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words for Swedish language
    swedish_stop_words = stopwords.words('swedish')
    words = [word for word in words if not word in swedish_stop_words]

    # Join the words back into a string
    text = ' '.join(words)

    return text

# Define the clean_jobs function
def clean_jobs(jobs):
    # Remove rows with missing job descriptions
    jobs = jobs.dropna(subset=['Description'])

    # Clean the job descriptions
    jobs['Description'] = jobs['Description'].apply(clean_text)

    return jobs

# Clean the job dataset
jobs = clean_jobs(jobs)

# Define the classify_job function
def classify_job(input_words, jobs):
    # Create a set of the input words
    input_words_set = set(input_words)

    # Create a dictionary to store the scores for each job
    job_scores = {}

    # Loop through each job description
    for index, row in jobs.iterrows():
        description = row['Description']
        score = 0

        # Loop through each word in the job description
        for word in description.split():
            if word in input_words_set:
                score += 1

        # Add the score to the job_scores dictionary
        job_scores[row['Occupation']] = score

    # Sort the job_scores dictionary by the scores in descending order
    sorted_jobs = sorted(job_scores.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 jobs with the highest scores
    return sorted_jobs[:5]

# Example usage
input_words = ['samarbetande', 'analytisk', 'kreativ']
matching_jobs = classify_job(input_words, jobs)
print(matching_jobs)
