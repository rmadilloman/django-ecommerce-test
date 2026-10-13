from django.urls import path
from . import views
from .views import UserProfileView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.process_order, name='process_order'),
    path('chart/', views.sales_chart_page, name='sales_chart_page'),
    path('chart/data/', views.sales_chart_data, name='sales_chart_data'),
    path('register/', views.register, name='register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('test-auth/', TemplateView.as_view(template_name='ventas/test_auth.html'), name='test_auth'),
]