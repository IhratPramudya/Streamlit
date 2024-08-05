import streamlit as st
import nltk
import re
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

st.title("Hallo Semua Selamat Datang di app NLP yang Ihrat Buat")

st.subheader("Welcome to our Application WEWELOVEuuuuu")

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
    st.title("NLP Untuk para pencari Cinta Sejati")

    st.subheader("Selamat Datang di aplikasi WEWELOVEuuuuu")

    text = st.text_area("Your Text Contoh 'I Love You' Aku Cinta Kamu")

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