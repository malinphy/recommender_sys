3.1 Recommendation as classification:

The task of the deep neural network is to learn user embeddings u as 
a function of the user's history and context that are usefil for discriminating 
among videos with a softmax classifier.
Althou explicit feedback mechanisms exist on YouTube we user the 
implicit feed back.

Efficient Extreme multiclass

To efficiently train such a model with millions of classes, we rely on a 
technique to sample negative classes form backfround disribution ('candidate sampling)
and then correct for this sampling via importance weighting.
At serving time we ned to compute the most likely N classes (videos)
in order to choose the top N to present the user.
3.2 MODEL ARCHITECTURE  
Features are concatenated into a wide first layer, followed by several layers
of fully connected ReLU. 
3.3 HETEROGENEOUS SIGNALS
A key advantage of using deep neural networds as generalization of matrix 
factorization is thta arbitrary contininous and categorical features can be easily
added to the model.

3.5 EXPERIMENTS WITH FEATURES AND DEPTH :
The softmax layer outputs a multinomial distribution over the same 1M video classes with a dimension 
of 256. 

4.1 Feature representation:
An axample of univalent categorical feature is the video ID of the impression
being scored , while a corresponding multivalent feature might be a bog of the 
last N vide IDs the user has watched.  We also classify features according to 
whether they describe properties of the item ('impression') or properties of 
the user/context ('query'). Query features are computed once per request while
impression features are computed for each item scored.

Feature Engineering

The main challenge is in representing a temporal sequence of user action and 
how these actions relate to video impression being scored. 
WE OBSERVE THAT MOST IMPORTANT SIGNALS ARE THOSE THAT DESCRIBE A USER'S PREVIOUS
INTERACTION WITH THE ITEMS ITSELF AND OTHER SIMILAR ITEMS, MATCHING OTHER'S 
EXPERIENCE IN RANKING ADS. ???
	As an example, consider the user's past history with the channel that
	uploaded the video being scored- how manu videos has the user watched 
	from this channel ? When was the last time the user watched a video 
	on this topic ?
we have also fount it crucial to propagate information from candidate generation 
into ranking in form of features, e.g. which sources nominated this video 
candidate? What scores did they assign?

Embedding Categorical Features 

Similar to candidate generation, we use embeddings to map sparse categorical 
features to dense representation suitable for neural networks. 
Each unique ID space ('vocabulary') has a seperate learned embedding with dimension 
that increases approximately proportinal to the algorithm of the number of unique values. 
Very large cardinality ID spaces (e,g, video IDs or serach query terms) are 
truncated by including only the top N after sorting based on their frequency
in clicked impressions. As in candidate generation, multivalent categorical 
feature embeddings are averaged before fed into the network. Importantly, categorical
features in the same ID space also share underlying embeddings. Despote the 
shared embedding, eah fetaure is fed seperatly into the network so that layers above
can learn specialized representations per feature. 

Normalizing Continuous Features:
NNs are sensitive to the scalng and distribution of their inputs. A continious feature
X with distiribution f is transformed to X by scaling the values such that the feature
is equally distributed in [0,1)  using the cumulative distribution.


