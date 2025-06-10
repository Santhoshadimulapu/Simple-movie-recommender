import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
movies = pd.read_csv('movies.csv')
movies['combined']=movies['title']+" "+movies["genres"]
cv=CountVectorizer(stop_words='english')
vectorized=cv.fit_transform(movies['combined'])
similarity=cosine_similarity(vectorized)
def recommend(movie_title):
    try:
        idx = movies[movies['title'].str.contains(movie_title,case=False)].index[0]
        scores = list(enumerate(similarity[idx]))
        scores = sorted(scores,key=lambda x:x[1],reverse=True)[1:6]
        recommended_titles = []
        for i in scores:
            recommended_titles.append(movies.iloc[i[0]]['title'])
        return recommended_titles
    except IndexError:
        return ["❌ Sorry, we cannot find the movie you are looking for"]
        