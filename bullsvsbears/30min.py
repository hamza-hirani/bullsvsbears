import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import Day

# getting the start date 
print("Date: ")
startDate = input()
try:
    # setting the end date
    day = int(startDate[8:10])
    endingDay = day + 1
    endDate = startDate[0:8] + str(endingDay)
    print(endDate)

    print("Equity: ")
    symbol = input()

    stock = yf.Ticker(symbol)

    historicalPriceData = stock.history(start=startDate, end=endDate, interval="30m")
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
except:
    print("Invalid date")