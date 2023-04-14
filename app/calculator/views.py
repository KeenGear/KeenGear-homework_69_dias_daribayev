import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def add(request):
    if request.method == 'POST':
        data = request.POST.dict()
        a = data.get('A')
        b = data.get('B')
        if a is None or b is None:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            result = int(a) + int(b)
            return JsonResponse({'answer': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
@require_POST
def subtract(request):
    try:
        data = request.POST.dict()
        a = float(data['A'])
        b = float(data['B'])
        result = a - b
        return JsonResponse({'answer': result})
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

@csrf_exempt
@require_POST
def multiply(request):
    try:
        data = request.POST.dict()
        a = float(data['A'])
        b = float(data['B'])
        result = a * b
        return JsonResponse({'answer': result})
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

@csrf_exempt
@require_POST
def divide(request):
    try:
        data = request.POST.dict()
        a = float(data['A'])
        b = float(data['B'])
        if b == 0:
            return JsonResponse({'error': 'Division by zero!'}, status=400)
        result = a / b
        return JsonResponse({'answer': result})
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)
