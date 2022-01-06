from .models import Project, Task
from .serializer import ProjectSerializer, TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ProjectList(APIView):

    def get(self, request, format=None):
        projects = Project.objects.all()
        if projects is None:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_204_NO_CONTENT)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors, "code": 0}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ProjectDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(project_id=pk)

        except:

            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(snippet)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(project_id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors, "code": 0}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            project = Project.objects.get(project_id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({"message": "Delete successfully", "code": 1}, status=status.HTTP_204_NO_CONTENT)


@method_decorator(csrf_exempt, name='dispatch')
class TaskList(APIView):

    def get(self, request, format=None):
        task = Task.objects.all()
        if task is None:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_204_NO_CONTENT)

        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "saved data successfully", "code": 1}, status=status.HTTP_200_OK)

        return Response({"error": serializer.errors, "code": 0}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class TaskDetail(APIView):

    def get(self, request, pk, format=None):
        try:

            snippet = Task.objects.get(id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            snippet = Task.objects.get(id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors, "code": 0}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):

        try:
            task = Task.objects.get(id=pk)
        except:

            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({"message": "Delete successfully!", "code": 1}, status=status.HTTP_204_NO_CONTENT)
