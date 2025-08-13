import yfinance as yf
import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft JhengHei")

# 下載資料 (自動調整股價)
ticker = "2330.TW"
# auto_adjust False 才會有 AdJ Close 欄位
data = yf.download(ticker, period="max", auto_adjust=False)
print(data.tail())



# 繪圖
plt.figure(figsize=(10, 5))
# pct_change 是日報酬率 ， cumprod 是用日報酬率計算 累積報酬率
plt.plot(data.index, (data["Close"].pct_change()+1).cumprod(), label="Close (報酬率)", color="blue")
plt.plot(data.index, (data["Adj Close"].pct_change()+1).cumprod(), label="Adj Close (報酬率)", color="red")

# 圖表設定
plt.title(f"{ticker} Close vs Adj Close", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.legend()
plt.grid(True)

plt.show()
