# 📈 Logistic Regression
Description: Regression is a statistical method that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y or 'label' in machine learning) and a series of other variables (known as independent variables). 
Logistic Regression attempts to find the probability of an event taking place by having the log-odds for the event be a linear combination of one or more independent variables.
Logistic 
Regression is fitting the line values to the sigmoid curve. Loss Function for Logistic Regression is the Cross Entropy.

Steps:

1. Predict values using a sigmoid of the linear function, sigmoid(y) = sigmoid(wx + b) then initialize weights(w) and bias(b) as zero 
2. Find the weights and bias using a cost function which in logistic regression we use Cross Entropy Loss
   - Cross Entropy Loss = -ylog(yHat) - (1-y)log(1-yHat)
   - yHat = sigmoid( transpose(w) * x ) where weights and bias has been initialised usually equals to zero.
   - sigmoid(x) = 1/(1 + exp(-x)), graph is as shown below 
   
   ![sigmoid](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Logistic-Regression/sigmoid.png)
3. We want the error function to be as low as possible, so we find the minimum of our error function using derivative
4. Use gradient descent to get the minimum where
   - weights(n+1) = weights(n) - learning rate * derivative of MSE with respect to weights(df/dw)
   - bias(n+1) = bias(n) - learning rate * derivative of MSE with respect to bias(df/db)
5. After getting the minimum, then y_predicted = yHat with the updated weights and bias  

The expected output is to get the sigmoid curve to be able to estimate the maximum likelihood of a point as shown below
![result](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Logistic-Regression/result.jpeg)
