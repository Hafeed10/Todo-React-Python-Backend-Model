from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tasks.models import Tasks
from api.v1.tasks.serializers import TaskSerializer, TaskDeleteSerializer

@api_view(["GET",])
def tasks(request):
    instances = Tasks.objects.filter(is_deleted=False)
    serializer = TaskSerializer(instances, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_task(request, pk):
    try:
        instance = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({"status_code": 6001, "message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            "status_code": 6000,
            "message": "Task Updated Successfully",
            "data": serializer.data,
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6000,
            "message": "Validation failed",
            "data": serializer.errors,
        }
        return Response(response_data)



@api_view(['POST'])
def delete_task(request, pk):
    try:
        instance = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({"status_code": 6001, "message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskDeleteSerializer(instance=instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            "status_code": 6000,
            "message": "Task Updated Successfully",
            "data": serializer.data,
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6000,
            "message": "Validation failed",
            "data": serializer.errors,
        }
        return Response(response_data)
