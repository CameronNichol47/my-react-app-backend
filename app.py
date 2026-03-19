from flask import Flask, jsonify, request

app = Flask(__name__)

ALLOWED_ORIGINS = {
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:5173",
    "http://localhost:5174",
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
    titles = [movie["Title"] for movie in selected_movies]

    print("TITLES:", titles)
    return jsonify({"titles": titles})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)