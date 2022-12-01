# 📊 Support Vector Machine
Description: an algorithm where a linear model is used to find a hyperplane that best separates the data.
The best hyperplane is the one that represents the largest separation between the two classes.

The hyperplane used must satisfied the conditions below

- Wx - b = 0 and y(Wx - b) >= 1 where W = weights, b = Bias and y is the class.
- A cost function is used to determine the weights and bias.
- loss = lambda*magnitude(W) + 1/n * sum(max(0, 1 - y(Wx - b))) called the Hinge Loss
- loss = lambda*magnitude(W), IF y.f(x)>= 1
- loss = lambda*magnitude(W) + 1 - f(x),    Otherwise
- Where f(x) = y(Wx - b)
- The margin between the two classes = 2/magnitude(W) so W must be minimise in order to get the maximum margin.
- gradient descent is used to minimise it 
- update rule : w = w - learning rate * dw and b = b - learning rate * db

The algorithm is as shown below

       
       
