kaggle_link = https://www.kaggle.com/azathoth42/myanimelist

NCF notes
Evaluating the model

The paper uses top@K for evaluation so we’ll be using the same here.
The idea is to remove one of the known positive interactions for a 
user and then check if that item is present in the top K recommended items.
So say we set K=10 we can get a percentage of how often our known but 
“removed” items would be recommended if we showed the user 10 
recommendations. It does not, however, take into account where in that batch
of 10 the item appeared. What value we use for K here is a bit arbitrary, 
but if we were developing a recommender for use in a real implementation 
where the UI only shows the user say 5 recommended items we should, of 
course, use K=5 to model the real world conditions.

Once we have our data loaded and in the format wee want we pslit it into a 
train and a test sets. For the test set, we select the latest interaction 
for every user (the holdout item) and remove that interaction from our 
training data. We also sample 100 negative interactions for each user and 
add thse to our test data. the reasor for this is to avoid ranking every 
item in our dataset when we do our evaluation. Instead, we will rank these
101 items and check if our holdout was among the K highesest ranked ones.

We first define get_train_instances. This function samples a number of 
negative (unknown) interactions for every known user-item interactio in 
our training data. In this example, we get 4 negative interaction for each 
positive one.

dataprep:
Once we have our data loaded and in the format we want we split it into a
train and a test sets. For the test set, we select the latest interaction 
for every user (the holdout item) and remove that interaction from our 
training data. We also sample 100 negative interactions for each user and 
add these to our test data. The reason for this is to avoid raking every 
item in our dataset when we do our evaluation. Instead, we will rank these 
101 items and check if our holdout was among the K highest ranked ones.

We first define get_train_instances. This function samples a number of 
negative (unknown) interactions for every known user-item interaction in 
our training data. In this example, we get 4 negative interactions for each 
positive one. We then also define random_mini_batches used to generate 
randomized batches of size 256 during training.
