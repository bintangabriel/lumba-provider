import json
from .models import *
from .serializers import *
from django.http import JsonResponse
from workspace.models import *
from rest_framework.decorators import *

@api_view(['POST'])
def save_model(request):
    # fetch request file & model metadata
    model_metadata = json.loads(request.body)
    print(model_metadata)
    workspace_type = model_metadata['type']
    

    model_name = model_metadata['model_name']
    file_name = model_metadata['filename']
    username = model_metadata['username']
    workspace = model_metadata['workspace']
    method = model_metadata['model_type']
    metrics_scores = model_metadata['metrics_scores']
    print("metrics scores: ", metrics_scores)
    # score = model_metadata['score']
# fields = ('id', 'name', 'file_name', 'username', 'workspace', 
#                   'method', 'algorithm', 'metrics_scores','created_time', 'updated_time')
    workspace_fk = Workspace.objects.get(name=workspace, username=username, type=workspace_type)
    print(f'workspace: {workspace_fk}')
    payload = {
        'name' : model_name,
        'file_name' : file_name,
        'username': username,
        'workspace' : workspace_fk.id,
        'method' : method,
        'algorithm' : method,
        'metrics_scores' : json.dumps(metrics_scores)
    }
    obsegmodel_serializer = ObsegModelSerializer(data=payload)
    print(payload)

    print(obsegmodel_serializer.is_valid())

    if obsegmodel_serializer.is_valid():
      # save model to db
      print('here')
      obsegmodel_serializer.save()
      print('model saved')

      # create & save modelkey        

      return JsonResponse(obsegmodel_serializer.data)

    return JsonResponse(obsegmodel_serializer.errors)
    
@api_view(['GET'])
def get_workspace(req):
  print('hai')
  workspaces = Workspace.objects.all()
  workspace_list = list(workspaces.values())  # Convert QuerySet to list of dictionaries

  return JsonResponse(workspace_list, safe=False)