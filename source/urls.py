from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path("", views.company_list, name='home'),

    path('company/create/', views.company_create, name='create_company'),  # Şirket oluşturma sayfası
    path('company/list/', views.company_list, name='company_list'),  # Şirketleri listeleme sayfası
    path('company/edit/<int:company_id>/', views.edit_company, name='company_update'),
    path('company/delete/<int:company_id>/', views.delete_company, name='delete_company'),
    path('getDatasSource/', views.get_data_source, name='get_data_source'),

]
