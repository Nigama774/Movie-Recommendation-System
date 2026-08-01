import joblib

# Load the saved objects
movies = joblib.load("models/movies.pkl")
similarity = joblib.load("models/similarity.pkl")


def recommend(movie_name, top_n=10):

    movie_name = movie_name.lower()

    # Find matching movie
    #matches = movies[movies["title"].str.lower() == movie_name]
    matches = movies[movies["title"].str.lower().str.contains(movie_name)]

    if matches.empty:
        return []

    idx = matches.index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:top_n+1]

    recommendations = []

    for i, score in similarity_scores:
        recommendations.append(
            movies.iloc[i]["title"]
        )

    return recommendations


def search_movie(query):

    query = query.lower()

    result = movies[
        movies["title"].str.lower().str.contains(query)
    ]

    return result["title"].tolist()[:10]

if __name__ == "__main__":

    print(recommend("Toy Story (1995)"))