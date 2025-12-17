from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from recommender import SongRecommender

app = FastAPI(title="Song Recommendation System")

# USE CLEANED DATASET
recommender = SongRecommender("data/cleaned_songs.csv")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/recommend")
def recommend(song: str, top_n: int = 5):
    return {
        "input": song,
        "recommendations": recommender.recommend_by_song(song, top_n),
    }


@app.get("/recommend-by-mood")
def recommend_by_mood(mood: str, top_n: int = 5):
    return {
        "input": mood,
        "recommendations": recommender.recommend_by_mood(mood, top_n),
    }
