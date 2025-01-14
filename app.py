from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import os

# Flask app setup
app = Flask(__name__)
app.secret_key = "super_secret_key_12345"
bcrypt = Bcrypt(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["movie_recommender"]
users_collection = db["users"]

# Load movies data from local JSON file
movies_file_path = "cleaned_movies_fixed.json"
with open(movies_file_path, "r", encoding="utf-8") as f:
    movies = json.load(f)

# Generate embeddings for movies if not already present
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
if "embeddings" not in movies[0]:
    for movie in movies:
        movie["embeddings"] = embedding_model.encode(movie["overview"]).tolist()
    with open(movies_file_path, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def get_id(self):
        return self.id

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user_data = users_collection.find_one({"_id": ObjectId(user_id)})
            if user_data:
                return User(str(user_data["_id"]), user_data["username"])
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

# Routes
@app.route("/")
@login_required
def home():
    return render_template("home.html", name=current_user.username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users_collection.find_one({"username": username})
        if user and bcrypt.check_password_hash(user["password"], password):
            user_obj = User(str(user["_id"]), user["username"])
            login_user(user_obj)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Invalid username or password!", "danger")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        existing_user = users_collection.find_one({"username": username})
        if existing_user:
            flash("Username already exists!", "danger")
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            users_collection.insert_one({"username": username, "email": email, "password": hashed_password})
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))

@app.route("/search", methods=["POST"])
@login_required
def search():
    query = request.form.get("query")
    recommendations = search_movies(query)
    return render_template("recommendations.html", recommendations=recommendations, username=current_user.username)

# Helper functions
def search_movies(query):
    query_embedding = embedding_model.encode(query).tolist()
    movie_embeddings = [movie["embeddings"] for movie in movies]
    similarities = cosine_similarity([query_embedding], movie_embeddings)
    sorted_indices = sorted(range(len(similarities[0])), key=lambda i: similarities[0][i], reverse=True)
    top_movies = [movies[i] for i in sorted_indices[:5]]
    return top_movies

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
