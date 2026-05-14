# IMPORTING ALL LIBRARIES
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# DOWNLOADING stopwords and wordnet data
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# DEFINING FUNCTION TO CLEAN THE TEXT
def clean_text(text):
    # FIRST STEP TO LOWER THE TEXT SO THAT ALL WORDS CAN BE IN SAME FORMAT WHICH MAKES EASY TO PERFORM FUTHER OPERATIONS 
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()
    # ANALYSING ROOT WORD OF EACH WORDS
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    # WHILE RETURNING WE RETURN IT LIKE STRING
    return ' '.join(words)
