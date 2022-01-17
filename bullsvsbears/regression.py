import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression

# get data and prepare for conversion 
print("Equity: ")
symbol = input()

stock = yf.Ticker(symbol)

historicalPriceData = stock.history(start='2022-01-13', end='2022-01-14', interval="1m")
listOfPrices = historicalPriceData["Open"]

listOfTimes = list(range(1, 391))

# performing the regression
time = np.array(listOfTimes).reshape(-1,1)
price = np.array(listOfPrices).reshape(-1,1)
regressor = LinearRegression()
regressor.fit(time, price)
forecast = regressor.predict(time)

#visualization
plt.scatter(time, price)
plt.plot(time, forecast, color = 'green')
plt.show()