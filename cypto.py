import yfinance as yf
from sklearn.linear_model import LinearRegression

print("Welcome to the Cypto Market")

# Create a dictionary mapping ticker symbols to model objects
models = {}

# Define the ticker symbols for the crypto assets
ticker_symbols = ['BTC-USD', 'ETH-USD']

# Iterate over the ticker symbols
for ticker in ticker_symbols:
    # Get the cryptocurrency data
    crypto_data = yf.Ticker(ticker).history(period="3mo")

    # Split the data into a training set and a test set
    train_data = crypto_data[:int(0.8*len(crypto_data))]
    test_data = crypto_data[int(0.8*len(crypto_data)):]

    # Extract the close prices from the training and test sets
    train_close_prices = train_data["Close"].values.reshape(-1, 1)
    test_close_prices = test_data["Close"].values.reshape(-1, 1)

    # Create a linear regression model and fit it to the training data
    model = LinearRegression()
    model.fit(train_close_prices, train_data["Close"])

    # Store the model in the dictionary
    models[ticker] = model

# Iterate over the ticker symbols again
for ticker in ticker_symbols:

    # Get the model for the current ticker symbol
    model = models[ticker]

    # Use the model to make predictions on the test data
    predictions = model.predict(test_close_prices)

    # Print the predictions
    print(f"Predictions for {ticker}: {predictions}")



