from django.urls import path

from djangoapp import views

urlpatterns = [
    path('', views.about, name='demo'),




]