import streamlit as st
import os
import nltk
import re
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
from nltk.data import find

def download_nltk_data():
    target_dir = os.path.join(os.getcwd(), 'nltk_data')
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    try:
        find('corpora/stopwords.zip', paths=[target_dir])
        print("NLTK data already exists.")
    except LookupError:
        print("Downloading only required NLTK data...")
        nltk.download('stopwords', download_dir=target_dir)
        print(f"NLTK stopwords data has been downloaded to {target_dir}")

download_nltk_data()

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