from django.urls import path

from authentication.views import HelloAuthView, UserCreateView

urlpatterns = [

    path('',HelloAuthView.as_view(),name="hello_auth"),
    path('signup/',UserCreateView.as_view(),name="signup"),
]
