import json
import pandas as pd

# Here we set up a little helper class to handle our timelineData object
class TimelineElement:
    def __init__(self, timelineData, index):
        data = timelineData[index]
# Example entry showing all rows:
# -> {'time': '1486252800', 'formattedTime': 'Feb 5 â€“ 11, 2017', 'formattedAxisTime': 'Feb 5, 2017', 'value': [67], 'hasData': [True], 'formattedValue': ['67']}
        if (data['hasData'][0]):
            self.entry = {"hasData":data['hasData'][0], "time":data['time'], "formattedAxisTime":data['formattedAxisTime'], "value":data['value'][0], "formattedValue":data['formattedValue'][0]}
        else:
            self.entry = {"hasData":data['hasData'][0], "time":"no-data", "formattedAxisTime":"no-data", "value":0, "formattedValue":"no-data"}

class TrendParser:
    def __init__(self, fileURI):
        ### Lets start opening our file now
        json_data = ""
        # Open our file containing data, read it into data
        with open(fileURI) as file:
            json_data = json.load(file)
        # Extract our useful data
        self.timelineData = json_data['default']['timelineData']

        self.dataElements = []

        for i in range(0, len(self.timelineData)):
            self.dataElements.append(TimelineElement(self.timelineData, i))

    def buildDataFrame(self, dataColumns=["time","formattedAxisTime","value","formattedValue"], includeEmptyElements=False):
        columns = dict()
        for col in dataColumns:
            columns[col] = []
        for elements in self.dataElements:
            for col in dataColumns:
                obj = elements.entry[col]
                if (obj):
                    if (elements.entry["hasData"]):
                        columns[col].append(obj)
                    elif (includeEmptyElements):
                        columns[col].append(obj)
                else:
                    logging.error("Bad dataColumn entry",col,"could not be found in the data.")
        df = pd.DataFrame.from_dict(columns, orient="index")
        return df.transpose()

########## EXAMPLE RUN ############
# p = TrendParser("trend_tax.txt")
# df = p.buildDataFrame()
# print(df.head())
