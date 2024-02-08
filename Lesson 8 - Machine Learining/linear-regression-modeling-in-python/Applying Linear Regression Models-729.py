## 1. Introduction ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

auto = pd.read_csv('automobiles.csv')

X = auto.drop(['normalized_losses'], axis=1)
y = auto['normalized_losses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=729)

## 2. Test Error ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 729)

model = LinearRegression()

X_train_subset = X_train[['length', 'engine_size']]
X_test_subset = X_test[['length', 'engine_size']]

model.fit(X_train_subset, y_train)

train_pred = model.predict(X_train_subset)
test_pred = model.predict(X_test_subset)

train_mse = mean_squared_error(y_train, train_pred)
test_mse = mean_squared_error(y_test, test_pred)

train_rmse = mean_squared_error(y_train, train_pred, squared=False)
teat_rmse = mean_squared_error(y_test, test_pred, squared=False)

## 3. Feature Selection And Correlation ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 729)

auto_corr = auto.corr()

## 4. More Complex Predictors ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 729)

X_train["length_squared"] = X_train["length"] ** 2
X_test["length_squared"] = X_test["length"] ** 2

X_train_subset = X_train[["length", "length_squared"]]
X_test_subset = X_test[["length", "length_squared"]]

model = LinearRegression()
model.fit(X_train_subset, y_train)

train_predictions = model.predict(X_train_subset)
test_predictions = model.predict(X_test_subset)

train_mse = mean_squared_error(y_train, train_predictions)
test_mse = mean_squared_error(y_test, test_predictions)

## 5. Outcome Transformations ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 729)

X_train["length_squared"] = X_train["length"] ** 2
X_test["length_squared"] = X_test["length"] ** 2

X_train_subset = X_train[['length']]
X_test_subset = X_test[['length']]

y_train_log = np.log2(y_train)
y_test_log = np.log2(y_test)

model = LinearRegression()
model.fit(X_train_subset, y_train_log)

train_predictions = model.predict(X_train_subset)
test_predictions = model.predict(X_test_subset)

train_mse = mean_squared_error(y_train_log, train_predictions)
test_mse = mean_squared_error(y_test_log, test_predictions)

## 6. The Box-Cox Transformation ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.stats import boxcox

auto = pd.read_csv("automobiles.csv")
X = auto.drop(["normalized_losses"], axis = 1)
y = auto["normalized_losses"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 729)

auto['normalized_losses'].hist()
plt.show()

auto['log_norm_losses'] = boxcox(auto['normalized_losses'], lmbda=0)
auto['log_norm_losses'].hist()
plt.show()

auto['boxcox_norm_losses'] = boxcox(auto['normalized_losses'])[0]
auto['boxcox_norm_losses'].hist()
plt.show()