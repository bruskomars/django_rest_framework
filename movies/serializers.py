from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)# Serialize ImageField
    class Meta:
        model = MovieData
        fields = '__all__'
