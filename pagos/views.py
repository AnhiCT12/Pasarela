# pagos/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
from .models import Transaccion

@csrf_exempt
def crear_pago(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            monto = data.get('monto')
            metodo = data.get('metodo_pago')

            # Generar un ID único para la transacción
            id_externo = str(uuid.uuid4())

            # Crear la transacción simulada
            Transaccion.objects.create(
                id_externo=id_externo,
                monto=monto,
                metodo_pago=metodo,
            )
            return JsonResponse({'status': 'pendiente', 'id_transaccion': id_externo})
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Datos inválidos'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def obtener_estado(request, id_transaccion):
    try:
        transaccion = Transaccion.objects.get(id_externo=id_transaccion)
        return JsonResponse({'status': transaccion.estado, 'monto': str(transaccion.monto)})
    except Transaccion.DoesNotExist:
        return JsonResponse({'error': 'Transacción no encontrada'}, status=404)
# Create your views here.
