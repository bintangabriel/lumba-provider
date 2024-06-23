from rest_framework import serializers
from .models import ModelTrainingRecord, ObsegModel

class ModelTrainingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTrainingRecord
        fields = ('id', 'status', 'created_time', 'updated_time')

class ObsegModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObsegModel
        fields = ('id', 'name', 'file_name', 'username', 'workspace', 
                  'method', 'algorithm', 'metrics_scores','created_time', 'updated_time')