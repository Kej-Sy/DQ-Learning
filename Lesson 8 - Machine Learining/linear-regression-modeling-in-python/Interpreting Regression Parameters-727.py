## 1. Introduction ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv('automobiles.csv')
print(auto.info())

X = auto.drop(['normalized_losses'], axis=1)
y = auto['normalized_losses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=727)

## 2. The LinearRegression Object ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 727)

model = LinearRegression()

## 3. Fitting a LinearRegression Object ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 727)

model = LinearRegression()
X = X_train[['length', 'engine_size']]
model.fit(X, y_train)