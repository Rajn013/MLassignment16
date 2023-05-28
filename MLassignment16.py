#!/usr/bin/env python
# coding: utf-8

# 1. In a linear equation, what is the difference between a dependent variable and an independent variable?
# 

# A linear equation in two variables can be described as a linear relationship between x and y, that is, two variables in which the value of one of them (usually y) depends on the value of the other one (usually x). In this case, x is the independent variable, and y depends on it, so y is called the dependent variable.

# 2. What is the concept of simple linear regression? Give a specific example.
# 

# We could use the equation to predict weight if we knew an individual's height. In this example, if an individual was 70 inches tall, we would predict his weight to be:
# 
# Weight = 80 + 2 x (70) = 220 lbs.
# 
# In this simple linear regression, we are examining the impact of one independent variable on the outcome.

# 3. In a linear regression, define the slope.
# 

# The vertical distance divided by the horizontal distance between any two points on the line.

# 4. Determine the graph's slope, where the lower point on the line is represented as (3, 2) and the higher point is represented as (2, 2).
# 

# In[7]:


x1, y1 = 3, 2
x2, y2 = 2, 2

slope = (y2 - y1) / (x2 - x1)
print("The slope of the line is:", slope)


# 5. In linear regression, what are the conditions for a positive slope?
# 

# if the slope is positive, y increases as x increases, and the function runs "uphill" (going left to right). If the slope is negative, y decreases as x increases and the function runs downhill. If the slope is zero, y does not change, thus is constant—a horizontal line.

# 6. In linear regression, what are the conditions for a negative slope?
# 

# If the slope is negative, y decreases as x increases and the function runs downhill. If the slope is zero, y does not change, thus is constant—a horizontal line.

# 7. What is multiple linear regression and how does it work?
# 

# Multiple linear regression refers to a statistical technique that uses two or more independent variables to predict the outcome of a dependent variable. The technique enables analysts to determine the variation of the model and the relative contribution of each independent variable in the total variance.

# 8. In multiple linear regression, define the number of squares due to error.
# 

# In multiple linear regression, the sum of squares due to error (SSE) represents the total variation in the dependent variable (response variable) that is not explained by the linear regression model. It quantifies the discrepancy between the observed values and the predicted values from the regression model.

# 9. In multiple linear regression, define the number of squares due to regression.
# 

# In multiple linear regression, the sum of squares due to regression (SSR) represents the total variation in the dependent variable (response variable) that is explained by the linear regression model. It quantifies how well the regression model fits the data.

# In a regression equation, what is multicollinearity?
# 

# 
# Multicollinearity in a regression equation refers to a situation where two or more predictor variables are highly correlated with each other. It can lead to unstable and unreliable estimates of regression coefficients and makes it challenging to interpret the individual effects of each predictor variable. 

# 11. What is heteroskedasticity, and what does it mean?
# 

# Heteroskedasticity refers to a situation in regression analysis where the variability of the errors (residuals) in a regression model is not constant across all levels of the predictor variables. In other words, the spread or dispersion of the residuals differs systematically as the values of the independent variables change.

# 12. Describe the concept of ridge regression.
# 

# Ridge regression is a model tuning method that is used to analyse any data that suffers from multicollinearity. This method performs L2 regularization. When the issue of multicollinearity occurs, least-squares are unbiased, and variances are large, this results in predicted values being far away from the actual values.

# 13. Describe the concept of lasso regression.
# 

# Lasso regression algorithm is defined as a regularization algorithm that assists in the elimination of irrelevant parameters, thus helping in the concentration of selection and regularizes the models. Lasso models can be evaluated using various metrics such as RMSE and R-Square.

# 14. What is polynomial regression and how does it work?
# 

# Polynomial Regression is a form of regression analysis in which the relationship between the independent variable x and the dependent variable y is modelled as an nth degree polynomial in x

# 15. Describe the basis function.
# 

# In mathematics, a basis function is an element of a particular basis for a function space. Every function in the function space can be represented as a linear combination of basis functions, just as every vector in a vector space can be represented as a linear combination of basis vectors.

# 16. Describe how logistic regression works.
# 

# Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.

# In[ ]:




