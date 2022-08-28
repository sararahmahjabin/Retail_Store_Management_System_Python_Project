from django.shortcuts import render
from django.contrib import messages

from .models import Order
from .forms import OrderForm
from .models import Product
from InventoryManagement.models import Stock


# Create your views here.
def create_Order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)

        if forms.is_valid():

            order = forms.save(commit=False)

            print(forms)

            product = forms.cleaned_data['product']

            price = product.price

            quantity = forms.cleaned_data['quantity']

            total_price = price*quantity

            order.Price = total_price

            print(total_price, order.Price)

            stock = Stock.objects.get(product=product)
        if stock.Quantity >= quantity:

            stock.Quantity -= quantity
            stock.save()

            order.save()
            messages.info(request, 'Order has been created successfully ✅')

        else:
            messages.info(request, 'Insufficient Stock ⚠️')

    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)

def ShowOrder(request):
    order = Order.objects.all()

    context = {

        'all_Orders' : order
    }

    return render(request, 'store/order_list.html', context)
