from django.urls import path, include
from rest_framework import routers

from authentication.serializers import UserOrder
from authentication.views import HelloAuthView, UserCreateView, UserOrderView

route=routers.SimpleRouter()
route.register("order",UserOrderView,basename="user-order")
urlpatterns = [

    path('',HelloAuthView.as_view(),name="hello_auth"),
    path('user/',include(route.urls)),
    path('signup/',UserCreateView.as_view(),name="signup"),

]
