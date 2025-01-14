import requests
from django.shortcuts import render
from django.conf import settings

def get_stock_data(symbol):
    api_key = settings.ALPHA_VANTAGE_API_KEY
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data.get('Global Quote', {})

def stock_tracker(request):
    stock_data = None
    if request.method == 'POST':
        symbol = request.POST.get('symbol', '').upper()
        stock_data = get_stock_data(symbol)
    return render(request, 'tracker/tracker.html', {'stock_data': stock_data})
