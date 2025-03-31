# CinemAI: A Personalized Movie Recommendation System 🎥

CinemAI is a machine learning-based movie recommendation system designed to help users discover movies tailored to their preferences. This project leverages content-based filtering, cosine similarity, and text vectorization to deliver highly relevant recommendations through an intuitive user interface built with Streamlit, HTML, and CSS.

* * *

## Features ✨

- **Personalized Recommendations**: Suggests movies based on user input and preferences.
- **Content-Based Filtering**: Uses attributes like genres, directors, and actors to calculate similarity.
- **Interactive UI**: A user-friendly interface to search for movies and get recommendations instantly.
- **TMDb Dataset**: Data-driven insights using the popular TMDb 5000 Movie Dataset.
- **Cosine Similarity**: Measures the relevance of movies to suggest the closest matches.
- **Model Persistence**: Utilizes the Pickle library to save and load machine learning models efficiently.

* * *
## Demo 🎬

[![Watch the demo](https://github.com/RaunitArya/Movie-Recommendation/raw/main/main.mp4)]


* * *

## Libraries Used

- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Scikit-Learn**: For building and evaluating the recommendation engine.
- **Streamlit**: For creating the web-based interface.
- **Pickle**: For saving and loading models.

* * *

## Data & Resources 📊

Dataset can be found on Kaggle 
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

* * *

## How to Get TMDb API Key & Access Token 🔑

This project integrates TMDb API to fetch movie details. Follow these steps to obtain your API Key and Access Token:

1. **Sign up on TMDb**

    - Go to [The Movie Database (TMDb)](https://www.themoviedb.org/)
    - Create an account if you don’t already have one.
2. **Request an API Key**

    - Navigate to your profile by clicking on your avatar (top-right corner).
    - Go to **Settings** &gt; **API**.
    - Click on **Create a new API key**.
    - Choose "Developer" and provide the required details.
    - You will receive a **TMDB API Key**.
3. **Generate an Access Token**

    - On the same API page, request a **Bearer Token**.
    - TMDb will generate an access token that you can use for authentication.
4. **Store API Credentials Securely**

    - Create a `.env` file in your project directory and add the following:

            TMDB_API_KEY=your_tmdb_api_key_here
            TMDB_ACCESS_TOKEN=your_tmdb_access_token_here
    - Do **NOT** share this file or upload it to GitHub.
    - Add `.env` to your `.gitignore` file to keep it private.

* * *

## How It Works 🚀

1. **Data Preprocessing**:

    - Cleans the dataset by handling missing values and duplicates.
    - Extracts relevant features like genres, directors, and actors.
2. **Text Vectorization**:

    - Converts textual data into numerical format using techniques like TF-IDF.
3. **Similarity Calculation**:

    - Computes cosine similarity between movies based on their features.
4. **Recommendation Engine**:

    - Suggests movies based on similarity scores.
5. **Web Application**:

    - Built using Streamlit for seamless user interaction.

* * *

## Installation 🛠️

1. Clone this repository:

        git clone https://github.com/your-username/cinemai.git 
        cd cinemai
2. Install the required libraries:

        pip install -r requirements.txt
3. Run the application:

        streamlit run main.py

