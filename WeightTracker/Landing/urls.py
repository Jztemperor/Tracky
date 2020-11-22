from django.urls import path
from Landing import views

urlpatterns = [
  path('', views.home, name='landing-home'),
]
