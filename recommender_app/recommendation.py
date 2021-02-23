import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def create_sim():
    df = pd.read_csv('data/data.csv')
    sim = np.load('data/similarity_matrix.npy')
    return df, sim


def generate_recommendation(movie_name, top=10):
    movie_name = movie_name.lower()
    df, sim = create_sim()

    if movie_name not in df['movie_title'].unique():
        return False
    else:
        idx = df.loc[df['movie_title']==movie_name].index[0]
        movie_list = list(enumerate(sim[idx]))
        movie_list = sorted(movie_list, key = lambda x:x[1] ,reverse=True)
        movie_list = movie_list[1:top+1]

        recommendation = []
        for i in range(len(movie_list)):
            y = movie_list[i][0]
            name = ' '.join(word.title() for word in df['movie_title'][y].split(' '))
            recommendation.append(name)
            
        return recommendation

