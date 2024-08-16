import streamlit as st
import pickle
import pandas as pd
movies_similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = movies_similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
option = st.selectbox(
    "Select the movie for which you want recommendation",
    movies['title'].values
)
if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)