🎬 Hybrid Movie Recommender System

A personalized Hybrid Movie Recommendation System that combines Collaborative Filtering and Content-Based Filtering to deliver accurate, user-centric movie suggestions. This app integrates the TMDB API for dynamic posters and metadata, and is fully deployed using Streamlit, enabling real-time interactions and seamless user experience.

🚀 Features
🔹 Hybrid Recommendation Engine

Content-Based Filtering: Uses movie overviews, genres, keywords, and cast/crew metadata.

Collaborative Filtering: Leverages user–movie rating patterns for similarity-based predictions.

Hybrid Approach: Combines both methods for more accurate and diverse recommendations.

🔹 TMDB API Integration

Fetches posters, backdrops, ratings, cast details, and descriptions dynamically.

Ensures high-quality and visually appealing movie displays.

🔹 Streamlit-Powered Interface

Clean, responsive UI for real-time recommendations.

Interactive selection options for users to choose movies and explore similar titles.

🛠️ Tech Stack

Python

Pandas, NumPy, Scikit-Learn

TMDB API

Streamlit

Pickle / Joblib (for model persistence)

📁 Project Structure
├── app.py                 # Streamlit app  
├── model/                 # Preprocessed datasets & similarity matrices  
├── utils/                 # API helper functions  
├── requirements.txt       # Project dependencies  
├── README.md              # Project documentation  
└── assets/                # Images / logo  
