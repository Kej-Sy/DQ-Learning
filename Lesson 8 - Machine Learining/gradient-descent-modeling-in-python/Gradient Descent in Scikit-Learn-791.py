## 2. SGD in Scikit-learn ##

sgdr = SGDRegressor(learning_rate='constant',
                    eta0=0.0001, 
                    tol=0.0001, 
                    max_iter=25)
sgdr.fit(X_train, y_train)
y_pred = sgdr.predict(X_test)

sgdr_mse = mean_squared_error(y_test, y_pred)

## 4. Applying SGD ##

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

ow = pd.read_csv('overweight_dataset.csv')

X_train, X_test, y_train, y_test = train_test_split(ow[['Height']], ow[['Weight']])

scaler = StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

sgdr = SGDRegressor(tol=0.0001, eta0 = 0.0001, max_iter=10000)
sgdr.fit(X_train, y_train)

y_pred = sgdr.predict(X_test)

rmse = mean_squared_error(y_test, y_pred,  squared=False)
print(rmse)

## 6. SGD for Classification ##

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

sgdc = SGDClassifier(class_weight = 'balanced')
sgdc.fit(X_train, y_train)

y_pred = sgdc.predict(X_test)

report = classification_report(y_test, y_pred)

print(report)