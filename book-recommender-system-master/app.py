from flask import Flask, render_template, request
import pickle
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


with open(BASE_DIR / "popular.pkl", "rb") as file:
    popular_df = pickle.load(file)

with open(BASE_DIR / "pt.pkl", "rb") as file:
    pt = pickle.load(file)

with open(BASE_DIR / "books.pkl", "rb") as file:
    books = pickle.load(file)

with open(BASE_DIR / "similarity_scores.pkl", "rb") as file:
    similarity_scores = pickle.load(file)


app = Flask(__name__)


def clean_image_url(url):
    url = str(url)

    if "](" in url:
        url = url.split("](")[1]
        url = url.rstrip(")")

    return url


@app.route("/")
def index():

    images = [
        clean_image_url(url)
        for url in popular_df["Image-URL-M"].values
    ]

    return render_template(
        "index.html",
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=images,
        votes=list(popular_df["num_ratings"].values),
        rating=list(popular_df["avg_rating"].values)
    )


@app.route("/recommend")
def recommend_ui():

    return render_template("recommend.html")


@app.route("/recommend_books", methods=["POST"])
def recommend():

    user_input = request.form.get("user_input", "").strip()

    if not user_input:
        return render_template(
            "recommend.html",
            error="Please enter a book name."
        )

    # -----------------------------------
    # Find book using partial matching
    # -----------------------------------

    user_input_lower = user_input.lower()

    matches = []

    for index, title in enumerate(pt.index):

        title_lower = str(title).strip().lower()

        if user_input_lower in title_lower:
            matches.append((index, title))

    # -----------------------------------
    # Book not found
    # -----------------------------------

    if not matches:

        return render_template(
            "recommend.html",
            error=f'No book found for "{user_input}".'
        )

    # -----------------------------------
    # Select best match
    # -----------------------------------

    book_index = matches[0][0]


    # -----------------------------------
    # Find similar books
    # -----------------------------------

    similar_items = sorted(
        list(
            enumerate(
                similarity_scores[book_index]
            )
        ),
        key=lambda x: x[1],
        reverse=True
    )[1:5]


    data = []


    for i in similar_items:

        temp_df = books[
            books["Book-Title"] == pt.index[i[0]]
        ]

        temp_df = temp_df.drop_duplicates(
            "Book-Title"
        )


        if temp_df.empty:
            continue


        item = [
            temp_df["Book-Title"].iloc[0],
            temp_df["Book-Author"].iloc[0],
            clean_image_url(
                temp_df["Image-URL-M"].iloc[0]
            )
        ]


        data.append(item)


    return render_template(
        "recommend.html",
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)