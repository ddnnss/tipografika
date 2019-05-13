from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/<order_id>', views.order, name='order'),
    path('clients/', views.clients, name='clients'),
    path('client/<client_id>', views.client, name='client'),

    # path('statistic/', views.statistic, name='statistic'),

]
