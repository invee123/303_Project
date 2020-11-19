from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject

from google_parser import TrendParser as GoogleParser
from tiingo_parser import TrendParser as TiingoParser

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
print(googleData["trump"].describe())
print(tiingoData.describe())
