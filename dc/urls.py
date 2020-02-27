from django.urls import path
from . import views

# skipcq: PYL-C0103
urlpatterns = [
    path('hello/', views.index),
]
