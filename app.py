from flask import Flask, jsonify, request

app = Flask(__name__)

ALLOWED_ORIGINS = {
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:5173",
    "http://localhost:5174",
}

genres = {
    "Action": 0,
    "Adventure": 0,
    "Animation": 0,
    "Biography": 0,
    "Comedy": 0,
    "Crime": 0,
    "Documentary": 0,
    "Drama": 0,
    "Family": 0,
    "Fantasy": 0,
    "Film-Noir": 0,
    "Game-Show": 0,
    "History": 0,
    "Horror": 0,
    "Music": 0,
    "Musical": 0,
    "Mystery": 0,
    "News": 0,
    "Reality-TV": 0,
    "Romance": 0,
    "Sci-Fi": 0,
    "Short": 0,
    "Sport": 0,
    "Talk-Show": 0,
    "Thriller": 0,
    "War": 0,
    "Western": 0
}

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin")
    if origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response

@app.route("/")
def home():
    return "Flask is working!"

@app.route("/recommend", methods=["POST", "OPTIONS"])
def recommend():
    data = request.get_json(silent=True) or {}

    selected_movies = data.get("selectedMovies", [])
    genre = [movie["Genre"] for movie in selected_movies]


    for g in genre:
        for item in g.split(", "):
            if item in genres:
                genres[item] += 1


    vector = []
    #print(selected_movies)
    if len(genre) > 0:
        for value in genres.values():
            vector.append(value / len(genre))
    else:
        for value in genres.values():
            vector.append(0)

    print(vector)
    return jsonify({"Genre": genre})


   

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
    