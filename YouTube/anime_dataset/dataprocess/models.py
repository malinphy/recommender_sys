import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import Model,layers,Input
from tensorflow.keras.layers import *

def ret_model(SEQUENCE_LEN,EMBEDDING_DIM,BATCH_SIZE,NUM_EPOCHS,num_unique_movies):
    movie_inp = Input(shape =(SEQUENCE_LEN-1,), name='item_input')
    occ_inp = Input(shape =(1,), name='occ_input')
    gen_inp = Input(shape =(1,), name='gender_input')
    age_inp = Input(shape =(1,), name='age_input')
    zip_code_inp = Input(shape =(1,), name='zip_code_input')

    emb_layer = Embedding(num_unique_movies+1, EMBEDDING_DIM)(movie_inp)
    flat_layer = Flatten(name = 'flatten_layer')(emb_layer)
    concat_layer = tf.keras.layers.Concatenate(axis=1)([flat_layer,occ_inp,gen_inp,age_inp,zip_code_inp])
    d1 = Dense(256*4, activation = 'relu' , name = 'd1_layer')(concat_layer)
    d2 = Dense(256*2, activation = 'relu', name = 'd2_layer')(d1)
    d3 = Dense(256*1, activation = 'relu', name = 'd3_layer')(d2)
    final = Dense(num_unique_movies, activation = 'softmax', name = 'softmax_layer')(d3)

    return Model(inputs = [movie_inp,occ_inp,gen_inp,age_inp,zip_code_inp], outputs = final)
    
    
def rank_model(EMBEDDING_DIM,num_unique_movies_rank):
    user_id_inp_rank =  Input(shape =(1,), name='user_id_input_rank')
    movie_inp_rank = Input(shape =(1,), name='movie_input_rank')
    release_year_inp_rank = Input(shape =(1,), name='release_year_input_rank')
    # gen_inp = Input(shape =(1,), name='gender_input')
    # age_inp = Input(shape =(1,), name='age_input')
    # zip_code_inp = Input(shape =(1,), name='zip_code_input')

    emb_layer = Embedding(num_unique_movies_rank+1, EMBEDDING_DIM)(movie_inp_rank)
    flat_layer = Flatten(name = 'flatten_layer')(emb_layer) 
    concat_layer = tf.keras.layers.Concatenate(axis=1)([flat_layer,release_year_inp_rank])
    d1 = Dense(256*4, activation = 'relu' , name = 'd1_layer')(concat_layer)    
    d2 = Dense(256*2, activation = 'relu', name = 'd2_layer')(d1)
    d3 = Dense(256*1, activation = 'relu', name = 'd3_layer')(d2)
    final = Dense(1, activation = 'sigmoid', name = 'sigmoid_layer')(d3)

    return  Model(inputs = [user_id_inp_rank,movie_inp_rank,release_year_inp_rank], outputs = final)