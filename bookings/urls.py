from django.urls import path
from .views import BookingViewSet, LocationViewSet, PaymentViewSet ,VehicleViewSet, BookingDetail,  LocationDetail, PaymentDetail , VehicleDetail


urlpatterns = [
    path('booking/', BookingViewSet.as_view(), name= 'booking'),
    path('booking/<int:pk>/', BookingDetail.as_view(), name ='booking-detail'),
    path('location/', LocationViewSet.as_view(), name= 'location'),
    path('location/<int:pk>/', LocationDetail.as_view(), name ='loaction-detail'),
    path('payment/',PaymentViewSet.as_view(), name= 'payment'),
    path('payment/<int:pk>/', PaymentDetail.as_view(), name ='payment-detail'),
    path('vehicle/', VehicleViewSet.as_view(), name= 'vehicle'),
    path('vehicle/<int:pk>/', VehicleDetail.as_view(), name ='vehicle-detail')
    
]
