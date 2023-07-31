from django.urls import path
from transactions import views

urlpatterns = [
    path('transactions/', views.transaction_list),
    path('transactions/<int:pk>/', views.transaction_detail),
]
