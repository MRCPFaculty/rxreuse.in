from django.urls import path
from .views import AvailableMedicinesView, ApplyForAidView, AidDashboardView
from .payment_views import initiate_shipping_payment, payment_success

urlpatterns = [
    path('medicines/', AvailableMedicinesView.as_view(), name='available_medicines'),
    path('apply/', ApplyForAidView.as_view(), name='apply_for_aid'),
    path('dashboard/', AidDashboardView.as_view(), name='aid_dashboard'),
    path('pay/<int:application_id>/', initiate_shipping_payment, name='pay_shipping'),
    path('payment-success/', payment_success, name='payment_success'),
]
