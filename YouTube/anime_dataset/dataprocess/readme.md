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

3.4 LABEL and CONTEXT SELECTION :



