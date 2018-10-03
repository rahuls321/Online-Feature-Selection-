# Source http://scikit-learn.org/stable/modules/model_evaluation.html#hamming-loss

from sklearn.metrics import hamming_loss
from sklearn.metrics import precision_score
from sklearn.metrics import zero_one_loss
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error, r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

y_pred = [1, 2, 3, 4]
y_true = [5, 6, 5,8]
 
print("Hamming Loss", hamming_loss(y_true, y_pred))

print("Accuracy_score", accuracy_score(y_true, y_pred))
#Used for Binary class
print("Precision_score:")
print("f1_score:")
# print(precision_score(y_true, y_pred))
# print(f1_score(y_true, y_pred))

#Used for multiclass
print("Zero_one_Loss:", zero_one_loss(y_true, y_pred))

# The best possible score is 1.0, lower values are worse.
print("Explained_variance_score:", explained_variance_score(y_true, y_pred))

print("Man_absolute_error:", mean_absolute_error(y_true, y_pred))

print("Mean_squared_log_error", mean_squared_log_error(y_true, y_pred))

print("Median_absolute_error", median_absolute_error(y_true, y_pred))

print("R2_score",r2_score(y_true, y_pred))

print("Confusion_matrix", confusion_matrix(y_true, y_pred))