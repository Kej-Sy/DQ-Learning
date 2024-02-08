## 1. Introduction ##

import pandas as pd
import numpy as np

## 2. Examining The Data ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv('automobiles.csv')
auto.info()
print(auto.head())

X = auto.drop('normalized_losses', axis=1)
y = auto['normalized_losses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=726)

## 4. Types of Predictors ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 726)

auto_with_dummies = pd.get_dummies(auto, columns=['drive_wheels'])

## 5. The Cost Function ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 726)

beta0 = 5
beta1 = 3
beta2 = 2

se = (y_train - (beta0 + beta1*X_train['length'] + beta2*X_train['engine_size']))**2

sse = sum(se)

## 6. Estimating the Best Coefficients ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 726)

X_train_subset = X_train[['length', 'engine_size']]
X_train_subset['intercept'] = 1

X_trans = np.transpose(X_train_subset)
X_mat = np.matmul(X_trans, X_train_subset)
XX_inv = np.linalg.inv(X_mat)

XY = np.matmul(X_trans, y_train)

beta_hat = np.matmul(XX_inv, XY)