from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_7dc0a4388c26401bbe90aa3b847c64f3")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticket Symbol Above..."})

    # pk_7dc0a4388c26401bbe90aa3b847c64f3
    # https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_7dc0a4388c26401bbe90aa3b847c64f3




def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': "Enter a Ticket Symbol Above..."})
