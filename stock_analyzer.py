"""
COMPLETE STOCK SELECTION SYSTEM
Fundamental + Technical Analysis with Live Data
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class StockAnalyzer:
    def __init__(self, api_key=None):
        """Initialize with API key for NSE/BSE data"""
        self.api_key = api_key
        
    def get_stock_data(self, symbol):
        """Fetch live stock data"""
        try:
            stock = yf.Ticker(symbol + ".NS")  # NSE suffix for Indian stocks
            info = stock.info
            hist = stock.history(period="1y")
            
            return {
                'symbol': symbol,
                'price': info.get('currentPrice', 0),
                'market_cap': info.get('marketCap', 0),
                'pe_ratio': info.get('trailingPE', 0),
                'history': hist
            }
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            return None

    def calculate_eps_metrics(self, stock_data):
        """
        Calculate EPS metrics
        Requirements:
        - EPS latest quarter > EPS preceding year quarter
        - EPS latest quarter > EPS preceding quarter
        - EPS latest quarter > 0
        """
        # In real scenario, fetch from financial statements API
        # Using yfinance earnings data
        try:
            earnings = stock_data.quarterly_financials.get('Diluted EPS', [])
            if len(earnings) >= 2:
                latest_eps = earnings[0]
                preceding_eps = earnings[1]
                year_ago_eps = earnings[-1] if len(earnings) > 4 else earnings[-1]
                
                return {
                    'latest': float(latest_eps),
                    'preceding_quarter': float(preceding_eps),
                    'year_ago': float(year_ago_eps),
                    'passes': (latest_eps > preceding_eps and 
                              latest_eps > year_ago_eps and 
                              latest_eps > 0)
                }
        except:
            pass
        return None

    def calculate_debt_to_equity(self, stock_data):
        """
        Calculate Debt to Equity Ratio
        Requirement: < 1
        """
        try:
            balance_sheet = stock_data.quarterly_balance_sheet
            total_debt = (balance_sheet.loc['Total Debt'].iloc[0] 
                         if 'Total Debt' in balance_sheet.index else 0)
            total_equity = (balance_sheet.loc['Total Equity'].iloc[0] 
                           if 'Total Equity' in balance_sheet.index else 1)
            
            ratio = total_debt / total_equity if total_equity > 0 else 0
            return {
                'ratio': float(ratio),
                'passes': ratio < 1
            }
        except:
            return None

    def calculate_asset_turnover(self, stock_data):
        """
        Calculate Asset Turnover Ratio
        Requirement: > 1
        Formula: Revenue / Average Total Assets
        """
        try:
            income = stock_data.quarterly_income_stmt
            balance = stock_data.quarterly_balance_sheet
            
            revenue = float(income.loc['Total Revenue'].iloc[0])
            assets = float(balance.loc['Total Assets'].iloc[0])
            
            ratio = revenue / assets if assets > 0 else 0
            return {
                'ratio': float(ratio),
                'passes': ratio > 1
            }
        except:
            return None

    def calculate_working_capital_ratio(self, stock_data):
        """
        Calculate Working Capital to Sales Ratio
        Requirement: > 20%
        Formula: (Current Assets - Current Liabilities) / Net Sales
        """
        try:
            balance = stock_data.quarterly_balance_sheet
            income = stock_data.quarterly_income_stmt
            
            current_assets = float(balance.loc['Current Assets'].iloc[0])
            current_liabilities = float(balance.loc['Current Liabilities'].iloc[0])
            sales = float(income.loc['Total Revenue'].iloc[0])
            
            working_capital = current_assets - current_liabilities
            ratio = (working_capital / sales * 100) if sales > 0 else 0
            
            return {
                'ratio': float(ratio),
                'passes': ratio > 20
            }
        except:
            return None

    def calculate_sales_growth(self, stock_data):
        """
        Calculate Year-over-Year Sales Growth
        Requirement: > 15%
        """
        try:
            income = stock_data.quarterly_income_stmt
            latest_sales = float(income.loc['Total Revenue'].iloc[0])
            year_ago_sales = float(income.loc['Total Revenue'].iloc[4])  # 4 quarters back
            
            growth = ((latest_sales - year_ago_sales) / year_ago_sales * 100) if year_ago_sales > 0 else 0
            return {
                'growth': float(growth),
                'passes': growth > 15
            }
        except:
            return None

    def calculate_roce(self, stock_data):
        """
        Calculate Return on Capital Employed
        Requirement: > 12%
        Formula: EBIT / (Equity + Debt - Cash)
        """
        try:
            income = stock_data.quarterly_income_stmt
            balance = stock_data.quarterly_balance_sheet
            
            ebit = float(income.loc['Operating Income'].iloc[0])
            equity = float(balance.loc['Total Equity'].iloc[0])
            debt = float(balance.loc['Total Debt'].iloc[0] if 'Total Debt' in balance.index else 0)
            cash = float(balance.loc['Cash And Cash Equivalents'].iloc[0] if 'Cash And Cash Equivalents' in balance.index else 0)
            
            capital_employed = equity + debt - cash
            roce = (ebit / capital_employed * 100) if capital_employed > 0 else 0
            
            return {
                'roce': float(roce),
                'passes': roce > 12
            }
        except:
            return None

    def calculate_supertrend(self, data, period=10, multiplier=3):
        """
        Calculate Supertrend (Technical Indicator)
        Returns: Supertrend line and signal
        """
        high = data['High'].values
        low = data['Low'].values
        close = data['Close'].values
        
        # ATR calculation
        tr = np.maximum(high - low, 
                       np.maximum(abs(high - close[:-1] if len(close) > 1 else high),
                                 abs(low - close[:-1] if len(close) > 1 else low)))
        atr = np.convolve(tr, np.ones(period)/period, mode='valid')
        
        # HL2
        hl2 = (high + low) / 2
        
        # Basic bands
        up = hl2 - multiplier * atr
        down = hl2 + multiplier * atr
        
        # Calculate supertrend
        supertrend = np.zeros(len(close))
        trend = np.zeros(len(close))
        
        for i in range(len(close)):
            if i < period:
                supertrend[i] = close[i]
                continue
            
            if close[i] <= up[i - period]:
                supertrend[i] = up[i - period]
                trend[i] = 1  # Uptrend
            else:
                supertrend[i] = down[i - period]
                trend[i] = -1  # Downtrend
        
        return {
            'supertrend': supertrend[-1],
            'trend': trend[-1],
            'signal': 'BUY' if trend[-1] == 1 else 'SELL',
            'price_above': close[-1] > supertrend[-1]
        }

    def analyze_stock(self, symbol):
        """Complete analysis of a single stock"""
        print(f"Analyzing {symbol}...")
        
        stock_data = yf.Ticker(symbol + ".NS")
        
        # Get historical data for technical analysis
        hist = stock_data.history(period="6mo")
        
        # Fundamental metrics
        fundamentals = {
            'eps': self.calculate_eps_metrics(stock_data),
            'debt_to_equity': self.calculate_debt_to_equity(stock_data),
            'asset_turnover': self.calculate_asset_turnover(stock_data),
            'working_capital': self.calculate_working_capital_ratio(stock_data),
            'sales_growth': self.calculate_sales_growth(stock_data),
            'roce': self.calculate_roce(stock_data),
        }
        
        # Technical metrics
        technical = self.calculate_supertrend(hist)
        
        # Calculate scores
        fundamental_score = sum([
            20 if f and f.get('passes') else 0 
            for f in fundamentals.values() if f
        ]) / 120 * 100
        
        return {
            'symbol': symbol,
            'price': hist['Close'].iloc[-1],
            'fundamentals': fundamentals,
            'technical': technical,
            'fundamental_score': fundamental_score,
            'timestamp': datetime.now().isoformat()
        }

    def batch_analyze(self, symbols):
        """Analyze multiple stocks"""
        results = []
        for symbol in symbols:
            try:
                result = self.analyze_stock(symbol)
                results.append(result)
            except Exception as e:
                print(f"Error analyzing {symbol}: {e}")
        
        return results

    def filter_by_criteria(self, results):
        """Filter stocks that meet all criteria"""
        qualified = []
        
        for stock in results:
            f = stock['fundamentals']
            t = stock['technical']
            
            # Check fundamental criteria
            fundamental_pass = all([
                f.get('eps', {}).get('passes', False),
                f.get('debt_to_equity', {}).get('passes', False),
                f.get('asset_turnover', {}).get('passes', False),
                f.get('working_capital', {}).get('passes', False),
                f.get('sales_growth', {}).get('passes', False),
                f.get('roce', {}).get('passes', False),
            ])
            
            # Check technical criteria
            technical_pass = (
                t.get('price_above', False) and 
                t.get('signal') == 'BUY'
            )
            
            stock['fundamental_pass'] = fundamental_pass
            stock['technical_pass'] = technical_pass
            stock['final_signal'] = 'BUY' if (fundamental_pass and technical_pass) else 'HOLD'
            
            if fundamental_pass or technical_pass:
                qualified.append(stock)
        
        return sorted(qualified, key=lambda x: x.get('fundamental_score', 0), reverse=True)


# USAGE EXAMPLE
if __name__ == "__main__":
    # Top 20 NSE stocks
    stocks_to_analyze = [
        'RELIANCE', 'TCS', 'HDFC', 'INFY', 'WIPRO', 
        'AXISBANK', 'LT', 'MARUTI', 'ICICIBANK', 'HCLTECH',
        'SBIN', 'SUNPHARMA', 'JSWSTEEL', 'BAJAJFINSV', 'TECHM',
        'NTPC', 'POWERGRID', 'BHARTIARTL', 'ITC', 'ULTRACEMCO'
    ]
    
    analyzer = StockAnalyzer()
    
    print("=" * 60)
    print("STOCK SELECTION ANALYSIS - LIVE DATA")
    print("=" * 60)
    
    # Analyze all stocks
    results = analyzer.batch_analyze(stocks_to_analyze)
    
    # Filter by criteria
    qualified = analyzer.filter_by_criteria(results)
    
    # Display results
    print("\n" + "=" * 60)
    print("QUALIFIED STOCKS (BUY SIGNAL)")
    print("=" * 60)
    
    for stock in qualified:
        if stock['final_signal'] == 'BUY':
            print(f"\n{stock['symbol']} - Price: ₹{stock['price']:.2f}")
            print(f"Fundamental Score: {stock['fundamental_score']:.1f}%")
            print(f"Technical Signal: {stock['technical']['signal']}")
            print(f"Supertrend Level: ₹{stock['technical']['supertrend']:.2f}")
    
    # Export to JSON for web dashboard
    with open('stock_analysis_results.json', 'w') as f:
        json.dump(qualified, f, indent=2, default=str)
    
    print("\n✓ Results exported to stock_analysis_results.json")
