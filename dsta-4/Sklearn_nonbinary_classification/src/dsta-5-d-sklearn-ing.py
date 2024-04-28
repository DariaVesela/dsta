# -*- coding: utf-8 -*-
"""DSTA_5b_sklearn_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-SAXFfR6ZFtm9tWAsIhNS9M85N0WIFl0

# DSTA Lab 5-b: Classification with Scikit-learn

This notebook is available on Colab or from the [DSTA repo (download only)](https://www.dcs.bbk.ac.uk/~ale/dsta/)

Data is imported from the [Openml.org](https://openml.org/) public repository.

## Supervised Classification with the Python Scikit-learn module

### Slides and codes are courtesy of Andreas C. Mueller, NYU

Please see [Andreas C. Mueller](https://github.com/amueller/)

### Example: Exploratory classification of a blood transfusion dataset from Sklearn

The blood transfusion dataset is imported by Scikit-learn.
Check "fetch_openml" import sttement further below. 

Details about the dataset: [https://www.openml.org/d/1464](https://www.openml.org/d/1464).

### Package Imports
"""

import numpy as np
import pandas as pd

import sklearn
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.tree import export_graphviz

from subprocess import check_call

import matplotlib.pyplot as plt

"""### Matplotlib and Sklearn Settings Configuration"""

# Commented out IPython magic to ensure Python compatibility.
sklearn.set_config(print_changed_only=True)
# Toggle to 'False' if you want to see the default parameters 
# See example below

# %matplotlib inline
# Don't spawn external windows

"""### Fetch the dataset from sklearn

Package sklearn includes toy datasets for experimentation with machine learning models. One example is the blood transfusion dataset (please check the link at the top of this notebook). Below, the dataset is loaded as an sklearn object that has multiple attributes. The actual data (X, Y) are the "data" and "target" attributes of the object.
"""

# Fetch the data - provided as sklearn.utils.bunch class
blood = fetch_openml('blood-transfusion-service-center')

print(f"blood Python object type: {type(blood)}")
print(f"Attributes of blood Python object: {dir(blood)}")

"""### Check X and Y variable names and data size"""

print(f"X variable names: {blood.feature_names}")
print(f"Y variable names: {blood.target_names}")
print(f"X data size: {blood.data.shape}")

"""### Check the type of X , Y data

X is a pandas dataframe and Y is a pandas series. These are the core data structures of pandas package.
"""

print(f"Type of X data: {type(blood.data)}")
print(f"Type of Y data: {type(blood.target)}")

"""### Print the first 5 rows of the data"""

blood.data.head()

"""### Print the first 5 values of the target variable"""

blood.target.head()

"""### Check class distribution of Y"""

blood.target.value_counts()

"""### Use ``train_test_split`` to prepare your train and test data

As we see above, the class distribution is imbalanced...
Hint: Look for a "stratified" ``train_test_split``!

Package documentation: [sklearn train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
"""

X_train, X_test, y_train, y_test = train_test_split(
    blood.data, 
    blood.target, 
    random_state=0
    )

"""### Use ``StandardScaler`` from sklearn to standardize the predictors. 

Package documentation: [sklearn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

Otherwise, once ``StandardScaler`` has been imported, use ``help(StandardScaler)`` to print its documentation. You can use ``help`` Python command to check the documentation of any function or class.
"""

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""### Check class distribution in training and test Y.

Hint: The ``value_counts()`` method can help here
"""

print(f"Training Y class count: \n{pd.Series(y_train).value_counts()}\n")
print(f"Test Y class count: \n{pd.Series(y_test).value_counts()}")

"""### Use ``LabelEncoder`` from sklearn to encode target labels with values between 0 and n_classes-1.

Package documentation: [sklearn LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
"""

label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)
y_test = label_encoder.transform(y_test)

mappings = {label: i for i, label in enumerate(label_encoder.classes_)}
print(f"Label Encoder Mapping: {mappings}")

"""### Use again the ``shape`` function to check the dimensions of training and test X."""

print(X_train.shape)
print(X_test.shape)

"""# Classify with K-nn

### Check ``KNeighborsClassifier`` documentation of ask for help below.

Documenation: [sklearn KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
"""

help(KNeighborsClassifier)

"""### Fit K-nn model"""

myclassifier = KNeighborsClassifier(n_neighbors=5)
myclassifier.fit(X_train, y_train)

"""### Calculate K-nn training and test data accuracy"""

knn_train_accuracy = myclassifier.score(X_train, y_train)
knn_test_accuracy = myclassifier.score(X_test, y_test)

print(f"K-nn training data accuracy: {round(knn_train_accuracy, 3)}")
print(f"K-nn test data accuracy: {round(knn_test_accuracy, 3)}")

"""### Use Grid Search and Cross Validation to find the best number of neighbors

The default option of 5 fold cross validation is used (check the documentation!).

GridSearchCV documentation: [sklearn GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
"""

# Define parameter grid
num_neighbors = np.array([1, 3, 5, 8, 10, 15, 20, 25, 30])
param_grid = dict(n_neighbors=num_neighbors)

param_grid

# Initialize model
knn_model = KNeighborsClassifier()
grid = GridSearchCV(
    estimator=knn_model, 
    param_grid=param_grid,
    scoring="accuracy"
    )

# Run grid search
grid.fit(X_train, y_train)
best_n = grid.best_estimator_.n_neighbors
best_score = round(grid.best_score_, 3)

print(f"Best number of neighbors: {best_n}")
print(f"Best achieved test accuracy for {best_n} neighbors: {best_score}")

"""# Classify using Decision Trees

### Check ``DecisionTreeClassifier`` documentation of ask for help below.

Documenation: [sklearn DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
"""

help(tree.DecisionTreeClassifier)

"""### Train Decision Tree Classifier

Gini index is the default split criterion. Check the documentation!
"""

decision_tree = tree.DecisionTreeClassifier()
fitted_tree = decision_tree.fit(X_train, y_train)

"""### Calculate Decision Tree training and test data accuracy"""

tree_train_acc = fitted_tree.score(X_train, y_train)
tree_test_acc = fitted_tree.score(X_test, y_test)

print(f"Decision Tree training data accuracy: {round(tree_train_acc, 3)}")
print(f"Decision Tree test data accuracy: {round(tree_test_acc, 3)}")

"""### Plot the tree

Decision trees are great for explainability, but they suffer from high variance.

"""

export_graphviz(
    fitted_tree,
    out_file='dec_tree.dot',
    feature_names=blood.feature_names,
    rounded=True,
    filled=True
    )

# convert .dot to .pngfrom subprocess import check_call
check_call(['dot','-Tpng','dec_tree.dot','-o','dec_tree.png'])

# if pydot is installed use the below
!dot -Tpng dec_tree.dot -o dec_tree.png -Gdpi-600

# Read and display the figure

plt.figure(figsize = (18, 26))
plt.imshow(plt.imread('dec_tree.png'))
plt.axis('off');
plt.show();

"""# In-class Exercise


Load the iris dataset from the ``sklearn.datasets`` module using the ``load_iris`` function or continue with the blood transfusion dataset already loaded. 
If you decide to work with Iris, split it into training and test set using ``train_test_split``.

Then train and evaluate ``sklearn.linear_model.LogisticRegression`` on the chosen dataset. How does it perform on the training set vs. the test set? 

If time allows, train and evaluate an ``sklearn.ensemble.RandomForestClassifier`` on the chosen dataset. Check again how it performs on the training set vs. the test set.

# Take-home Exercise 1 (discretionary)

Can you construct a binary classification dataset (using np.random for example) on which ``sklearn.linear_model.LogisticRegression`` achieves an accuracy of 1?

# Take-home Exercise 2 (discretionary)

Can you construct a binary classification dataset on which it achieves accuracy 0.5?
"""