# pagos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/crear-pago/', views.crear_pago, name='crear_pago'),
    path('api/estado/<str:id_transaccion>/', views.obtener_estado, name='obtener_estado'),
]