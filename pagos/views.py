# pagos/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import uuid
from .models import Transaccion

@csrf_exempt
def crear_pago(request):
    if request.method == 'GET':
        return render(request, 'pagos/formulario_pago.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            monto = data.get('monto')
            metodo = data.get('metodo_pago')
            referencia = data.get('referencia_pago')

            # Generar un ID único para la transacción
            id_externo = str(uuid.uuid4())

            # Crear la transacción simulada
            transaccion = Transaccion.objects.create(
                id_externo=id_externo,
                monto=monto,
                metodo_pago=metodo,
                referencia_pago=referencia
            )
            return JsonResponse({
                'status': 'pendiente', 
                'id_transaccion': id_externo,
                'monto': str(transaccion.monto),
                'metodo': transaccion.metodo_pago
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def obtener_estado(request, id_transaccion):
    try:
        transaccion = Transaccion.objects.get(id_externo=id_transaccion)
        return JsonResponse({'status': transaccion.estado, 'monto': str(transaccion.monto)})
    except Transaccion.DoesNotExist:
        return JsonResponse({'error': 'Transacción no encontrada'}, status=404)

def formulario_pago(request):
    return render(request, 'pagos/formulario_pago.html')

def estado_pago(request, id_transaccion):
    try:
        transaccion = Transaccion.objects.get(id_externo=id_transaccion)
        return render(request, 'pagos/estado_pago.html', {
            'transaccion': transaccion
        })
    except Transaccion.DoesNotExist:
        return JsonResponse({'error': 'Transacción no encontrada'}, status=404)
# Create your views here.
