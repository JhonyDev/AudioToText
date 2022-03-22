from django.urls import path
from django.views.generic import TemplateView
from .views import ConvertRequestCreateView

app_name = "customer-portal"
urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='customer/dashboard.html'), name='dashboard'),
    path('convert-request/add/', ConvertRequestCreateView.as_view(), name='convert-request-add'),
]
