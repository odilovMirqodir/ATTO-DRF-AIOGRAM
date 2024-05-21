from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreateView.as_view(), name="user-create"),
    path('users/<int:telegram_id>/', views.UserDetailView.as_view(), name="user-detail"),

    path('tarif/', views.TarifCreateView.as_view(), name='tarif-create'),
    path('tarif/<int:pk>/', views.TarifDetailView.as_view(), name='tarif-detail'),

]
