import pickle
import streamlit as st # type: ignore
import numpy as np

st.header('Books Recommendation System using Machine Learning')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
my_final_rating = pickle.load(open('artifacts/my_final_rating.pkl', 'rb'))


def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

selected_books = st.selectbox(
    "Type or select a book", books_name)

if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)