import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SongRecommender:
    def __init__(self, csv_path):
        """
        Load dataset and prepare TF-IDF matrix
        """
        # Load cleaned dataset
        self.df = pd.read_csv(csv_path)

        # Safety cleaning
        self.df = self.df[["song", "artist", "text"]]
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)

        # Create lowercase song column for matching
        self.df["song_lower"] = self.df["song"].str.lower()

        # Combine text features
        self.df["combined"] = (
            self.df["song"] + " " + self.df["artist"] + " " + self.df["text"]
        )

        # TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["combined"])

    def recommend_by_song(self, song_name, top_n=5):
        """
        Recommend songs based on song similarity
        """
        if not isinstance(song_name, str):
            return []

        song_name = song_name.strip().lower()

        # Check if song exists
        if song_name not in self.df["song_lower"].values:
            return []

        # Get index of input song
        idx = self.df[self.df["song_lower"] == song_name].index[0]

        # Compute cosine similarity
        similarity_scores = cosine_similarity(
            self.tfidf_matrix[idx], self.tfidf_matrix
        ).flatten()

        top_indices = similarity_scores.argsort()[::-1][1 : top_n + 1]

        return [
            {"song": self.df.iloc[i]["song"], "artist": self.df.iloc[i]["artist"]}
            for i in top_indices
        ]

    def recommend_by_mood(self, mood_text, top_n=5):
        """
        Recommend songs based on mood text
        """
        if not isinstance(mood_text, str):
            return []

        mood_text = mood_text.strip().lower()

        mood_vector = self.vectorizer.transform([mood_text])

        similarity_scores = cosine_similarity(mood_vector, self.tfidf_matrix).flatten()

        top_indices = similarity_scores.argsort()[::-1][:top_n]

        return [
            {"song": self.df.iloc[i]["song"], "artist": self.df.iloc[i]["artist"]}
            for i in top_indices
        ]
