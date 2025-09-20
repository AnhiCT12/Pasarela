# pagos/urls.py

from django.urls import path
from . import views

app_name = 'pagos'

urlpatterns = [
    # URLs para la interfaz de usuario (el formulario y la página de estado)
    path('', views.formulario_pago, name='crear_pago'),

    # URLs para la API (si las necesitas después)
    path('api/crear-pago/', views.crear_pago, name='crear_pago'),
    path('api/estado/<str:id_transaccion>/', views.obtener_estado, name='obtener_estado'),

    # URLs actualizadas
    path('crear/', views.crear_pago, name='procesar_pago'),
    path('estado/<str:id_transaccion>/', views.obtener_estado, name='obtener_estado'),
    path('estado-pago/<str:id_transaccion>/', views.estado_pago, name='estado_pago'),
]