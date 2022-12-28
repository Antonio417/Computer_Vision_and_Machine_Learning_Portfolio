# 🌲 Decision Tree 
Description: Decision trees are used in data analytics and machine learning to break down complex data into more manageable parts. A decision tree is a flowchart-like structure in which each internal node represents a test on a feature (e.g. whether a coin flip comes up heads or tails) , 
each leaf node represents a class label (decision taken after computing all features) and branches represent conjunctions of features that lead to those class labels. 
The paths from root to leaf represent classification rules. Below diagram illustrate the basic flow of decision tree for decision making with labels (Rain(Yes), No Rain(No)). 

<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Decision-Tree/treeExample.png" width="500" height="400" />


Training Steps:

1. Calculate information gain with each possible split
2. Divide set with that feature and value that gives the most information gain
3. Divide tree and do the same for all created branches until a stopping criteria is reached

Test Steps:

1. Follow the tree until we reached the leaf node
2. Return the most common label

The tree for a bag of marbles as an example are built as shown below:

![tree](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Decision-Tree/decisionTree.gif)
