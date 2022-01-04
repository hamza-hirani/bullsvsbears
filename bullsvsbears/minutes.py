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

    historicalPriceData = stock.history(start=startDate, end=endDate, interval="1m")
    price = historicalPriceData["Open"]

    time = list(range(1, 392))

    data = {
        "time": time,
        "prices": price
    }

    df = pd.DataFrame(data)

    print(df)

    df.plot(x = 'time', y = 'prices', title = "$" + symbol)

    graph = plt.show()

    print(graph)
except:
    print("Invalid date")



    