from fastapi import FastAPI

from recommender import recommend
from recommender import search_movie

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Movie Recommendation API"
    }

@app.get("/health")
def health():

    return {
        "status": "Healthy"
    }

@app.get("/recommend")
def get_recommendation(movie: str):

    recommendations = recommend(movie)

    return {
        "movie": movie,
        "recommendations": recommendations
    }   

@app.get("/search")
def search(query: str):

    result = search_movie(query)

    return {
        "results": result
    }