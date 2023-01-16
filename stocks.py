import yfinance as yf
from sklearn.linear_model import LinearRegression

print("Welcome to the Stock Market")

# Create a dictionary mapping ticker symbols to model objects
models = {}

# Define the ticker symbols
ticker_symbols = ['TSLA', 'GOOGL', 'META', 'TWTR', 'MSFT']

# Iterate over the ticker symbols
for ticker in ticker_symbols:
    # Get the stock data
    stock_data = yf.Ticker(ticker).history(period="3mo")

    # Split the data into a training set and a test set
    train_data = stock_data[:int(0.8*len(stock_data))]
    test_data = stock_data[int(0.8*len(stock_data)):]

    # Extract the close prices from the training and test sets
    train_close_prices = train_data["Close"].values.reshape(-1, 1)
    test_close_prices = test_data["Close"].values.reshape(-1, 1)

    # Drop rows with missing values
    train_data.dropna(subset=["Close"])
    test_data.dropna(subset=["Close"])

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



