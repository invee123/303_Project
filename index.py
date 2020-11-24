from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject
from matplotlib.pyplot import yticks
from scipy.stats.stats import describe
import pandas as pd

from google_parser import TrendParser as GoogleParser
from tiingo_parser import TrendParser as TiingoParser

import matplotlib.pyplot as plt
import sklearn as sk
import numpy as np
from sklearn.model_selection import train_test_split

# Fetch data
success = muterun_js('index.js')

if success:
    print('Index.js successfully run')
else:
    print("i hate node w/ python")



# Set up dataframes
googleData = {}
googleData["tax"] = GoogleParser("trend_tax.txt").buildDataFrame()
googleData["trump"] = GoogleParser("trend_trump.txt").buildDataFrame(dataColumns=["value","time"])
tiingoData = TiingoParser("data.json").buildDataFrame()

tiingoData.drop(tiingoData.tail(1).index, inplace=True)

#print(result.describe())
#Plotting works
'''
googleData["trump"].plot()

googleData["tax"].plot()

tiingoData['close'].plot()
tiingoData['close'].set_xticks=tiingoData['date']
'''

data = { "time" : googleData["tax"]["time"], "tax_value" : googleData["tax"]["value"], "trump_value" : googleData["trump"]["value"], "tiingo_volume" : tiingoData["volume"], "tiingo_close" : tiingoData["close"] }
df = pd.DataFrame(data=data)

inputs = df[["tax_value", "trump_value", "tiingo_volume"]]
target = df["tiingo_close"].astype("int")


#Declare inputs and target
#googleTrump = googleData["trump"]
#target = tiingoData["close"]

#Split data
#inputs=googleTrump
x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size = 0.4)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression
#create a model object
model = LogisticRegression()
#train our model
model.fit(x_train, y_train)
logregPredictY = model.predict(x_test)
print("Logistic Regression Fit accuracy:", model.score(x_test, y_test))

#Train and test using KNN
from sklearn.neighbors import KNeighborsClassifier
k = 5
testing = KNeighborsClassifier(k)
testing.fit(x_train, y_train)
testing.predict(inputs)
print("KNN Fit accuracy:", testing.score(x_test, y_test))

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(x_train,y_train)
reg.predict(inputs)
print("Linear Regression Fit accuracy:", reg.score(x_test, y_test))
