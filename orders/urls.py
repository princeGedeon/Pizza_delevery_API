from django.urls import path, include

from orders.views import HelloOrdersView, OrderViewSet
from rest_framework import routers
route=routers.SimpleRouter()
route.register("",OrderViewSet,basename="order")
urlpatterns = [
    path('orders/',include(route.urls)),
    path('hello',HelloOrdersView.as_view(),name="hello_order")
]
