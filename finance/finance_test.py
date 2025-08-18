import yfinance as yf
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_dividend_data(ticker_symbol, years=10):
    """
    獲取股票的配股配息資料

    :param ticker_symbol: 股票代碼 (e.g., "2330.TW")
    :param years: 查詢年限
    :return: 包含配股配息資料的DataFrame
    """
    # 設定時間區間
    end_date = datetime.now()
    start_date = end_date - relativedelta(years=years)
    
    print(f"正在下載 {ticker_symbol} 從 {start_date.strftime('%Y-%m-%d')} 到 {end_date.strftime('%Y-%m-%d')} 的配股配息資料...")
    
    try:
        # 創建Ticker對象
        ticker = yf.Ticker(ticker_symbol)
        
        # 獲取股息數據
        dividends = ticker.dividends
        
        # 篩選時間範圍內的數據
        if not dividends.empty:
            # 將時間索引轉換為無時區的日期
            dividends.index = dividends.index.tz_localize(None)
            
            # 篩選時間範圍
            dividends = dividends[(dividends.index >= pd.Timestamp(start_date)) & 
                                 (dividends.index <= pd.Timestamp(end_date))]
            
            # 創建DataFrame
            div_df = pd.DataFrame({
                '日期': dividends.index.strftime('%Y-%m-%d'),
                '股息': dividends.values
            })
            
            # 按年份和月份分組
            div_df['年份'] = dividends.index.year
            div_df['月份'] = dividends.index.month
            div_df['季度'] = ((dividends.index.month - 1) // 3) + 1
            
            # 計算年度、季度和月度總和
            yearly_div = div_df.groupby('年份')['股息'].sum().reset_index()
            quarterly_div = div_df.groupby(['年份', '季度'])['股息'].sum().reset_index()
            monthly_div = div_df.groupby(['年份', '月份'])['股息'].sum().reset_index()
            
            # 重命名列
            yearly_div.columns = ['年份', '年度股息']
            quarterly_div.columns = ['年份', '季度', '季度股息']
            monthly_div.columns = ['年份', '月份', '月度股息']
            
            print(f"找到 {len(dividends)} 筆配股配息資料")
            
            return {
                'all_dividends': div_df,
                'yearly': yearly_div,
                'quarterly': quarterly_div,
                'monthly': monthly_div
            }
        else:
            print(f"在指定的時間範圍內沒有找到 {ticker_symbol} 的配股配息資料")
            return None
    except Exception as e:
        print(f"獲取配股配息資料時發生錯誤: {e}")
        return None

def export_dividend_data(ticker_symbol, dividend_data, years=10):
    """
    將配股配息資料匯出至CSV

    :param ticker_symbol: 股票代碼
    :param dividend_data: 配股配息資料字典
    :param years: 查詢年限
    """
    if dividend_data is None:
        return
    
    # 匯出所有配息記錄
    all_div_filename = f'{ticker_symbol.replace(".", "_")}_all_dividends_{years}y.csv'
    try:
        dividend_data['all_dividends'].to_csv(all_div_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"所有配息記錄已匯出至: {all_div_filename}")
    except Exception as e:
        print(f"匯出配息記錄時發生錯誤: {e}")
    
    # 匯出年度配息統計
    yearly_div_filename = f'{ticker_symbol.replace(".", "_")}_yearly_dividends_{years}y.csv'
    try:
        dividend_data['yearly'].to_csv(yearly_div_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"年度配息統計已匯出至: {yearly_div_filename}")
    except Exception as e:
        print(f"匯出年度配息統計時發生錯誤: {e}")
    
    # 匯出季度配息統計
    quarterly_div_filename = f'{ticker_symbol.replace(".", "_")}_quarterly_dividends_{years}y.csv'
    try:
        dividend_data['quarterly'].to_csv(quarterly_div_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"季度配息統計已匯出至: {quarterly_div_filename}")
    except Exception as e:
        print(f"匯出季度配息統計時發生錯誤: {e}")
    
    # 匯出月度配息統計
    monthly_div_filename = f'{ticker_symbol.replace(".", "_")}_monthly_dividends_{years}y.csv'
    try:
        dividend_data['monthly'].to_csv(monthly_div_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"月度配息統計已匯出至: {monthly_div_filename}")
    except Exception as e:
        print(f"匯出月度配息統計時發生錯誤: {e}")

def simulate_dca(ticker_symbol, monthly_investment, years=10):
    """
    模擬定期定額投資策略並將結果匯出至 CSV。

    :param ticker_symbol: 股票代碼 (e.g., "2330.TW")
    :param monthly_investment: 每月投資金額
    :param years: 投資年限
    :return: 包含模擬結果的DataFrame
    """
    # 1. 設定時間區間
    end_date = datetime.now()
    start_date = end_date - relativedelta(years=years)

    # 2. 下載股價資料
    print(f"正在下載 {ticker_symbol} 從 {start_date.strftime('%Y-%m-%d')} 到 {end_date.strftime('%Y-%m-%d')} 的股價資料...")
    try:
        # auto_adjust=False 以便能取得 'Close' 欄位
        data = yf.download(ticker_symbol, start=start_date, end=end_date, auto_adjust=False, progress=False)
        if data.empty:
            print(f"找不到股票代碼 {ticker_symbol} 的資料，請檢查代碼是否正確。")
            return None
            
        # 檢查數據結構並顯示列名
        print(f"下載的數據列名: {data.columns.tolist()}")
        
        # 處理多層索引的情況
        if isinstance(data.columns, pd.MultiIndex):
            print("檢測到多層索引，進行處理...")
            # 如果是多層索引，選擇第一層為'Close'的列
            close_col = [col for col in data.columns if col[0] == 'Close']
            if close_col:
                # 創建一個新的單層索引DataFrame
                new_data = pd.DataFrame(index=data.index)
                new_data['Close'] = data[close_col[0]]
                data = new_data
            else:
                print("找不到包含 'Close' 的列")
                return None
        elif 'Close' not in data.columns and 'Adj Close' in data.columns:
            # 如果是單層索引但沒有 'Close' 列
            print("找不到 'Close' 列，使用 'Adj Close' 列代替。")
            data['Close'] = data['Adj Close']
    except Exception as e:
        print(f"下載資料時發生錯誤: {e}")
        return None

    # 3. 找出每個月的實際購買日期
    # 我們要找的是每個月的第一天，如果那天沒開盤，就順延到下一個開盤日
    target_dates = pd.date_range(start=data.index.min(), end=data.index.max(), freq='MS') # 'MS' = Month Start

    buy_dates = []
    for date in target_dates:
        # searchsorted 會找到第一個不小於目標日期的索引
        actual_date_index = data.index.searchsorted(date, side='left')
        if actual_date_index < len(data.index):
            buy_dates.append(data.index[actual_date_index])

    # 去除重複的日期 (雖然在此邏輯下不太可能發生)
    buy_dates = sorted(list(set(buy_dates)))

    # 從主要資料中篩選出購買日的數據，並預先移除沒有收盤價的日期
    buy_data = data.loc[data.index.intersection(buy_dates)].dropna(subset=['Close'])

    # 4. 模擬投資過程
    transactions = []
    cumulative_cost = 0.0
    cumulative_shares = 0.0

    for date, row in buy_data.iterrows():
        price = row['Close']

        shares_bought = monthly_investment / price
        cumulative_cost += monthly_investment
        cumulative_shares += shares_bought
        cumulative_value = cumulative_shares * price
        transactions.append({
            '購買日期': date.strftime('%Y-%m-%d'),
            '股價': price,
            '購得股數': shares_bought,
            '累計費用': cumulative_cost,
            '累計股數': cumulative_shares,
            '累計股票價值': cumulative_value
        })

    if not transactions:
        print("在指定的時間範圍內沒有可執行的交易。")
        return None

    # 5. 建立 DataFrame 並匯出
    results_df = pd.DataFrame(transactions)

    # 顯示結果 (最後五筆)
    print("\n定期定額模擬結果 (最後五筆):")
    print(results_df.tail().to_string())

    # 匯出至 CSV
    output_filename = f'{ticker_symbol.replace(".", "_")}_dca_simulation_{years}y.csv'
    try:
        results_df.to_csv(output_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"\n資料已成功匯出至: {output_filename}")
    except Exception as e:
        print(f"匯出 CSV 時發生錯誤: {e}")
        
    return results_df

def calculate_dividend_return(ticker_symbol, dca_data, dividend_data, years=10):
    """
    計算含息報酬率

    :param ticker_symbol: 股票代碼
    :param dca_data: 定期定額投資數據
    :param dividend_data: 配股配息資料
    :param years: 投資年限
    :return: 含息報酬率數據
    """
    if dividend_data is None or dca_data.empty:
        print("無法計算含息報酬率：缺少必要數據")
        return None
    
    try:
        # 複製定期定額投資數據
        result_df = dca_data.copy()
        
        # 將購買日期轉換為datetime
        result_df['購買日期'] = pd.to_datetime(result_df['購買日期'])
        
        # 獲取所有配息記錄
        all_dividends = dividend_data['all_dividends'].copy()
        all_dividends['日期'] = pd.to_datetime(all_dividends['日期'])
        
        # 初始化累計配息欄位
        result_df['累計配息'] = 0.0
        result_df['含息總價值'] = result_df['累計股票價值']
        
        # 計算每次交易後的累計配息
        for i, row in result_df.iterrows():
            current_date = row['購買日期']
            current_shares = row['累計股數']
            
            # 找出當前日期之前的所有配息
            if i > 0:
                # 繼承前一筆交易的累計配息
                result_df.at[i, '累計配息'] = result_df.at[i-1, '累計配息']
            
            # 找出當前交易日期之前、上一次交易日期之後的配息
            prev_date = result_df.at[i-1, '購買日期'] if i > 0 else pd.Timestamp('1900-01-01')
            new_dividends = all_dividends[(all_dividends['日期'] > prev_date) & 
                                         (all_dividends['日期'] <= current_date)]
            
            # 如果有新的配息，計算配息金額並加入累計配息
            if not new_dividends.empty:
                # 假設配息是按照當時持有的股數計算
                # 實際上應該根據除息日的持股數計算，但這裡簡化處理
                prev_shares = result_df.at[i-1, '累計股數'] if i > 0 else 0
                for _, div_row in new_dividends.iterrows():
                    dividend_amount = div_row['股息'] * prev_shares
                    result_df.at[i, '累計配息'] += dividend_amount
            
            # 計算含息總價值
            result_df.at[i, '含息總價值'] = result_df.at[i, '累計股票價值'] + result_df.at[i, '累計配息']
        
        # 計算報酬率
        result_df['不含息報酬率'] = (result_df['累計股票價值'] / result_df['累計費用'] - 1) * 100
        result_df['含息報酬率'] = (result_df['含息總價值'] / result_df['累計費用'] - 1) * 100
        
        # 匯出結果
        output_filename = f'{ticker_symbol.replace(".", "_")}_dividend_return_{years}y.csv'
        result_df.to_csv(output_filename, index=False, encoding='utf-8-sig', float_format='%.4f')
        print(f"含息報酬率數據已匯出至: {output_filename}")
        
        return result_df
    except Exception as e:
        print(f"計算含息報酬率時發生錯誤: {e}")
        return None

if __name__ == '__main__':
    # --- 設定參數 ---
    TICKER = "2330.TW"
    MONTHLY_AMOUNT = 10000
    INVESTMENT_YEARS = 10
    # ----------------

    # 模擬定期定額投資
    dca_results = simulate_dca(TICKER, MONTHLY_AMOUNT, INVESTMENT_YEARS)
    
    # 獲取並匯出配股配息資料
    dividend_data = get_dividend_data(TICKER, INVESTMENT_YEARS)
    if dividend_data:
        export_dividend_data(TICKER, dividend_data, INVESTMENT_YEARS)
        
        # 顯示年度配息統計
        print("\n年度配息統計:")
        print(dividend_data['yearly'].to_string(index=False))
        
        # 計算含息報酬率
        if dca_results is not None:
            dividend_return = calculate_dividend_return(TICKER, dca_results, dividend_data, INVESTMENT_YEARS)
            if dividend_return is not None:
                print("\n含息報酬率結果 (最後五筆):")
                print(dividend_return[['購買日期', '累計費用', '累計股票價值', '累計配息', '含息總價值', '不含息報酬率', '含息報酬率']].tail().to_string())
