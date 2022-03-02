import streamlit as st
import pandas as pd
import pickle
import requests

# ======= BACKEND
st.set_page_config(layout='wide')
movie_list = pickle.load(open('tagdata.pkl','rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=649132eacc2ec7c4e3e09bc9ab438e2c&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11 ]
    
    recommend_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        m_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(m_id))

    return recommend_movies , recommended_movies_poster

# ======= Frontend
st.text('By Parmeet')
st.title("Movie Recommendation System")


option = st.selectbox(
     'Please select One Movie',
     movies['title'].values)

if st.button("Recommend Me"):

    names, poster = recommend(option)

    col1 , col2 , col3, col4, col5  = st.columns(5)

    col6 , col7 , col8 , col9 , col10 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image(poster[6])
    with col8:
        st.text(names[7])
        st.image(poster[7])
    with col9:
        st.text(names[8])
        st.image(poster[8])
    with col10:
        st.text(names[9])
        st.image(poster[9])
