from rest_framework import serializers
from scheduler.models import Project, Event, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'user')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'deadline', 'importance', 'scheduled_time', 'project', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post_time', 'event', 'user')
