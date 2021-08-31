from django.urls import path
from .views import Dashboard, DeleteImage, OrderDetails
urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('delete_image/', DeleteImage.as_view(), name='delete_image'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
]
