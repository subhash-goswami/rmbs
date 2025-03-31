from django.urls import path

from .views import MortgageListCreateView, MortgageRetrieveUpdateDeleteView

urlpatterns = [
    path('mortgages/', MortgageListCreateView.as_view(), name='mortgage-list-create'),
    path('mortgages/<int:pk>/', MortgageRetrieveUpdateDeleteView.as_view(), name='mortgage-detail'),
]