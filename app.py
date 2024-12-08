import pickle
import streamlit as st # type: ignore
import numpy as np

st.header('Books Recommendation System using Machine Learning')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
