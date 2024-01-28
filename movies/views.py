from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all() # Should be 'queryset'
    serializer_class = MovieSerializer # Should be 'serializer_class'

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='Action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='Comedy')
    serializer_class = MovieSerializer