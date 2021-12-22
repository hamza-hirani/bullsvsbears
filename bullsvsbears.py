import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import Day

print("Equity: ")
symbol = input()

stock = yf.Ticker(symbol)

historicalPriceData = stock.history(start="2021-12-15", end="2021-12-16", interval="30m")
price = historicalPriceData["Open"]

time = ["9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00", "3:30"]

data = {
    "time": time,
    "prices": price
}

df = pd.DataFrame(data)

df.plot(x = 'time', y = 'prices', title = "$" + symbol)

graph = plt.show()

print(graph)