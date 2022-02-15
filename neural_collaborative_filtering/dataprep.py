### this file is created to be generate ua file

from google.colab import drive 
drive.mount('/content/drive')


import numpy as np 
import pandas as pd 
from platform import python_version
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
import datetime 
import sys 
import os
import re

### anime dataset has large amount of data, it is time consuming to work with whole dataset, Therefore, I will select couple of columns from the dataset
anime_cleaned_cols = ['anime_id','title_english','type', 'source','episodes','duration_min','score','genre']
users_cleand_cols  = ['username', 'user_id','gender', 'location', 'birth_date']
animelist_cleaned_cols = ['username','anime_id','my_score','my_last_updated']


anime_cleaned = pd.read_csv('drive/MyDrive/Colab Notebooks/datasets/anime/anime_cleaned.csv'
                            ,usecols= anime_cleaned_cols
                            # ,nrows = 10
                           ).dropna()

animelists_cleaned = pd.read_csv('drive/MyDrive/Colab Notebooks/datasets/anime/animelists_cleaned.csv'
                            ,usecols= animelist_cleaned_cols
                            # ,nrows = 10
                           ).dropna()

users_cleaned = pd.read_csv('drive/MyDrive/Colab Notebooks/datasets/anime/users_cleaned.csv'
                            ,usecols= users_cleand_cols
                            # ,nrows = 10
                           ).dropna()


print('ANIME_CLEANED info')
print(anime_cleaned.info())
print('ANIMELISTS_CLANED INFO')
print(animelists_cleaned.info())
print('USERS_CLANED INFO')
print(users_cleaned.info())


#### Seen from the info tabel common columns are anime_id on animelists_cleaned and anime_cleaned and username on animelists_cleaned and users_cleaned. Final dataframe will be created 
#### merging tables on those columns.
df = users_cleaned.merge(animelists_cleaned, left_on = 'username', right_on = 'username')
del animelists_cleaned
del users_cleaned
df = df.merge(anime_cleaned, left_on = 'anime_id', right_on = 'anime_id')
del anime_cleaned

df["username"] = df["username"].astype("category")
df['user_id'] =df['user_id'].astype('int32')
df['gender'] = df['gender'].astype('category')
df['duration_min'] = df['duration_min'].astype('float32')
df['score'] = df['score'].astype('float32')
df['episodes'] =df['episodes'].astype('int32')
# subset.memory_usage(deep = True)
df.info()

###  According to my_last_updated column some of the entries show that there are data points have values before the 2000. I believe those points do not show reliable information.
###  Therefore, I will drop those entries.
old_updated = ((np.where(df['my_last_updated'] < '2000-00-0 00:00:00'))[0][:])
print('number of entries before 2000',len(old_updated))

df = df.reset_index(drop=True)


ua_df = pd.DataFrame({'user_id': df['user_id'],
              'anime_id': df['anime_id'],
              'score': df['score']})

df = df.drop(old_updated)
