from django.db import models
from workspace.models import *

# Create your models here.

class ModelTrainingRecord(models.Model):
    status = models.CharField(max_length=100,default="accepted")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class ObsegModel(models.Model):
    name = models.CharField(max_length=100, default='')
    file_name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default="default")
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    method = models.CharField(max_length=100, default="-")
    algorithm = models.CharField(max_length=100, default="-")
    metrics_scores = models.CharField(max_length=200, default="")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)