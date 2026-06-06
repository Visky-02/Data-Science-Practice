import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender")

# 1. Loading the datasets
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Recommendation Logic Function
def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['Movie_Title'] == movie].index[0]
    
    # Get similarity distances for that movie
    distances = similarity[movie_index]
    
    # Sort distances to get top 5 similar movies (excluding the movie itself at index 0)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Fetch the movie titles
    recommendations = []
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].Movie_Title)
        
    return recommendations

# 3. Web App UI
st.title("Movie Recommendation System")
st.write("Select a movie from the dropdown to find similar recommendations.")

selected_movie = st.selectbox("Select a Movie:", movies['Movie_Title'].values)

if st.button("Recommend"):
    # Call the recommendation function
    recommended_movies = recommend(selected_movie)
    
    # Display the results
    st.subheader("Top 5 Recommendations:")
    for movie in recommended_movies:
        st.write(f"🎬 {movie}")