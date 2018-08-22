# Online-Feature-Selection-
Feature Selection using Mutual Information for High Dimensional DataSets
### Introduction to Feature Selection

It is possible to automatically select those features in your data that are most useful or most relevant for the problem you are working on. 
This is a process called feature selection. It is also called variable selection or attribute selection.

##### Two Broader Categories
- **Filter Method**: 
Filter feature selection methods apply a statistical measure to assign a scoring to each feature. The features are ranked by the score and 
either selected to be kept or removed from the dataset. The methods are often univariate and consider the feature independently, or with regard to the dependent variable. 
This method is faster and computational more efficient than Wrapper. It doesn't depend on learning algorithm.

- **Wrapper Method**:
Wrapper methods consider the selection of a set of features as a search problem, where different combinations are prepared, evaluated and compared to other combinations. 
A predictive model us used to evaluate a combination of features and assign a score based on model accuracy.It needs one predetermined learning algorithm in Feature Selection 
and utilizes, its performance to evaluate and determine selected features.


### Mutual Information
It is a measure between two(possibly multi-dimensional) random variables X and Y, that quantifies the amount of information obtained about one random variable, 
through the other random variable.

Mutual information(MI) is given by ![this formula](http://mistic.leloir.org.ar/docs/MIformula.png)

If X and Y are are comletely independent with each other then **MI = 0**.
We would like to maximise the MI between subset of selected features X<sub>s</sub> and the target variable y.

> S = arg max MI(X<sub>s</sub>; y)  |S| = k

k is the no. of features we want to select. S is called joint mutual information and maximising this quantity is an **NP-Hard Optimisation Problem**


### Entropy
Measure of uncertainity of random variable. It always related with random variable rather than actual variable.
Entropy is given by ![this formula](https://4.bp.blogspot.com/-79mxfloJ-a0/WacWFEZVx4I/AAAAAAAA6Gk/Fhz1A0DBaNYRGxNbbU3c9LsDUqWvyUqUwCLcBGAs/s1600/shannon_equation.jpg)

Here p(x) is the probability mass function 

### Information Gain 
Amount of which entropy of **a** decreases reflects the additional information about **a** provided by **T**.

![IG](http://l830524.weebly.com/uploads/7/4/0/3/74035531/4678421_orig.jpg)

Amount of information gained about **a** after observing **T** is equal to amount of information gained about **T** after observing **a**.

### Symmetrical Uncertainity
Correlation measure between two variables (i.e two features) is given by 

![this formula](https://raw.githubusercontent.com/rahuls321/Online-Feature-Selection-/master/su.png)
