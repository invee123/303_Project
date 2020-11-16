import json

# Here we set up a little helper class to handle our timelineData object
class TimelineElement:
    def __init__(self, timelineData, index):
        data = timelineData[index]

        self.hasData = data['hasData'][0]
        if (self.hasData):
            self.time = data['time']
            self.value = data['value'][0] # exists as a list in the json tho, as do the following few
            self.formattedValue = data['formattedValue'][0]
            self.formattedAxisTime = data['formattedAxisTime']
        else:
            self.time, self.value = 0
            self.formattedAxisTime, self.formattedValue = ""


class TrendParser:
    def __init__(self, fileURI):
        ### Lets start opening our file now
        json_data = ""
        # Open our file containing data, read it into data
        with open(fileURI) as file:
            json_data = json.load(file)
        # Extract our useful data
        self.timelineData = json_data['default']['timelineData']

#    def sortDataByTime():
#        lowestIndex = 0
#        for i in range(0, len(self.timelineData)):
#            compareItem TimelineElement(self.timelineData, lowestIndex)
#            item = TimelineElement(self.timelineData, i)
#            if (item.time < compareItem.time)





#debug comment -- print data very nice
#print(json.dumps(json_data, indent = 4, sort_keys = True))

# Now that the data is loaded into json_data, we can play with it.
# json_data['default']['timelineData'] is of interest...

#print(json_data['default']['timelineData'][0])
# -> {'time': '1486252800', 'formattedTime': 'Feb 5 â€“ 11, 2017', 'formattedAxisTime': 'Feb 5, 2017', 'value': [67], 'hasData': [True], 'formattedValue': ['67']}

#print(type(json_data['default']['timelineData'][0]['value']))
# -> list

#test = TimelineElement(timelineData, 0)
#print(test.formattedAxisTime)
