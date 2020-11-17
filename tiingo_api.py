from tiingo import TiingoClient
import json

# Set TIINGO_API_KEY in your environment variables in your .bash_profile, OR
# pass a dictionary with 'api_key' as a key into the TiingoClient.
config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
# Enter tiingo account key:
config['api_key'] = "ENTER_KEY"
# Initialize
client = TiingoClient(config)

# Get Ticker
ticker_metadata = client.get_ticker_metadata("GOOGL")

# Get latest prices, based on 3+ sources as JSON, sampled weekly
ticker_price = client.get_ticker_price("GOOGL", frequency="weekly")

# Get historical prices from different dates by adjusting parameters
historical_prices = client.get_ticker_price("GOOGL",fmt='json',startDate='2017-08-01',endDate='2017-08-31',frequency='daily')

# Print out price results - every line has info from every frequency (every day/week/month/etc...)
for i in range(0, len(historical_prices)):
    print(historical_prices[i])

# Outputs results to JSON file (can change name of file)
with open('data.json', 'w') as outfile:
    json.dump(historical_prices,outfile)