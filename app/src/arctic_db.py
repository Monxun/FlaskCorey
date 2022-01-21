from arctic import Arctic
import vectorbt as vbt
import quandl

ticker = 'AAPL'
# Connect to Local MONGODB
store = Arctic('localhost')

# Create the library - defaults to VersionStore
store.initialize_library(ticker)

# Access the library
library = store['AAPL']

# Load some data - maybe from Quandl
price = quandl.get(f"WIKI/{ticker}", authtoken="ADtcPQAzkx2YwrVEmyXS")

# price = vbt.YFData.download(ticker).get('Close')
# Store the data in the library
library.write(ticker, price, metadata={'source': 'YahooFinance'})

# Reading the data
item = library.read(ticker)
price = item.data
metadata = item.metadata