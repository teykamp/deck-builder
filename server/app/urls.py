from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('testcard/', views.testcard),
    path('testcard', views.testcard),
    path('testcard/<int:card_id>', views.yugiohcard),
]
