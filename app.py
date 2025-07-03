import streamlit as st
import pickle
import os
import zipfile

st.title("🎬 Movie Recommender System")

# Unzip similarity.pkl if it doesn't exist
if not os.path.exists("similarity.pkl"):
    if os.path.exists("similarity.zip"):
        with zipfile.ZipFile("similarity.zip", 'r') as zip_ref:
            zip_ref.extractall(".")

# Load the similarity matrix and movie DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_df = pickle.load(open('movies.pkl', 'rb'))

# Extract movie titles
movie_list = movie_df['title'].values
selected_movie = st.selectbox("Select a Movie", movie_list)

# Recommendation function (without list comprehension)
def recommend(movie):
    movie_index = movie_df[movie_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    for i in movie_indices:
        movie_title = movie_df.iloc[i[0]]['title']
        recommended_movies.append(movie_title)

    return recommended_movies

# Display recommended movies
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write("🎥", movie)
