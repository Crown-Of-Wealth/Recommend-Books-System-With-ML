import pickle
import streamlit as st # type: ignore
import numpy as np

st.header('Books Recommendation System using Machine Learning')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
my_final_rating = pickle.load(open('artifacts/my_final_rating.pkl', 'rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
        
    for i in book_name[0]:
        ids = np.where(my_final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = my_final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url


def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion[0])):
        books = book_pivotindex[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list

selected_books = st.selectbox(
    "Type or select a book", books_name)

if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
        