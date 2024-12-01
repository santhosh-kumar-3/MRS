import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_recommendations(movie_title, num_recommendations=5):
    # Load dataset
    movies = pd.read_csv("movies.csv")

    # Combine relevant features for recommendation
    movies['combined_features'] = (
        movies['genres'] + " " + movies['title']
    )

    # Convert text data to feature vectors
    vectorizer = CountVectorizer(stop_words='english')
    feature_matrix = vectorizer.fit_transform(movies['combined_features'])

    # Compute similarity matrix
    similarity_matrix = cosine_similarity(feature_matrix, feature_matrix)

    # Find the index of the given movie
    movie_idx = movies[movies['title'].str.contains(movie_title, case=False)].index[0]

    # Get similarity scores and sort
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get movie titles for recommendations
    recommendations = [
        movies.iloc[idx]['title'] for idx, score in similarity_scores[1:num_recommendations + 1]
    ]
    return recommendations
