from flask import Flask, render_template, request
from recommendation import get_recommendations

app = Flask(__name__)

# Combine GET and POST methods for the home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        movie_title = request.form["movie"]
        try:
            recommendations = get_recommendations(movie_title)
            return render_template(
                "index.html",
                recommendations=recommendations,
                movie_title=movie_title,
            )
        except IndexError:
            return render_template(
                "index.html",
                error="Movie not found. Please try another title.",
            )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
