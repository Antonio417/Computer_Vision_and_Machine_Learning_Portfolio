import numpy as np
from collections import Counter

class Node:
    def __init__(self,left=None, right=None, feature=None,threshold=None,*, value=None):
        self.left = left
        self.right = right
        self.feature = feature
        self.threshold = threshold
        self.value = None
   
    def is_leaf_node(self):
        return  self.value is not None

class DecisionTree:
    def __init__(self, min_split=2, max_depth=100, n_features=None):
        self.min_split = min_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, x, y):
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(x, y)

    def _grow_tree(self, x, y, depth):
        n_samples, n_feats = x.shape
        n_labels = len(np.unique(y))
        
        # check stopping criteria
        if(depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value =  self._most_common_label(y)
            return Node(value = leaf_value)

        feat_idx = np.random.choice(n_feats, self.n_features, replace=False)

        # Find best split
        best_threshold, best_feature = self._best_split(self, x, y, feat_idx)
        
        # create child nodes
        left_idxs, right_idxs = self._split(x[:, best_feature], best_threshold)
        left = self._grow_tree(x[left_idxs,:], y[left_idxs,:], depth+1)
        right = self._grow_tree(x[right_idxs,:], y[right_idxs,:], depth+1)
        return Node(left, right, best_feature, best_threshold)


    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value
    
    def _best_split(self, x, y, feat_idx):
        best_gain_value = -1
        split_thresh, split_idx = None, None

        for indexes, in feat_idx:
            x_col = x[:, indexes]
            thresh = np.unique(x_col)
            
            for thresholds in thresh:
                # calculate info gain
                gain = self._info_gain(y, x_col, thresholds)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = indexes
                    split_thresh = thresholds
        return  split_thresh, split_idx
    
    def _info_gain(self, y, x_col, thresholds):
        # parent entropy
        parent_entropy = self._entropy(y)

        # create children
        left_idx, right_idx = self._split(x_col, thresholds)

        if len(left_idx) == 0 or len(right_idx) == 0:
            return 0

        # calculate weighted entropy of children
        n = len(y)
        n_left, n_right = len(right_idx), len(left_idx) 
        # entropy
        e_left, e_right = self._entropy(y[left_idx]), self._entropy(y[right_idx])
        child_entropy =(n_left/n) * e_left + (n_right/n) * e_right

        # calculate info gain
        info_gain = parent_entropy - child_entropy
        return info_gain

    def _split(self, x_col, split_thresholds):
        left_idx = np.argwhere(x_col <= split_thresholds).flatten()
        right_idx = np.argwhere(x_col > split_thresholds).flatten()
        return left_idx, right_idx

    def _entropy(self, y):
        hist = np.bincount(y)
        prob  = hist/len(y)
        return -np.sum([i * np.log(i) for i in prob if i > 0])



    def predict(self):

