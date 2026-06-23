from django.urls import path
from .views import ItemsView, ItemDetailView

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('items/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
]