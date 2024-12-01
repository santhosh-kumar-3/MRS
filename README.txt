###Movie Recommendation System###

This project is a Movie Recommendation System built using Python, Flask, and scikit-learn. 
It suggests movies based on their titles and genres using content-based filtering.

###Features
Suggests similar movies based on a given movie title.
Modern and user-friendly interface using Bootstrap.
Simple and lightweight web application.

###Installation and Usage

Prerequisites
Python: Ensure Python 3.8+ is installed on your system.
Pip: Make sure pip (Python package manager) is installed.

###Steps to Run the Project

#Extract the ZIP File:

- Download the ZIP file and extract it into a folder.

- Navigate to the Project Directory. (cd path/to/ML-project)

- Install Dependencies: Install the required Python packages using the requirements.txt file: ( pip install -r requirements.txt )

- Run the Application: Start the Flask server by running: ( python app.py )

- Access the Application: Open a web browser and go to: http://127.0.0.1:5000


###Project Structure

  ML-project/
  ├── app.py                # Main Flask application
  ├── recommendation.py     # Recommendation system logic
  ├── templates/
  │   └── index.html        # HTML template for the web app
  ├── movies.csv            # Dataset of movies
  ├── requirements.txt      # List of Python dependencies


###How It Works
  Content-Based Filtering:

  This system uses a combination of movie genres and titles to create a feature vector for each movie.
  TF-IDF (Term Frequency - Inverse Document Frequency) is used to process the text data and represent it numerically.
  Cosine Similarity:

  The similarity between movies is calculated using the cosine similarity algorithm, which measures the angular difference between feature vectors.
  Recommendations:

  Based on the cosine similarity scores, the system ranks and returns the top 5 most similar movies.
