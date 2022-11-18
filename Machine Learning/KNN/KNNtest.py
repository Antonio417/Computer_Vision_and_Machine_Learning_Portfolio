from KNN import KNN
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Plotting inital data
cmap = ListedColormap(['#F00F00', '#00FF00', '#0000FF'])
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

print(X_train.shape) # 120 samples with 4 features 
print(X_train[0])
print(y_train.shape) # 1D row vector of size 120 (label for our training sample)
plt.figure()
plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap, edgecolors='k', s=20)
plt.show()

classifier = KNN(k=3)
classifier.fit(X_train,y_train)
predictions = classifier.predict(X_test)
acc = np.sum(predictions == y_test) / len(y_test) # Accuracy = probability of getting the right predictions
print("KNN classification accuracy", acc) 