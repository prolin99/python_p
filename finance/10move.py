import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft JhengHei")

# 下載資料 (自動調整股價)
ticker = "2330.TW"
# auto_adjust False 才會有 AdJ Close 欄位
data = yf.download(ticker, period="max", auto_adjust=False)
# print(data.tail())



# 繪圖
plt.figure(figsize=(10, 5))
plt.plot( data.loc['2023':'2024',"Close"], label="收盤價", color="blue")
plt.plot( data.loc['2023':'2024',"Close"].rolling(20).mean(), label="月均線", color="red")
plt.plot( data.loc['2023':'2024',"Close"].rolling(60).mean(), label="季均線", color="green")
# pct_change 是日報酬率 ， cumprod 是用日報酬率計算 累積報酬率
#plt.plot(data.index, (data["Close"].pct_change()+1).cumprod(), label="Close (報酬率)", color="blue")
#plt.plot(data.index, (data["Adj Close"].pct_change()+1).cumprod(), label="Adj Close (報酬率)", color="red")

# 圖表設定
plt.title(f"{ticker} 均線", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.legend()
plt.grid(True)

plt.show()
