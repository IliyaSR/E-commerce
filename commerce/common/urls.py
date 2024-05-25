from django.urls import path, include

from commerce.common import views

urlpatterns = [
    path('', views.home, name='home_page'),
]
