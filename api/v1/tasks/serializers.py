from rest_framework.serializers import ModelSerializer
from tasks.models import Tasks

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'datetime', 'is_complete')



class TaskDeleteSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'is_deleted')