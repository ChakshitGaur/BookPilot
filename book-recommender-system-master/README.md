# 📚 BookPilot — Book Recommendation System

A **Machine Learning-based Book Recommendation System** built using **Python, Flask, Pandas, NumPy, and Scikit-learn**.

BookPilot recommends books similar to a book selected by the user using **collaborative filtering and cosine similarity**.

## 🚀 Features

- 📖 Browse popular books
- 🔍 Search for a book
- 🤖 Get personalized similar-book recommendations
- ⭐ Display book ratings
- 🖼️ Display book covers
- 🌐 Simple and responsive Flask web interface

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **HTML**
- **CSS**
- **Jupyter Notebook**

## 🧠 Machine Learning

The recommendation system uses **collaborative filtering**.

The main steps are:

1. Load the books, users, and ratings datasets.
2. Merge the book and rating information.
3. Create a user-book rating matrix.
4. Filter active users and sufficiently rated books.
5. Calculate **cosine similarity** between books.
6. Use the similarity scores to recommend books similar to the selected book.

## 📂 Project Structure

```text
Book-recommender-System/
│
├── app.py
├── book-recommender-system.ipynb
├── popular.pkl
├── pt.pkl
├── books.pkl
├── similarity_scores.pkl
├── Books.csv
├── Users.csv
├── Ratings.csv
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd Book-recommender-System
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## 📊 Dataset

The project uses book, user, and rating data to build the recommendation system.

The datasets contain information such as:

- Book titles
- Authors
- Publishers
- Users
- User ratings
- Book cover image URLs

## 📌 Note

The `.pkl` files contain the processed data and similarity calculations required by the Flask application.

The Jupyter Notebook contains the data preprocessing, model-building, and recommendation-system development process.

## ⚠️ Disclaimer

This project is created **for educational and demonstration purposes only**. The recommendations are generated using a machine learning approach and should not be considered professional or definitive recommendations.

## 👨‍💻 Author

**Chakshit Gaur**