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
