from django.urls import path
from .views import *

urlpatterns = [
  path('save/', save_model),
  path('get', get_workspace)
]
