import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title(index):	
	return df[df.index == index]["title"].values[0]

def get_index(title):		
	return df[df.title == title]["index"].values[0]
df = pd.read_csv("F:\\GithubMY\\Movie\\dataset.csv")
features = []
for feature in features:
	df[feature] = df[feature].fillna('')		
def combination(row):
	try:	
	except:
		
df["combination"] = df.apply(combination,axis=1)
