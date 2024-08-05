import streamlit as st
import os
import nltk
from nltk.data import find
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
import re

# Define the target directory for NLTK data
target_dir = '/usr/local/share/nltk_data'

# Check if the target directory exists and contains NLTK data
try:
    find('corpora/stopwords.zip', paths=[target_dir])
    print(f"NLTK data already exists in {target_dir}")
except LookupError:
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Download NLTK data to the target directory
    nltk.download('all', download_dir=target_dir)
    print(f"NLTK data has been downloaded and installed to {target_dir}")

st.title("Hallo Semua Selamat Datang di app NLP yang Ihrat Buat")

st.subheader("Welcome to our Application")

text = st.text_area("Enter Your Text Contoh 'hari ini cuaca cerah / Good Weather'")

#Keeping only Text and digits
text = re.sub(r"[^A-Za-z0-9]", " ", text)
#Removes Whitespaces
text = re.sub(r"\'s", " ", text)
# Removing Links if any
text = re.sub(r"http\S+", " link ", text)
# Removes Punctuations and Numbers
text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)

# Splitting Text
text = text.split()

# Lemmatizer
wnl = WordNetLemmatizer()
lemmatized_words =[wnl.lemmatize(word, pos='v') for word in text]
text = " ".join(lemmatized_words)

    
if st.button("Analyze 1"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity
        if result > 0.0:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.warning('Sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))
        st.success("Polarity Score is: {}".format(result))

        
import streamlit as st
# NLP Pkgs
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
import re

def main():
    st.title("NLP")

    st.subheader("Welcome to our Application")

    text = st.text_area("Your Text Contoh Aku Patah Hati")

    #Text Cleaning
    #Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    #Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)

    # Splitting Text
    text = text.split()

    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words =[lemmatizer.lemmatize(word, pos='v') for word in text]
    text = " ".join(lemmatized_words)

    if st.button("Analyze"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity
        if result > 0.0:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.warning('Sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))
        st.success("Polarity Score is: {}".format(result))

if __name__ == '__main__':
    main()