from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def add(request):
    try:
        data = request.POST.dict()
        a = float(data['A'])
        b = float(data['B'])
        result = a + b
        return JsonResponse({'answer': result})
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Invalid input data'}, status=400)

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
