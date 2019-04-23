from django.shortcuts import render
from django.http import HttpResponseRedirect
from client.models import Client
from order.models import Order
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'crm/index.html', locals())

@login_required
def order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'crm/order.html', locals())

@login_required
def clients(request):
    clients = Client.objects.all()
    return render(request, 'crm/clients.html', locals())
