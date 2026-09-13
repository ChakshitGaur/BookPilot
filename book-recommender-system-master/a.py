import pickle
import pandas as pd

books = pd.read_csv('Books.csv', low_memory=False)
users = pd.read_csv('Users.csv', low_memory=False)
ratings = pd.read_csv('Ratings.csv', low_memory=False)