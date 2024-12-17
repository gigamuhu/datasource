from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path("", views.company_list, name='home'),

    path('company/create/', views.company_create, name='create_company'),
    path('company/list/', views.company_list, name='company_list'),
    path('company/detail/<int:company_id>/', views.company_detail, name='company_detail'),
    path('company/edit/<int:company_id>/', views.edit_company, name='company_update'),
    path('company/delete/<int:company_id>/', views.delete_company, name='delete_company'),
    path('siem-test-connect', views.siem_test_connect, name='siem-test-connect'),
    path('company/get-data-source/<int:company_id>/', views.get_data_source, name='get-data-source'),

]
