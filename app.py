from flask import Flask, request, render_template
from recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend(movie)
        return render_template("index.html", recommendations=recommendations)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
