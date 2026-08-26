"""
FLASK API SERVER FOR STOCK ANALYSIS DASHBOARD
Live data fetching with caching and real-time updates
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from stock_analyzer import StockAnalyzer
import json
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)
CORS(app)

# Global cache
cache = {
    'results': [],
    'last_update': None,
    'updating': False
}

analyzer = StockAnalyzer()

# Default stocks to analyze
DEFAULT_STOCKS = [
    'RELIANCE', 'TCS', 'HDFC', 'INFY', 'WIPRO', 
    'AXISBANK', 'LT', 'MARUTI', 'ICICIBANK', 'HCLTECH',
    'SBIN', 'SUNPHARMA', 'JSWSTEEL', 'BAJAJFINSV', 'TECHM'
]

def update_analysis():
    """Background task to update stock analysis"""
    cache['updating'] = True
    try:
        print(f"[{datetime.now()}] Starting analysis update...")
        results = analyzer.batch_analyze(DEFAULT_STOCKS)
        qualified = analyzer.filter_by_criteria(results)
        
        cache['results'] = qualified
        cache['last_update'] = datetime.now().isoformat()
        print(f"[{datetime.now()}] Analysis complete. Found {len(qualified)} qualified stocks.")
    except Exception as e:
        print(f"Error in analysis: {e}")
    finally:
        cache['updating'] = False

def start_background_update():
    """Start background update thread"""
    thread = threading.Thread(target=update_analysis, daemon=True)
    thread.start()

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    """Get analyzed stocks"""
    min_score = request.args.get('min_score', 0, type=float)
    signal_only = request.args.get('signal_only', 'false').lower() == 'true'
    
    results = cache['results']
    
    if signal_only:
        results = [s for s in results if s.get('final_signal') == 'BUY']
    
    if min_score > 0:
        results = [s for s in results if s.get('fundamental_score', 0) >= min_score]
    
    return jsonify({
        'stocks': results,
        'last_update': cache['last_update'],
        'total': len(results),
        'updating': cache['updating']
    })

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_detail(symbol):
    """Get detailed analysis for a single stock"""
    for stock in cache['results']:
        if stock['symbol'] == symbol.upper():
            return jsonify(stock)
    
    # If not in cache, analyze now
    try:
        result = analyzer.analyze_stock(symbol.upper())
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Get summary statistics"""
    results = cache['results']
    
    summary = {
        'total_analyzed': len(results),
        'buy_signals': len([s for s in results if s.get('final_signal') == 'BUY']),
        'fundamental_pass': len([s for s in results if s.get('fundamental_pass', False)]),
        'technical_pass': len([s for s in results if s.get('technical_pass', False)]),
        'avg_fundamental_score': sum([s.get('fundamental_score', 0) for s in results]) / len(results) if results else 0,
        'last_update': cache['last_update'],
    }
    
    return jsonify(summary)

@app.route('/api/update', methods=['POST'])
def trigger_update():
    """Manually trigger analysis update"""
    if cache['updating']:
        return jsonify({'message': 'Update already in progress'}), 400
    
    start_background_update()
    return jsonify({'message': 'Update started'})

@app.route('/api/analyze', methods=['POST'])
def analyze_custom():
    """Analyze custom list of stocks"""
    data = request.json
    symbols = data.get('symbols', [])
    
    if not symbols:
        return jsonify({'error': 'No symbols provided'}), 400
    
    try:
        results = analyzer.batch_analyze(symbols)
        qualified = analyzer.filter_by_criteria(results)
        return jsonify({'stocks': qualified})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'ok',
        'last_update': cache['last_update'],
        'cached_stocks': len(cache['results'])
    })

if __name__ == '__main__':
    # Initial update on startup
    start_background_update()
    
    # Run Flask server
    print("Starting Stock Analysis API Server...")
    print("Access dashboard at http://localhost:5000")
    app.run(debug=True, port=5000)
