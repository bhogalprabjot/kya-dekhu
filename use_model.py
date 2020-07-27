import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from joblib import dump, load

from difflib import get_close_matches

movieList = load('movieList.joblib')
movieNames = movieList.tolist()

def get_title_from_index(index):
    # return df[df.index == index]["title"].values[0]
    return movieNames[index] 

def get_index_from_title(title):
    # return df[df.title == title]["index"].values[0]
    return movieNames.index(title)


def nameCheck(name):
    simName = get_close_matches(name, movieNames)
    if name in movieNames:
       return name , True
    elif simName:
        return simName[0], True
    else:
        return "This movie does not exist in my dataset! I'll update it shortly!", False
    

def recommend(movie):

    model = load('model.joblib')

    movie_user_likes = movie
    cosine_sim = cosine_similarity(model)

    movie_index = get_index_from_title(movie_user_likes)
    similar_movies = list(enumerate(cosine_sim[movie_index]))

    sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)
    
    rec_movies = []
    i=0
    # print("\nList of similar movies: \n")
    for movie in sorted_similar_movies:
        rec_movies.append(get_title_from_index(movie[0]))
        # print(rec_movies)
        i+=1
        if i>5:
            break

    return rec_movies


# if __name__ == '__main__':
#     recommend("Avatar")