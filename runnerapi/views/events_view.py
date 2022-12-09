"""View module for handling requests about park types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from runnerapi.models import Event, Runner, Park


class EventView(ViewSet):
    """Level up eventEvent types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single eventEvent type

        Returns:
            Response -- JSON serialized eventEvent type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        # event_list = []

        # if "park" in request.query_params:
        #     events_fetched = Event.objects.all()
        #     parkId_variable = request.query_params['park']
        #     event_list = events_fetched.filter(park=parkId_variable)
        #     serializer = EventSerializer(event_list, many=True)
        # else:
        #     runner = Runner.objects.get(user=request.auth.user)
        #     # Set the `joined` property on every event
        #     for event in event_list:
        #         # Check to see if the runner is in the attendees list on the event
        #         event.joined = runner in event.attendees.all()

               
        event_list = Event.objects.all()

        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)
            
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized park instance
        """
        runner = Runner.objects.get(user=request.auth.user)
        park = Park.objects.get(pk=request.data["parkId"])

        event = Event.objects.create(
            park = park,
            title=request.data["eventTitle"],
            date=request.data["dateOfRunEvent"],
            time=request.data["timeOfRunEvent"],
            pace_of_run =request.data["runningPaceInMiles"],
            miles_to_run=request.data["milesToRun"],
            organizer = runner
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a park

        Returns:
            Response -- Empty body with 204 status code
        """
        # I AM HERE THIS IS WHERE I LEFT OFF BEFORE LUNCH
        event = Event.objects.get(pk=pk)
        event.title = request.data["eventTitle"]
        event.date = request.data["dateOfRunEvent"]
        event.time = request.data["timeOfRunEvent"]
        event.pace_of_run =request.data["runningPaceInMiles"]
        event.miles_to_run=request.data["milesToRun"]

        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    @action(methods=['post'], detail=True)
    def attend(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        runner = Runner.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(runner)
        return Response({'message': 'Runner added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['DELETE'], detail=True)
    def unattend(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        runner = Runner.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(runner)
        return Response({'message': 'Runner added'}, status=status.HTTP_204_NO_CONTENT)
    
class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Park
        fields = ('id', "name", "address", "zipcode")
    
class RunnerSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Runner
        fields = ('id', "runner_full_name")


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    park = ParkSerializer(many=False)
    attendees = RunnerSerializer(many=True)
    organizer = RunnerSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'title', 'park', 'date', 'time', 
        'pace_of_run','miles_to_run','organizer','attendees')
