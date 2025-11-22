from django.urls import path
from .views import DonateMedicineView, DonationListView, AddTrackingView

urlpatterns = [
    path('donate/', DonateMedicineView.as_view(), name='donate_medicine'),
    path('my-donations/', DonationListView.as_view(), name='my_donations'),
    path('tracking/<int:pk>/', AddTrackingView.as_view(), name='add_tracking'),
]
