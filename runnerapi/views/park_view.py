"""View module for handling requests about park types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from runnerapi.models import Park, Runner


class ParkView(ViewSet):
    """Level up park view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single park

        Returns:
            Response -- JSON serialized park
         """
        park = Park.objects.get(pk=pk)
        serializer = ParkSerializer(park)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all 

        Returns:a
            Response -- JSON serialized list of parks
        """
        park = Park.objects.all()
        serializer = ParkSerializer(park, many=True)
        return Response(serializer.data)
 
class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for park types
    """
    class Meta:
        model = Park
        fields = ('id','name', 'address', 'city', 'zipcode','county','miles_available_to_run', 'difficulty')