from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject
from matplotlib.pyplot import yticks
from scipy.stats.stats import describe

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
googleData["trump"] = GoogleParser("trend_trump.txt").buildDataFrame()
tiingoData = TiingoParser("data.json").buildDataFrame()


print(googleData["tax"].describe())
print(tiingoData.describe())

#Plotting works
'''
googleData["trump"].plot()

googleData["tax"].plot()

tiingoData['close'].plot()
tiingoData['close'].set_xticks=tiingoData['date']
'''

#Declare inputs and target
googleTrump = googleData["trump"]
target = tiingoData["close"]

#Split data
inputs=googleTrump[["value"]]
x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size = 0.4)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

#Train and test using KNN
from sklearn.neighbors import KNeighborsClassifier
k = 5
testing = KNeighborsClassifier(k)
testing.fit(x_train, y_train)
testing.predict(inputs)
testing.score(x_test, y_test)








