# Tiingo parser
import json
import pandas as pd

# Here we set up a little helper class to handle our timelineData object
class TimelineElement:
    def __init__(self, timelineData, index):
        data = timelineData[index]
# Example entry showing all rows:
# -> {"date": "2017-08-01T00:00:00.000Z", "close": 946.56, "high": 954.49, "low": 944.96, "open": 947.81, "volume": 1205799, "adjClose": 946.56, "adjHigh": 954.49, "adjLow": 944.96, "adjOpen": 947.81, "adjVolume": 1205799, "divCash": 0.0, "splitFactor": 1.0}
        self.entry = {"date":data['date'], "close":data['close'], "high":data['high'], "low":data['low'], "open":data['open'], "volume":data['volume'], "adjClose":data['adjClose'], "adjHigh":data['adjHigh'], "adjLow":data['adjLow'], "adjOpen":data['adjOpen'], "adjVolume":data['adjVolume'], "divCash":data['divCash'], "splitFactor":data['splitFactor']}

class TrendParser:
    def __init__(self, fileURI):
        ### Lets start opening our file now
        json_data = ""
        # Open our file containing data, read it into data
        with open(fileURI) as file:
            json_data = json.load(file)
        # Extract our useful data
        self.timelineData = json_data

        self.dataElements = []

        for i in range(0, len(self.timelineData)):
            self.dataElements.append(TimelineElement(self.timelineData, i))

    def buildDataFrame(self, dataColumns=["date","close","volume","high","low"]):
        columns = dict()
        for col in dataColumns:
            columns[col] = []
        for elements in self.dataElements:
            for col in dataColumns:
                obj = elements.entry[col]
                if (obj):
                    columns[col].append(obj)
                else:
                    logging.error("Bad dataColumn entry",col,"could not be found in the data.")
        df = pd.DataFrame.from_dict(columns, orient="index")
        return df.transpose()

########## EXAMPLE RUN ############
# parserObject = TrendParser("data.json")
# df = parserObject.buildDataFrame()
# print(df.head())
