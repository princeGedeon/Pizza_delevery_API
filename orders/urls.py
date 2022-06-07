from django.urls import path

from orders.views import HelloOrdersView

urlpatterns = [

    path('',HelloOrdersView.as_view(),name="hello_order")
]
