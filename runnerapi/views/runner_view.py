"""View module for handling requests about runner types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from runnerapi.models import Runner, Runner


class RunnerView(ViewSet):
    """RunnerApp runner view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single runner

        Returns:
            Response -- JSON serialized runner
         """
        runner = Runner.objects.get(pk=pk)
        serializer = RunnerSerializer(runner)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def logged_user(self, request):
        """Handle GET requests for the current runner

        Returns:
            Response -- JSON serialized runner
         """

        current_user = Runner.objects.get(user=request.auth.user)
        serializer = RunnerSerializer(current_user)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all 

        Returns:a
            Response -- JSON serialized list of runners
        """
        runner = Runner.objects.all()
        serializer = RunnerSerializer(runner, many=True)
        return Response(serializer.data)

    
class RunnerSerializer(serializers.ModelSerializer):
    """JSON serializer for runner types
    """
    class Meta:
        model = Runner
        fields = ('id','mileage','zipcode', "runner_full_name", "events_assisting")