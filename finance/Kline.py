import yfinance as yf
import mplfinance as mpf

import pandas as pd

import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft JhengHei")

# 下載資料 (自動調整股價)
ticker = "2330.TW"
# auto_adjust False 才會有 AdJ Close 欄位
#data = yf.download(ticker, period="max", auto_adjust=False)
data = yf.download(ticker, period="3mo", interval="1d")


# 打印列名以檢查實際的數據結構
print("Column names:", data.columns)

# 處理數據結構以符合 mplfinance 的要求
if isinstance(data.columns, pd.MultiIndex):
    # 獲取第一層索引的名稱
    level0_names = data.columns.get_level_values(0).unique().tolist()
    print("Level 0 names:", level0_names)
    
    # 如果有 'Price' 和其他列，則重新組織數據
    if 'Price' in level0_names:
        # 創建新的 DataFrame 以符合 mplfinance 的要求
        new_data = pd.DataFrame(index=data.index)
        
        # 映射 Price 列到標準 OHLC 列名
        price_columns = {'Open': 'Open', 'High': 'High', 'Low': 'Low', 'Close': 'Close'}
        for mpl_col, yf_col in price_columns.items():
            if ('Price', yf_col) in data.columns:
                new_data[mpl_col] = data[('Price', yf_col)]
        
        # 添加成交量列
        if 'Volume' in level0_names:
            new_data['Volume'] = data['Volume'].iloc[:, 0]  # 假設只有一個 Volume 列
        
        # 替換原始數據
        data = new_data
    else:
        # 如果沒有 'Price' 層，則嘗試直接重命名列
        # 假設列的順序是 Open, High, Low, Close, Volume
        if len(data.columns) >= 5:  # 至少有 OHLCV 五列
            data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        else:
            print("Warning: Unexpected column structure")

print("Final columns:", data.columns)

print(data.tail())

# 繪製 K 線圖 並設定標題
mpf.plot(data, type='candle', title='2330 台積電 K 線圖')


