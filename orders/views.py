from django.shortcuts import render

# Create your views here.
def show_cart(reaquest):
    return render(reaquest,'cart.html')