import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

stocks = []

print("Enter number of stocks: ")
numStocks = int(input())
for i in range(0, numStocks):
    print("Enter ticker: ")
    newStock = input()
    stocks.append(newStock)

stockData = yf.download(stocks, start='2018-01-01')

#daily returns
closing = stockData['Close']
percentChange = closing.pct_change()

p_weights = []
p_returns = []
p_risk = []
p_sharpe = []

count = 100
for i in range(0, count):
    wts = np.random.uniform(size = len(percentChange.columns))
    wts = wts/np.sum(wts)
    p_weights.append(wts)

    #returns
    mean_ret = (percentChange.mean() * wts).sum()*252
    p_returns.append(mean_ret)

    #volatility
    ret = (percentChange * wts).sum(axis = 1)
    annual_std = np.std(ret) * np.sqrt(252)
    p_risk.append(annual_std)
    
    #Sharpe ratio
    sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
    p_sharpe.append(sharpe)


max_ind = np.argmax(p_sharpe)

plt.scatter(p_risk, p_returns, c=p_sharpe, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')

plt.scatter(p_risk[max_ind], p_returns[max_ind], color='r', marker='*', s=500)
plt.show()