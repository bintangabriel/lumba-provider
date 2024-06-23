from django.http import JsonResponse
from rest_framework.decorators import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def home(req):
  return JsonResponse({'message': 'pong'})