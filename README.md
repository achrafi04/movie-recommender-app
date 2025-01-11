# Movie Recommender Application 🎥🌿

**A sleek, nature-inspired movie recommendation system** that provides personalized movie suggestions based on query similarity. Built with Python, Flask, and MongoDB, it features a user-friendly interface with animated backgrounds and smooth styling.

---

## Description

This application allows users to:
- **Register and Login** securely with their credentials.
- **Search for Movies** using natural language queries to get personalized recommendations based on their interests.
- **Experience a Modern UI** with a dynamic, GIF-based background and semi-transparent containers.

---

## Features

- **User Authentication**: Secure login and registration using `Flask-Login` and `bcrypt`.
- **Recommendation Engine**: Suggests movies using `SentenceTransformer` embeddings.
- **MongoDB Integration**: Stores user data securely and scalably.
- **Local JSON Movie Data**: Efficiently processes and queries pre-stored movie metadata.
- **Stylish Interface**: A green-themed, nature-inspired UI with an animated background.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MongoDB (via `pymongo`)
- **ML Models**: `SentenceTransformer` for semantic embeddings
- **Frontend**: HTML, CSS, Jinja2 templates
- **Deployment**: Flask development server (can be extended for production)

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB installed and running locally
- Git installed

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/movie-recommender-app.git
   cd movie-recommender-app
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare MongoDB Database**:
   - Start MongoDB locally:
     ```bash
     mongod --dbpath "path_to_your_db_directory"
     ```
   - Verify MongoDB is running on `localhost:27017`.

5. **Run the Application**:
   ```bash
   python app.py
   ```
   Access it at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Project Structure

```
movie-recommender-app/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── static/
│   ├── styles.css         # CSS for styling
│   ├── background.gif     # Animated background
├── templates/
│   ├── base.html          # Base layout template
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── home.html          # Search page
│   ├── recommendations.html # Recommendations page
├── data/
│   ├── cleaned_movies_fixed.json # Movie data with embeddings
├── README.md              # This file
├── .gitignore             # Ignore unnecessary files
```

---

## Usage

1. **Register/Login**: Securely log in or register an account.
2. **Search for Movies**: Use the search bar to find personalized movie recommendations.
3. **Enjoy the Experience**: A visually appealing app with seamless functionality.

---

## Future Improvements

- Integrate Pinecone for scalable vector search.
- Add user-specific recommendation history.
- Deploy the app on platforms like Heroku or AWS.

---

## Team

- **Achraf Ikisse** - [GitHub](https://github.com/achrafi04)
- **Moaad Ezzahir**
- **Youssef Bouabid**
- **Hatim Hayou**

---

Feel free to contribute or report issues to make this app even better! 🚀
```

---

### To Use It:
1. Save the content as `README.md` in the root folder of your project.
2. Commit and push it to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Add README with project details"
   git push
   ```
