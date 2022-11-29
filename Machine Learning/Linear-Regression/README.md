# 📈 Linear Regression
Description: Regression is a statistical method that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y or 'label' in machine learning) and a series of other variables (known as independent variables). Linear regression attempts to find the line (or a more complex linear combination) that most closely fits the data according to a specific mathematical criterion. In layman terms, it tries to find the line of best fit in a 2D data.

Steps:

1. Predict Values using a linear function y = wx + b, initialize weights(w) and bias(b) as zero 
2. Find the weights and bias using a cost function which in linear regression we use Mean-Squared Error(MSE)
   - MSE = (1/number of sample) * sum( (actual value(y) - predicted value(yHat))^2 ) 
   - yHat = wx + b where weights and bias has been initialised usually equals to zero.
3. We want the MSE function to be as low as possible, so we find the minimum of our error function using derivative
4. Use gradient descent to get the minimum where
   - weights(n+1) = weights(n) - learning rate * derivative of MSE with respect to weights(df/dw)
   - bias(n+1) = bias(n) - learning rate * derivative of MSE with respect to bias(df/db)
5. After getting the minimum, then y_predicted = wX + b with the updated weights and bias  

The expected output is an equation for a line as shown below
![img1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Linear-Regression/Linear_Regression.png)
