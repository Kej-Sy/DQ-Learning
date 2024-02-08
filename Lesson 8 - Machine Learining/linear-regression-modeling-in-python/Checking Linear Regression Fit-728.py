## 1. Introduction ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto = pd.read_csv('automobiles.csv')

X = auto.drop(['normalized_losses'], axis=1)
y = auto['normalized_losses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=728)

## 2. Calculating Residuals ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 728)

model = LinearRegression()

X_train_subset = X_train[['length', 'width']]

model.fit(X_train_subset, y_train)

predictions = model.predict(X_train_subset)

residuals = y_train - predictions

## 3. Checking The Residual Mean ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 728)

model = LinearRegression()
X_train_subset = X_train[["length", "width"]]
model.fit(X_train_subset, y_train)

predictions = model.predict(X_train_subset)
residuals = y_train - predictions

residual_mean = residuals.mean()

## 6. Checking The Sum of Squared Errors ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 728)

model = LinearRegression()
X_train_subset = X_train[["length", "width"]]
model.fit(X_train_subset, y_train)

predictions = model.predict(X_train_subset)
residuals = y_train - predictions
training_mse = mean_squared_error(y_train, predictions)
training_rmse = mean_squared_error(y_train, predictions, squared=False)

## 7. The Coefficient of Determination ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 728)

model = LinearRegression()
X_train_subset = X_train[["length", "width"]]
model.fit(X_train_subset, y_train)

predictions = model.predict(X_train_subset)
residuals = y_train - predictions

R2 = r2_score(y_train, predictions)