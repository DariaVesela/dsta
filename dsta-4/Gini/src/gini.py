# Baseline implementation of a Decision-tree classifier
# it uses Gini to measure purity of the segments.

# Line 171: define the location of your data: filename="./uci-data_banknote_authentication.csv"

# Line 89: implement function gini_index(groups, classes):

# requires the dataset in the same folder
# or adapt line 169 accordingly

# v. 3 by Ale,  2021
# v. 2 by Abul, 2020
# v. 1 by Alan, 2019
#----------------------------------------
from random import seed
from random import randrange
from csv import reader


# Load a CSV file
def load_csv(filename):
	file = open(filename, "r")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
  dataset_split = list()
  dataset_copy = list(dataset)
  fold_size = int(len(dataset) / n_folds)
  # for i in range(n_folds):
  #   fold = list()

  #   while len(fold) < fold_size:
  #     index = randrange(len(dataset_copy))
  #     fold.append(dataset_copy.pop(index))

  #   dataset_split.append(fold)
	
  #   return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	
    for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
	
    	for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
	
    	predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	
    return scores

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

def gini_index(groups, classes):
    # TODO: implement this function to calculate the Gini IndexError
    # count all samples at split point
    # sum weighted Gini index for each group
    # score the group based on the score for each class
    # weight the group score by its relative size

    gini=0
    
    return gini

# Select the best split point for a dataset
def get_split(dataset):
    # TODO: find the best possible place to split the dataset
    pass

# Create a terminal node value
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	
    # check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return

	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	
    # process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	
    # process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
	root = get_split(train)
	split(root, max_depth, min_size, 1)
	return root

# Make a prediction with a decision tree
def predict(node, row):
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']

# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):
	tree = build_tree(train, max_depth, min_size)
	predictions = list()
	for row in test:
		prediction = predict(tree, row)
		predictions.append(prediction)
	return(predictions)


def main(ifname):
    dataset = load_csv(filename)
    # convert string attributes to integers
    for i in range(len(dataset[0])):
        str_column_to_float(dataset, i)
    #print(dataset)
    # evaluate algorithm
    n_folds = 5
    max_depth = 5
    min_size = 10
    scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))

if __name__ == '__main__':
    try:
        filename="./uci-data_banknote_authentication.csv"
        main(filename)
    except IndexError:
        print(
            "[ERROR] Please give the data-file location as the first argument.")