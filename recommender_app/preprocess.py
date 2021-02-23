import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('data/movie_metadata.csv')

df = df.loc[:,['actor_1_name','actor_2_name','actor_3_name','director_name','genres','movie_title']]

df['actor_1_name'] = df['actor_1_name'].replace(np.nan, 'unknown')
df['actor_2_name'] = df['actor_2_name'].replace(np.nan, 'unknown')
df['actor_3_name'] = df['actor_3_name'].replace(np.nan, 'unknown')
df['director_name'] = df['director_name'].replace(np.nan, 'unknown')
df['genres'] = df['genres'].replace('|', ' ')
df['movie_title'] = df['movie_title'].str.lower()
df['movie_title'] = df['movie_title'].str[:-1]

# df.to_csv('data/data.csv',index=False)
# data = pd.read_csv('data.csv')

df['movie_info'] = df['actor_1_name'] + ' ' + df['actor_2_name'] + ' '+ df['actor_3_name'] + ' '+ df['director_name'] + ' ' + df['genres']

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['movie_info'])
sim = cosine_similarity(count_matrix)

np.save('data/similarity_matrix', sim)
df.to_csv('data/data.csv',index=False)
