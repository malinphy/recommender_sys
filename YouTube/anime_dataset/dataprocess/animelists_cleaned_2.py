# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mt5_TIIsq_zuIlR-LN6GL2z99fTt8GkM
"""

import numpy as np 
import pandas as pd 
import os 
import sys 
from google.colab import drive 
drive.mount('/content/drive')
dir_url = 'drive/MyDrive/Colab Notebooks/datasets/anime/animelists_cleaned.csv'
class data_prep:
  def __init__(self,dir):
    self.dir = dir
  
  def prep(self):
    animelist_cleaned_cols = ['username','anime_id','my_last_updated'] ##since data set is large, 
                                                                       ##I will not add some non-related columns
    df = pd.read_csv(self.dir,
                     usecols = animelist_cleaned_cols,
                    #  nrows = 100
                     )
    

    date_part_1 = []   #### "last_updated" column contains both date and hours
                       ### however, I will not make sorting according to hours,
                       ### therfore time part will be stipped
    for i in df['my_last_updated']:
      x = (str(i).split(' ')[0])
      date_part_1.append(x)

    df['my_last_updated'] =date_part_1
    #### Above column will convert the string data into a date data
    earlier_index = np.where(df['my_last_updated'] < '2000-00-00')
    df = df.drop(earlier_index[0]).reset_index(drop= True)
    df['my_last_updated'] = pd.to_datetime(df['my_last_updated'])
    


    #### unique users and corresponding anime data will be grouped and will be sorted as 
    #### function of time as ascendin order 
    x = df.set_index(['username','my_last_updated']).sort_index()
    #### grouped date will be converted into pandas dataframe with suitable indexes
    x = x.reset_index()
    x = x.drop(columns= ['my_last_updated'])  
    #### all animes were sorted as function of time and transposed according to username 
    df = x.groupby('username').aggregate(lambda tdf: tdf.unique().tolist())
    df = df.reset_index()
    
    ### users who watched less than min_len animes , has been dropped
    min_len = 5
    shorts = []
    for i,j in enumerate(df['anime_id']):
      if len(j) < min_len:
        shorts.append(i)

    df = df.drop(shorts).reset_index(drop=True)
    last_watches = []
    previous_watches = []
    for i in df['anime_id']:
      last_watches.append(i[-1])
      previous_watches.append(i[:-1])
    df['previous_watches'] = previous_watches
    df['last_watches'] = last_watches
    df = df.drop(columns = ['anime_id'])

    np_prev_w = []
    for i in  df['previous_watches'] :
      var1 = []
      for j in i:
        var1.append(int(j))
      np_prev_w.append(np.array(var1))

    df['previous_watches'] = np_prev_w
    return df 
df = data_prep(dir_url).prep()
df.head(2)













