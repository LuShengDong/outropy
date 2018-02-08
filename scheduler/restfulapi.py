from scheduler.models import Project, Event, Comment
from scheduler.serializers import ProjectSerializer, EventSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjectsList(APIView):
    def get(self, request):
        user = request.user
        projects = Project.objects.filter(user=user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.POST.copy().dict()
        data['user'] = request.user.id
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    def get(self, request, project_id):
        user = request.user
        project = Project.objects.get(user=user, id=project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def delete(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response({'message': 'project does not exist'}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({'message': 'success'}, status=status.HTTP_202_ACCEPTED)


class EventsList(APIView):
    def get(self, request):
        user = request.user
        events = Event.objects.filter(user=user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.POST.copy().dict()
        data['user'] = request.user.id
        try:
            project = Project.objects.get(id=data['project'])
        except:
            return Response('Not Your Project', status=status.HTTP_404_NOT_FOUND)
        if project.user.id != data['user']:
            return Response('Not Your Project', status=status.HTTP_403_FORBIDDEN)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    def get(self, request, event_id):
        user = request.user
        try:
            event = Event.objects.get(user=user, id=event_id)
        except:
            return Response('Not Your Event', status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, event_id):
        try:
            user = request.user
            event = Event.objects.get(user=user, id=event_id)
        except:
            return Response({'message': 'project does not exist'}, status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response({'message': 'success'}, status=status.HTTP_202_ACCEPTED)
