
# Song Recommendation System

This project is a **content-based song recommendation system** built using Python and Machine Learning.
It suggests songs either by **similarity to a given song** or based on a **user’s mood** (for example: happy, sad, energetic).

The main idea behind this project is to understand how text data (song lyrics and metadata) can be used to build a recommendation system without relying on user ratings or history.

---

## What the Project Does

* Recommends songs similar to a given song name
* Recommends songs based on mood or emotion entered by the user
* Uses song lyrics, artist name, and song title for similarity comparison
* Provides recommendations through a simple web interface using FastAPI

This is a **content-based system**, meaning recommendations depend only on the song data itself.

---

## How It Works 

1. Song lyrics, song name, and artist name are combined into a single text field.
2. This text is converted into numerical form using **TF-IDF**.
3. **Cosine similarity** is used to measure how similar two songs are.
4. For song-based input, the most similar songs are returned.
5. For mood-based input, the mood text is compared with all songs and the closest matches are shown.

---

## Technologies Used

* Python
* FastAPI
* Pandas
* Scikit-learn
* HTML, CSS, JavaScript

---

## Project Structure

```
song-recommendation-system/
│
├── app.py
├── recommender.py
├── requirements.txt
│
├── data/
│   └── cleaned_songs.csv  (not included in the repository)
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
```

---

## How to Run the Project

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:

```bash
uvicorn app:app --reload
```

3. Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## Testing the System

* Song-based input example:
  `imagine`

* Mood-based input examples:
  `happy`, `sad`, `energetic`

You can also test the APIs using:

```
http://127.0.0.1:8000/docs
```

---

## Dataset Information

The dataset is **not included in this repository** due to GitHub file size limitations.
To run the project, place a cleaned lyrics dataset inside the `data/` folder with the following columns:

* `song`
* `artist`
* `text`

---

## About This Project

This project was built mainly for **learning and academic purposes**.
It helped me understand:

* text vectorization
* similarity-based recommendation systems
* backend-frontend integration using FastAPI

---

## Author

**Ankush Mahato**

* GitHub: [https://github.com/PixelEngineer01](https://github.com/PixelEngineer01)
* Email: [work.ankushmahato@gmail.com](mailto:work.ankushmahato@gmail.com)
