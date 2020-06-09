### Project Overview

 This project is based on Linear Regression model. through this project we predicted the price of a new lego product before its price is realeased using a linear regression model.


### Learnings from the project

 After completing this project, I have a better understanding of how to build a linear regression model. In this project, the following concepts were applied-

Train-test split
Correlation between the features
Linear Regression
MSE and R2 Evaluation Metrics


### Approach taken to solve the problem

 Data loading and splitting : Loading the dataset and splitting the data into train and test.
Scatter plot : check the scatter_plot for different features vs target variable list_price. This tells us which features are highly correlated with the target variable list_price and help us predict it better.
Remove highly correlated columns : Features highly correlated with each other adversely affect our lego pricing model. Thus we keep a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.
Make prediction : Intialize the model and make prediction . To check the predictions are accurate calculate r2 error make sure r2 error should be greater than 0.5.
Calculate Residues : To check how much difference is present between train values and predicted values .


### Challenges faced

 I faced a few syntax errors which I resolved through re-evaluation of the codes.


### Additional pointers

 It was a very informative and knowledgeable project.


