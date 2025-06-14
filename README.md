# 🎬 Simple Movie Recommendation System

This is a basic content-based movie recommendation system built using Python and Flask. It uses cosine similarity to suggest similar movies based on the title you enter.

## 🚀 Features

- Input a movie title
- Get 5 recommended movies using cosine similarity
- Basic web interface with HTML/CSS (Flask)
- Modular Python code
- Can be extended to larger datasets or ML models

## 📁 Project Structure
.
├── app.py # Flask web app
├── recommender.py # Logic for recommending movies
├── templates/ # HTML files
├── static/ # CSS files
├── requirements.txt # Python dependencies
├── README.md # You're reading it!

## 🧠 How It Works

1. The user inputs a movie name
2. The system finds its index in the dataset
3. Calculates cosine similarity with other movies
4. Returns top 5 similar movies
