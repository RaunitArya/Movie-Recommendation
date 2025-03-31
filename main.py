import pickle
import time

import pandas as pd
import streamlit as st
import requests

from streamlit_lottie import st_lottie

from dotenv import load_dotenv
import os

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottie_url("https://lottie.host/63eb9dac-2602-4b4a-93cf-8ef67108eee6/HAW2psDBQ2.json")

col1, col2 = st.columns([1,3])
with col1:
    st_lottie(lottie_animation, width=200, height=150)
    
with col2:
    # st.title('CinemAI')
    st.markdown('<h1 style="font-size: 84px;">CinemAI</h1>', unsafe_allow_html=True)

def fetch_poster(movie_id):
   response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US')
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

def get_genre(x):
    genres = []
    if x['genres']:
        genre_str = " "
        for i in range(0, len(x['genres'])):
            genres.append(x['genres'][i]['name'])
        return genre_str.join(genres)
    else:
        return 0

def get_actors():
    url = "https://api.themoviedb.org/3/movie/{}/credits?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": f"{TMDB_ACCESS_TOKEN}"
    }
    re = requests.get(url, headers=headers)
    re = re.json()
    actors = []
    if re['cast']:
        for i in range(0, 5):
            actors.append(re['cast'][i]['name'])
        return actors
    else:
        return 0

def get_actors_pic():
    url = "https://api.themoviedb.org/3/movie/{}/credits?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": f"{TMDB_ACCESS_TOKEN}"
    }
    re = requests.get(url, headers=headers)
    re = re.json()
    pics = []
    for i in range(0, 5):
        pics.append(re['cast'][i]['profile_path'])
    return pics

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

title = st.selectbox("Enter Movie Name", movies['title'].values)
search = st.button("Search")

movie_index = movies[movies['title'] == title].index[0]
movie_id = movies.iloc[movie_index].movie_id

if search:
    # try:
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": f"{TMDB_ACCESS_TOKEN}"
    }
    re = requests.get(url, headers=headers)
    re = re.json()
    col1, col2 = st.columns([1, 2])
    with col1:
        # st.image("https://image.tmdb.org/t/p/w500/" + re['poster_path'])
        st.image(fetch_poster(movie_id))
    with col2:
        st.subheader(re['title'])
        st.caption(f"Genre: {get_genre(re)}")
        st.caption(f"Release Date: {re['release_date']}")
        st.write(re['overview'])
        st.caption(f"Rating: {re['vote_average']}")
        st.progress(float(re['vote_average'])/10)
        st.link_button("For more info", re['homepage'])

    container = st.container()
    with container:
        st.subheader("Top Cast")
        col1, col2, col3, col4, col5 = st.columns(5)
        names = get_actors()
        pics = get_actors_pic()

        with col1:
            st.text(names[0])
            st.image("https://image.tmdb.org/t/p/w500/" + pics[0])

        with col2:
            st.text(names[1])
            st.image("https://image.tmdb.org/t/p/w500/" + pics[1])

        with col3:
            st.text(names[2])
            st.image("https://image.tmdb.org/t/p/w500/" + pics[2])

        with col4:
            st.text(names[3])
            st.image("https://image.tmdb.org/t/p/w500/" + pics[3])

        with col5:
            st.text(names[4])
            st.image("https://image.tmdb.org/t/p/w500/" + pics[4])
            
    
    st.subheader("Recommendation")
    names,posters = recommend(title)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
       
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
       
    with col4:
        st.text(names[3])
        st.image(posters[3])
        
    with col5:
        st.text(names[4])
        st.image(posters[4])
        
# HTML code for displaying popular movies
with open('popular_movies.html', 'r') as file:
    html_code = file.read()

st.subheader("Trending Movies")
num_movies = 20
html_height = 200*num_movies

# Embed the HTML code for displaying popular movies
st.components.v1.html(html_code, height=html_height, width = 1200)

