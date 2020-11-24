#from Naked.toolshed.shell import execute_js, muterun_js
#from Naked.toolshed.types import NakedObject
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
#success = muterun_js('index.js')
success = True

if success:
    print('Index.js successfully run')
else:
    print("i hate node w/ python")



# Set up dataframes
googleData = {}
googleData["tax"] = GoogleParser("trend_tax.txt").buildDataFrame()
googleData["trump"] = GoogleParser("trend_trump.txt").buildDataFrame()
googleData["google"] = GoogleParser("trend_google.txt").buildDataFrame()
googleData["youtube"] = GoogleParser("trend_youtube.txt").buildDataFrame()
googleData["amazon"] = GoogleParser("trend_amazon.txt").buildDataFrame()
googleData["android"] = GoogleParser("trend_android.txt").buildDataFrame()

tiingoData = TiingoParser("data.json").buildDataFrame()

tiingoData.drop(tiingoData.tail(1).index, inplace=True)


#Declare inputs and target

data = { "time" : googleData["tax"]["time"],
    "tax_value" : googleData["tax"]["value"], 
    "trump_value" : googleData["trump"]["value"],
    "google_value" : googleData["google"]["value"],
    "youtube_value" : googleData["youtube"]["value"],
    "amazon_value" : googleData["amazon"]["value"],
    "android_value" : googleData["android"]["value"],
    "tiingo_volume" : tiingoData["volume"], 
    "tiingo_close" : tiingoData["close"] }

df = pd.DataFrame(data=data)

#inputs = df[["tax_value", "trump_value", "tiingo_volume"]]
#inputs = df[["amazon_value", "android_value"]]
#inputs = df[["tax_value", "trump_value", "youtube_value"]]
#inputs = df[["tax_value", "trump_value", "tiingo_volume", "android_value"]]
#inputs = df[["tiingo_volume", "amazon_value", "google_value"]]
#inputs = df[["tax_value", "trump_value"]]
target = df["tiingo_close"].astype("int")


#Split data

x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size = 0.4)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

#Train and test using Logistic Regression
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

#Train and test using Linear Regression
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(x_train,y_train)
plot_y = reg.predict(x_train)
print("Linear Regression Fit accuracy:", reg.score(x_test, y_test))

#print(type(y_test))


plt.plot(x_test, y_test, 'b.')
#plt.xticks(df["time"])
